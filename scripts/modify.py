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
brains = app.skipshistorie.portal_catalog(portal_type="skip")
#Test sith one doucment
#brains = app.skipshistorie.portal_catalog(id="423sugelstad")

portal = api.portal.get()

#initids = getUtility(IIntIds)
if brains:
	print('Total  objects counted: ')
	print(len(brains))

	ant = 0
	#for index, brain in enumerate(brains):
	for brain in  brains:
		obj = brain.getObject()
		#import pdb; pdb.set_trace()
		
		obj.konstruksjon = str(obj.konstruksjon)
		obj.skipstype__bruk_ = str(obj.skipstype__bruk_)
		if obj.konstruksjon  == 'None':
			obj.konstruksjon = ''
			
		if obj.skipstype__bruk_  == 'None':
			obj.skipstype__bruk_ =''
			

		modified(obj)
		ant += 1
		if ant % 500 == 1:
			transaction.commit()
			print('trans')


transaction.commit()

#print(ant)
