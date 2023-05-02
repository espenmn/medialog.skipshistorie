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
brains = app.skipshistorie.portal_catalog(id="hong kong")

	#import pdb; pdb.set_trace()

if brains:
	print('Total  objects: ')
	print(len(brains))
	ant = 0
	
	for brain in  brains:
		print('hong')
		obj = None
		try:
			obj = brain.getObject()
			#print(obj.Title)
			a = 1

		except KeyError as ke:
			import pdb; pdb.set_trace()
			my_id  = brain.id
			xxxx = ke.args[0]
			brainse = app.skipshistorie.portal_catalog(id=xxxx)
			ant = ant + 1
			for braine in brains:
			    obj = brain.getObject()
			    print(ke)
			    transaction.commit()
			    modified(obj)
				
			
					##move transaction to end of loop
	print(ant)
	transaction.commit()
