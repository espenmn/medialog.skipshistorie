#python 3
#bin/instance run  set_alt_leadimage.py
#cd /home/medialog/vol3/skipshistorie9996/zinstance/; sudo bin/instance run  ../../set_resolve_images.py

from zope.lifecycleevent import modified
import plone.api
from zope.component.hooks import setSite
from plone.app.textfield import RichText
from plone.app.textfield.value import RichTextValue
from plone.rfc822.interfaces import IPrimaryFieldInfo
from plone import api

#Dont need all these
from plone.uuid.interfaces import IUUID
from zope.intid.interfaces import IIntIds
from Products.CMFCore.utils import getToolByName
from z3c.relationfield import RelationValue
from zope.interface import Interface
from zope import component
from zope.intid import IntIds
from zope.intid.interfaces import IIntIds
from zope.component import getUtility
from zExceptions import NotFound
from zope.lifecycleevent import modified
import transaction
from bs4 import BeautifulSoup

#Replace 'skipshistorie' with your own site name
setSite(app['skipshistorie'])
brains = app.skipshistorie.portal_catalog(portal_type="Document")
#Test sith one doucment
#brains = app.skipshistorie.portal_catalog(id="some-document-id")

portal = api.portal.get()

#initids = getUtility(IIntIds)
if brains:
	print('Total  objects counted: ')
	print(len(brains))

	ant = 0
	for brain in   brains:
		obj = None
		obj = brain.getObject()
		try:
			oldtext = obj.text.raw
			soup = BeautifulSoup(oldtext, 'html.parser')

			for bilde in soup.findAll('img'):
				img_link = bilde['src']

				if img_link and not 'resolveuid' in img_link:
					folder_path = '/'.join(obj.aq_parent.getPhysicalPath())           
					folder_path = folder_path + "/" + img_link.replace("../", "").replace("--", "-").replace("-.", ".").replace("..", ".")
					#older_path  = img_link.replace("../", "").replace("--", "-").replace("-.", ".").replace("..", ".")
					folder_path = folder_path.replace("(", "").replace(")", "")
					folder_path = folder_path.replace("+", "-")
					folder_path = folder_path.replace("%C3%B8", "251cy")
					folder_path = folder_path.replace("%C3%98", "o")
					folder_path = folder_path.replace("%C3%86", "251")
					folder_path = folder_path.replace("Ö", "2560")
					folder_path = folder_path.replace("%C3%96", "2560")
					folder_path = folder_path.replace("http://nohost", "")
					folder_path = folder_path.replace("tekster/bilder", "bilder")
					#indeks = folder_path.find(".jpg") 
					#folder_path = folder_path[:indeks+4]   
					#import pdb; pdb.set_trace()
					index = folder_path.find("//skipshisto")
					
					folder_path = folder_path[index+1:]	                                                            



					found_items = None
					try:
						found_items = plone.api.content.get(path=folder_path)


						#print('found it')

					#probably dont need all these
					except AttributeError:
						found_items = None
					except NotFound:
						found_items = None
					except IndexError:
						found_items = None


					if found_items:
						image_uid = found_items.UID()
						new_url= "resolveuid/"  + image_uid
						bilde['src'] = new_url
						ant += 1
						if (ant % 10 == 1):
							#print('transaction')
							transaction.commit()
					else:
						#print('---------------')
						if not ("rederiblader" in obj.absolute_url()):
							print('did not find: ')
							# +  img_link)
							print(obj.absolute_url())
							print(folder_path)
							print('---------------------')


			obj.text = RichTextValue(str(soup))
			#Probably
			modified(obj)

		except AttributeError:
			aaa = 1


transaction.commit()

#print('did not find:')
print(ant)
