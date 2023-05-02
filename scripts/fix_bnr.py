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
#brains = app.skipshistorie.portal_catalog(id="osl33019580500000-hoegh-ailette")

#import pdb; pdb.set_trace()

if brains:
	print('Total  objects: ')
	print(len(brains))
	ant = 0
	count = 0

	for brain in brains:
		count += 1
		obj = brain.getObject()
		bnr = obj.bnr
		#setattr(obj, "bnr", None )
		try:
			if bnr  and bnr  != None and bnr  != 'None':
				if bnr  == '':
					setattr(obj, "bnr", None )
				else:
					#bnr = str(bnr) + ' '
					obj.bnr = str(bnr)
		except ValueError:
			print(bnr)
			print(obj.Title())

		#modified(obj)
		#transaction.commit()


					##move transaction to end of loop
	print(ant)
	transaction.commit()
