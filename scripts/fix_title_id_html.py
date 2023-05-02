#python 3
#bin/instance stop; bin/instance run  change_titlec.py  -O skipshistorie

#import pandas as pd
#import openpyxl
from zope.lifecycleevent import modified
import plone.api
from zope.component.hooks import setSite
from plone.app.textfield import RichText
from plone.app.textfield.value import RichTextValue
from plone.rfc822.interfaces import IPrimaryFieldInfo
from zope.lifecycleevent import modified
import transaction
from bs4 import BeautifulSoup
import re


from inspect import currentframe, getframeinfo

#frameinfo = getframeinfo(currentframe())
cf = currentframe()



setSite(app['skipshistorie'])

#brains = app.skipshistorie.portal_catalog(portal_type="Folder")
brains = app.skipshistorie.portal_catalog(Title=".htm")
#brains = app.skipshistorie.portal_catalog(Title=".Htm")
#brains = app.skipshistorie.portal_catalog(id="brg554oairgens")



if brains:
	print('Total  objects counted: ')
	print(len(brains))

	ant = 0
	xxx = 0
	for brain in  brains:
		obj = brain.getObject()
		obj.setTitle(obj.id.title())



	print(ant)
	transaction.commit()
