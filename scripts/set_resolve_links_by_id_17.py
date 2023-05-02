#python 3
#bin/instance run  name.py

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
brains = app.skipshistorie.portal_catalog(portal_type="Document", sort_on="modified", sort_order='ascending')
#Test sith one doucment
#brains = app.skipshistorie.portal_catalog(id="brg54900000100000-skipsliste")

portal = api.portal.get()

ant = 0
#initids = getUtility(IIntIds)
if brains:
	print('Total  objects counted: ')
	print(len(brains))

	#for index, brain in enumerate(brains):
	for brain in  brains:
		obj = None
		obj = brain.getObject()
		#if index % 1000 == 1:
		#	print(index)



		tekst = obj.text
		if tekst != None:
			oldtext = tekst.raw
		else:
			continue

		soup = BeautifulSoup(oldtext, 'html.parser')

		try:


			for reflink in soup.find_all('a'):
				#import pdb; pdb.set_trace()

				ref = reflink['href']

				if ref and not 'resolveuid' in ref and not 'http' in ref and not 'file' in ref and not 'mailto' in ref:


					folder_path = None
					folder_parts = ref.split("/")
					index = None

					folder_path = folder_parts[-1]

					found_items = None

					print('looking')


					if not found_items:
						found_imgs = api.content.find(portal_type="Image")
						#import pdb; pdb.set_trace()

						for imges in found_imgs:
							if imges.id[:17] == folder_path[:17]:
								found_items.append(imges)


					if not found_items:
						found_items= api.content.find(id=folder_path)



					if found_items and len(found_items==1):
						ref_uid = found_items[0].UID()
						new_url= "resolveuid/"  + str(ref_uid)
						reflink['href'] = new_url
						ant += 1
						print('found it')
						abc =123
						if (ant % 1000 == 1):
							#print('transaction')
							transaction.commit()

					else:
						print('not found')
						print(ref)






		except TypeError:
			#import pdb; pdb.set_trace()
			#transaction.commit()
			print('type error')
			print(reflink)
			abc = 123

		except KeyError as ke:
			#a without hfref, mostly 'bad html' skip these
			#print(ke)
			#abc = 123
			#print('key error')
			#print(reflink)
			abc = 1


		except AttributeError:
			#print('attribute eror')
			#a without hfref, mostly 'bad html' skip these

			#print(brain.getPath())
			print(id)
			#import pdb; pdb.set_trace()
			aaa = 1


		obj.text = RichTextValue(str(soup))
		#Probably
		#modified(obj)



transaction.commit()

print(ant)
