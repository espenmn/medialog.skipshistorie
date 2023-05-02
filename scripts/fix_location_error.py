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

brains = app.skipshistorie.portal_catalog(portal_type="Document", sort_on="modified", sort_order='ascending')
#brains = app.skipshistorie.portal_catalog(id="osl32419320100000-torlak")

#import pdb; pdb.set_trace()

if brains:
	print('Total  objects: ')
	print(len(brains))
	ant = 0
	count = 0

	for brain in brains:
		count += 1
		obj = brain.getObject()
		#import pdb; pdb.set_trace()
		hist_type= type(obj.historikk)


		#if isinstance(hist_type, str):
		if  str(hist_type) == "<class 'str'>":
			obj.historikk = RichTextValue(obj.historikk)
		#transaction.commit()

		hist_type= type(obj.history)
		#if isinstance(hist_type, str):
		if  str(hist_type) == "<class 'str'>":
  			obj.history = RichTextValue(obj.history)
		#transaction.commit()

					##move transaction to end of loop
	print(ant)
	transaction.commit()
