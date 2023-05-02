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
#brains = app.skipshistorie.portal_catalog(id="brg554oairgens")



if brains:
	print('Total  objects counted: ')
	print(len(brains))
	
	ant = 0
	xxx = 0
	for brain in  brains:
		obj = None
		try:
			# Use regular expressions to find the index of the last number in the string
			obj = brain.getObject()
			#print(cf.f_lineno)
			#import pdb; pdb.set_trace()
			
			if (isinstance(obj.Title, str)):
				#print(cf.f_lineno)
				b = 1
				obj.Title = obj.Title 
			else:
				ant+=1
				print(cf.f_lineno)
				#import pdb; pdb.set_trace()
				#obj.title = obj.Title()
				obj.Title = obj.Title()
				modified(obj)
				transaction.commit()
			
		except  KeyError:
			print('key error')
			#import pdb; pdb.set_trace()
			xxx = xxx + 1
		
		if (isinstance(brain.Title, str)):
			abc = 1
		else:
			abc=1
			print('else')
			#import pdb; pdb.set_trace()
		
	print(xxx)   
		
		
	print(ant)
	transaction.commit()
