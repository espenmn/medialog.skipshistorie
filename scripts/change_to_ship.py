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
brains = app.skipshistorie.portal_catalog(portal_type="Document")
#Test sith one doucment
#brains = app.skipshistorie.portal_catalog(id="brg12419150200000-gustav-vigeland")

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
		if obj.kallesignal and obj.kallesignal != '':
			obj.portal_type = "skip"
			brain_portal_type = "skip"
			obj.layout = "boat-view"

		if obj.vessel and obj.vessel != '':
			obj.portal_type = "skip"
			brain_portal_type = "skip"
			obj.layout = "boat-view"

		modified(obj)



transaction.commit()

#print(ant)
