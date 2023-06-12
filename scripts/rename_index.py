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
brains = app.skipshistorie.portal_catalog(portal_type="Document", id="index")
#Test sith one doucment
#brains = app.skipshistorie.portal_catalog(id="brg54900000100000-skipsliste")

portal = api.portal.get()

#initids = getUtility(IIntIds)
if brains:
	print('Total  objects counted: ')
	print(len(brains))

	ant = 0
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

				ref = reflink['href']
				folder_path = None

				found_refs = 1
				if ref and not 'resolveuid' in ref and not 'http' in ref and not 'file' in ref and not 'mailto' in ref:
					found_refs = 0

				if found_refs == 1:
					api.content.rename(obj=obj, new_id='index.html')
					ant += 1

					if ant % 50:
						transaction.commit()




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



		except AttributeError as at:
				print(at)
				print('attribute eror')

				print(ref)
				#import pdb; pdb.set_trace()
				aaa = 1

transaction.commit()

#print(ant)
