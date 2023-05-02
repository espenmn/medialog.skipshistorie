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
brains = app.skipshistorie.portal_catalog()
#brains = app.skipshistorie.portal_catalog(id="stg103brodreneolsen")



if brains:
	print('Total  objects counted: ')
	print(len(brains))

	ant = 0
	xxx = 0
	for brain in  reversed(brains):
		string = brain.Title
		# Add space after the last digit
		string = re.sub(r'(\d)([A-Za-z])', r'\1 \2', string)
		#Add space before every capital letter
		string = re.sub(r'([a-z])([A-Z])', r'\1 \2', string)
		brain.getObject().setTitle(string)


	print(ant)
	transaction.commit()
