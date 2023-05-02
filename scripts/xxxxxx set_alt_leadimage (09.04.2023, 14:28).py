#python 3
#bin/instance run  set_alt_leadimage.py  

from zope.lifecycleevent import modified
import plone.api
from zope.component.hooks import setSite
from plone.app.textfield import RichText
from plone.app.textfield.value import RichTextValue
from plone.rfc822.interfaces import IPrimaryFieldInfo
from plone import api


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


setSite(app['testsite'])
brains = app.testsite.portal_catalog(portal_type="Document")
#initids = getUtility(IIntIds)

if brains:
	print('Total  objects counted: ')
	print(len(brains))
	
	ant = 0

	for brain in  brains:
			obj = None
			obj = brain.getObject()
			
			
			#primary_field = IPrimaryFieldInfo(obj)
			#if isinstance(primary_field.field, RichText):
			#or use obj.text
			oldtext = obj.text.raw
			soup = BeautifulSoup(oldtext, 'html.parser')
			images = soup.find('img')
			print(obj.Title())
			if images:
				img_link = images['src']
             
				if img_link:
					import pdb; pdb.set_trace()
					#find 'resloveuid" in url
					image_uid=img_link.split("/")[2]
					#find catalog object
					image_brain  = app.testsite.portal_catalog(UID=image_uid)[0]
					
					#uuid = IUUID(image_brain.getObject(), None)
					
					#IntIds(image_brain.getObject())
					
					#initids = getUtility(IIntIds)
					
					#obj.related_image.add(image_brain)
					
					#Dont trust AI
					#udi = api.content.get_uuid_from_url(img_link)
					#api.content.get(path='img_link').UID()
					#resolved_object = api.content.get(UID=image_uid)
					#initid_a = initids.getId(obj)
					#initid_b = initids.getId(image_brain.getObject())
					#relation = api.RelationValue(initid_b)
					#intids = getUtility(IIntIds)
					#obj.related_image = RelationValue(image_brain)
					initids = getUtility(IIntIds)
					braini = initids.getId(image_brain.getObject())
					
					obj.related_image = RelationValue( braini )
					#RelationValue(uid=image.UID())
					
					modified(obj)
					

					#obj.related_image = RelationValue(image_brain.intids.getId(iobj))
					
					#ant += 1

transaction.commit()
print(ant)
