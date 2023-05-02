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

 

#brains = app.skipshistorie.portal_catalog(portal_type="Image")
#brains = app.skipshistorie.portal_catalog()
#Plone6.portal_catalog(portal_type="Image")
brains = app.skipshistorie.portal_catalog()

###Ikke sikker på denne, sjekk heller karen script

import pdb; pdb.set_trace()
if brains:
	print('Total  objects counted: ')
	print(len(brains))
	
	ant = 0
	xxx = 0
	for brain in  brains:
			obj = None
			#try:
			# Use regular expressions to find the index of the last number in the string
			obj = brain.getObject()
			#print(cf.f_lineno)
			#import pdb; pdb.set_trace()
			
			if (isinstance(obj.Title, str)):
				#print(cf.f_lineno)
				b = 1
				tit = obj.Title + '-1'
				obj.setTitle(tit) 
				modified(obj) 
			else:
				ant+=1
				print(cf.f_lineno)
				#import pdb; pdb.set_trace()
				#obj.title = obj.Title()
				#obj.Title = obj.Title()
				tit = obj.Title() + '-1'
				obj.setTitle(tit) 
				modified(obj) 
			

 
	print(xxx)   
		
		
	print(ant)
	transaction.commit()
