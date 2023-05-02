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
#brains = app.skipshistorie.portal_catalog(id="tbg10119480300000-baleine")

	#import pdb; pdb.set_trace()

if brains:
	print('Total  objects: ')
	print(len(brains))
	ant = 0
	count = 0
	myList = []
	for brain in brains:
			obj = brain.getObject()
			
			#import pdb; pdb.set_trace()
			primary_field = IPrimaryFieldInfo(obj)
			if isinstance(primary_field.field, RichText):
				if obj.text:
					#We found rich text
					oldtext = obj.text.output
					soup = BeautifulSoup(oldtext, 'html.parser')
						
					findFields = soup.findAll('td')
						
					for findField in findFields:

						if findField:
							klass = []
							try: 
								klass = findField['class']
							except KeyError:
								klass = []
							if not (klass and 'scraped' in findField['class']):
								if not (klass and 'lead-captioned' in findField['class']):
									findText = findField.text
									parenttr = findField.find_parent('tr')
									if findField.text:
										if len(findText) >=3 and len(findText) < 50:
											#import pdb; pdb.set_trace()
										
											try:
												if not (parenttr['class'] and 'tr-empty'  in parenttr['class'] ) :
													#print('\""', end='')
													myList.append("'" + findText +"'")
													#print('\"')
											except KeyError:
												myList.append("'" + findText +"'")
											
 
										
				
	print(set(myList))			
