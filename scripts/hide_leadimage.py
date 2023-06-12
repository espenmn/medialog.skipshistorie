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
brains = app.skipshistorie.portal_catalog(portal_type="skip",  sort_on="modified", sort_order='ascending')
#brains = app.skipshistorie.portal_catalog(id="hau22618770100000-ida")
#initids = getUtility(IIntIds)
#brains = app.skipshistorie.portal_catalog(id="fre55319630100000-bjornvik")

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
			image = None
			soup = None
			if mytext:
				oldtext = obj.text.raw
				oldtext = oldtext.replace("<div>skipshistorie<body>", "<div><body>")
				soup = BeautifulSoup(oldtext, 'html.parser')
				image = soup.find('img')


			if image:
				if len(image) > 1:
					import pdb; pdb.set_trace()
				img_link = image['src']
				#import pdb; pdb.set_trace()

				if img_link and  'resolveuid'  in img_link:
					#print(obj.Title())
					#find 'resloveuid" in url
					ant += 1
					value = ""
					imgtr = image.find_parent('tr')
					if imgtr:
						imgtr['class']="lead-imaged"
					#	#modified(obj)

			obj.text = RichTextValue(str(soup))

			if ant % 500 == 1:
				print('transaction')
				transaction.commit()

		except IndexError:
			print('hallo')

	transaction.commit()
	print(ant)
