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

brains = app.skipshistorie.portal_catalog(portal_type="Document")
#brains = app.skipshistorie.portal_catalog(id="brg54119150100000-breim")

	#import pdb; pdb.set_trace()

if brains:
	print('Total  objects: ')
	print(len(brains))
	ant = 0

	for brain in   brains:
		try:
			obj = brain.getObject()
			#print(obj.Title)
			try:
				if '- ' in obj.Title():
					print('12k34')
					abd = 1234
					#import pdb; pdb.set_trace()
			except TypeError:
				#import pdb; pdb.set_trace()
				obj.Title = obj.Title()
			primary_field = IPrimaryFieldInfo(obj)
			if isinstance(primary_field.field, RichText):
					if obj.text:
						oldtext = obj.text.raw
						soup = BeautifulSoup(oldtext, 'html.parser')
						for tag in soup.find_all('tr'):
							#import pdb; pdb.set_trace()
							if tag.get_text().strip() == '':
								tag['class']  = 'tr-empty'
						obj.text = RichTextValue(str(soup))
						#modified(obj)



		except KeyError as ke:
			#import pdb; pdb.set_trace()
			my_id  = brain.id
			ant = ant + 1
			print(ke)


					##move transaction to end of loop
	print(ant)
	transaction.commit()
