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
brains = app.skipshistorie.portal_catalog(portal_type="Folder", Subject="Rederi")
#Test sith one doucment
#brains = app.skipshistorie.portal_catalog(id="stg135thssfalck")

portal = api.portal.get()

#initids = getUtility(IIntIds)
if brains:
	print('Total  objects counted: ')
	print(len(brains))

	ant = 0
	#for index, brain in enumerate(brains):
	for brain in  brains:
		obj = brain.getObject()
		rederinummer = obj.rederinummer



		if rederinummer and rederinummer !='':
			#import pdb; pdb.set_trace()
			if "Byer" in obj.aq_parent.Subject():
				by = obj.aq_parent.Title()
				obj.by = by

			tit = obj.Title().replace(rederinummer, "").strip()
			obj.setTitle(tit)
			modified(obj)



transaction.commit()

#print(ant)
