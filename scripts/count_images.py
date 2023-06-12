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
#from plone.uuid.interfaces import IUUID
#from zope.intid.interfaces import IIntIds
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


portal = api.portal.get()
if brains:
	for brain in   brains:
		obj = brain.getObject()
		btext = obj.text
		#import pdb; pdb.set_trace()
		if btext:
			oldtext = btext.raw
			soup = BeautifulSoup(oldtext, 'html.parser')

			firstImage = soup.find('img')
			#hasattr(object, attribute)
			#firstImage.has_attr('class')
			if firstImage:
				parent = firstImage.find_parent('tr')
				if parent and parent.get("class"):
					if 'with-image' in parent['class']:
						parent['class'] = 'with-leadimage'

					obj.text = RichTextValue(str(soup))
					modified(obj)



transaction.commit()
