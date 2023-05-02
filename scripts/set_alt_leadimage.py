#python 3
#bin/instance run  set_alt_leadimage.py

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

#from zope.lifecycleevent import modified
import transaction
from bs4 import BeautifulSoup




setSite(app['skipshistorie'])
brains = app.skipshistorie.portal_catalog(portal_type="Document",  sort_on="modified", sort_order='ascending')
#brains = app.skipshistorie.portal_catalog(id="hau22618770100000-ida")
#initids = getUtility(IIntIds)
#brains = app.skipshistorie.portal_catalog(id="stg12418960300000-fram")

#import pdb; pdb.set_trace()

if brains:
	print('Total  objects counted: ')
	print(len(brains))

	ant = 0

	for brain in  brains:
		try:
			obj = None
			obj = brain.getObject()
			mytext = obj.text
			images = None
			soup = None
			if mytext:
				oldtext = obj.text.raw
				soup = BeautifulSoup(oldtext, 'html.parser')
				images = soup.find('img')


			if images:
				img_link = images['src']
				#import pdb; pdb.set_trace()

				if img_link and  'resolveuid'  in img_link:
					#print(obj.Title())
					#find 'resloveuid" in url
					image_uid=img_link.split("/")[-1]

					#find catalog object
					image_brain  = app.skipshistorie.portal_catalog(UID=image_uid)[0]

					initids = getUtility(IIntIds)
					braini = initids.getId(image_brain.getObject())

					obj.related_image = RelationValue( braini )
					modified(obj)

					ant += 1
					value = ""
					imgtr = images.find_parent('tr')
					if imgtr:
						imgtr['class']="lead-imaged"
					try:
						capttd = value = images.find_parent('td').find_next('td')
						value = capttd.text
					except ValueError:
						abc = 124
					except AttributeError:
						abc = 123
					if value and len(value) >= 3 and len(value) < 100 :
						#import pdb; pdb.set_trace()
						capttd['class']="lead-captioned"
						print(value)
						setattr(obj,  'image_caption' , value)
			#try:
			#	#modified(obj)
			#except ValueError:
			#	print('value error')
			#	abc ="123"
			if soup:
				obj.text = RichTextValue(str(soup))
				
			if "Båt" in obj.Subject():
				obj.layout = "boat-view"
				
			if ant % 500 == 1:
				print('transaction')
				transaction.commit()

		except IndexError:
			print('hallo')
		
	transaction.commit()
	print(ant)
