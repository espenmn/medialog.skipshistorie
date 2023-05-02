
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

from zope.lifecycleevent import modified
import transaction
from bs4 import BeautifulSoup


from zExceptions import NotFound


setSite(app['skipshistorie'])


brains = app.skipshistorie.portal_catalog(portal_type="Document")
#initids = getUtility(IIntIds)

if brains:
	print('Total  objects counted: ')
	print(len(brains))

	ant = 0

	for brain in  reversed(brains):
		obj = None
		obj = brain.getObject()
		try:
			oldtext = obj.text.raw
			soup = BeautifulSoup(oldtext, 'html.parser')
			#images = soup.find('img')
			#print(obj.Title())

			#import pdb; pdb.set_trace()

			for bilde in soup.findAll('img'):
  				#bilde['src'] = a['href'].replace("google", "mysite")
				img_link = bilde['src']

				if img_link and not 'resolveuid' in img_link:
					#import pdb; pdb.set_trace()
					img_id = img_link.split("/")[-1].replace("-.", ".").replace("..", ".")
					found_items = None
					try:
						found_items = api.content.find(id=img_id)
						#print('found it')

					#probably dont need all these
					except AttributeError:
						found_items = None
					except NotFound:
						found_items = None
					except IndexError:
						found_items = None


					#image_url = obj.path or something + img_link replace "../", "/" ?

					if found_items and len(found_items) == 1:
						image_uid = found_items[0].UID()
						new_url= "resolveuid/"  + str(image_uid)
						bilde['src'] = new_url
						ant += 1
						if (ant % 500 == 1):
							#print('transaction')
							transaction.commit()
					else:
						print('---------------')
						#import pdb; pdb.set_trace()
						print('did not find one: ' +  img_link)
						print(obj.Title())
						print(obj.id)
						print(img_link)



			obj.text = RichTextValue(str(soup))
			modified(obj)

		except AttributeError:
				a = 1





transaction.commit()
print(ant)
