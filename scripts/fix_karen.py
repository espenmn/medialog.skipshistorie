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



#setSite(app['Plone6'])

#brains = app.skipshistorie.portal_catalog(portal_type="Image")
brains = app.skipshistorie.portal_catalog()
#brains = app.Plone6.portal_catalog(portal_type="Image")
#brains = brg54419170320001-karen.jpg


import pdb; pdb.set_trace()
if brains:
	print('Total  objects counted: ')
	print(len(brains))
	
	ant = 0
	xxx = 0
	for brain in  brains:
			obj = None
			#import pdb; pdb.set_trace()
			#try:
			# Use regular expressions to find the index of the last number in the string
			obj = brain.getObject()
			#print(cf.f_lineno)
			#import pdb; pdb.set_trace()
			
			try:
				delattr(obj, "Title") 
			except AttributeError:
				print('go on')
			finally:
				a = 1
			
			if (isinstance(obj.title, str)):
				#print(cf.f_lineno)
				ant+=1
				print('change')
				#tit = obj.title + '-1'
				tit = obj.title.replace("-1", "")
				obj.setTitle(tit) 
				#api.content.rename(obj=obj, new_id=obj.id.replace("-1", ""))
             	
				modified(obj) 
			else:
				ant+=1
				print(cf.f_lineno)
				#import pdb; pdb.set_trace()
				#obj.title = obj.Title()
				#obj.Title = obj.Title()
				tit = obj.title.replace("-1", "")
				#tit = obj.title + '-1'
				obj.setTitle(tit) 
				modified(obj) 
				
			#api.content.rename(obj=obj, new_id=obj.id.replace("-1", ""))
		
	print(ant)
	transaction.commit()
