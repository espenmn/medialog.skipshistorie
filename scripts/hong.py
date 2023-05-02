#python 3
#bin/instance stop; bin/instance run  find_havn_etc.py  -O skipshistorie

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


setSite(app['skipshistorie'])

#brains = app.skipshistorie.portal_catalog(portal_type="Folder")
#brains = plone.api.content.find(depth=2)
brains = app.skipshistorie.portal_catalog()

	#import pdb; pdb.set_trace()

if brains:
	print('Total  objects: ')
	print(len(brains))
	ant = 0
	
	mykeys = set()
	
	for brain in  brains:
			#if 'hong' in brain.id:
			#print('hong')
			obj = None
			try:
				obj = brain.getObject()
				#print(obj.Title)
				a = 1

			except KeyError as ke:
				#import pdb; pdb.set_trace()
				#print(ke)
				print(brain.getPath())
				mykeys.add(ke.args[0])
				my_id  = brain.id
			
				
			
					##move transaction to end of loop
	print(ant)
	print(mykeys)
	transaction.commit()
