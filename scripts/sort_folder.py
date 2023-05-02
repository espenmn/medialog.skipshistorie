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
#from bs4 import BeautifulSoup
from Products.CMFCore.utils import getToolByName

#Replace 'skipshistorie' with your own site name
setSite(app['skipshistorie'])
brains = app.skipshistorie.portal_catalog(portal_type="Folder", sort_on="modified", sort_order='ascending')

brains = app.skipshistorie.portal_catalog(id="osl317fearnley-eger")

portal = api.portal.get()


for brain in brains:
	"""Sort the contents of a folder alphabetically"""
	import pdb; pdb.set_trace()

	obj = brain.getObject()
	results = brain.getObject().contentItems().sort(key=lambda x: x[0])

	#results.sort(key=lambda x: x[0])

for result in results:
	#obj = result.getObject()
	order = result[1].getOrdering()
	order.setWeight(100000 + result.sortable_title)

transaction.commit()
