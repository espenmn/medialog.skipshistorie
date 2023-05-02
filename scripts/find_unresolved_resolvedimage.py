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
#brains = app.skipshistorie.portal_catalog(id="aac660turbinergenerelt1930")

	#import pdb; pdb.set_trace()

if brains:
	print('Total  objects: ')
	print(len(brains))
	ant = 0
	count = 0

	for brain in brains:
		count += 1
		obj = brain.getObject()

		if obj.text:

			print('.', end="")
			#souptext = obj.text.output

			oldtext = obj.text.raw
			soup = BeautifulSoup(oldtext, 'html.parser')

			bilder = soup.find_all('img')

			if bilder:
				for bilde in bilder:
					billedtext = bilde['src']
					if 'DexterityContent.UID' in billedtext:
						#mport pdb; pdb.set_trace()
						bilde['src'] = bilde['src'].replace("resolveuid/<bound method DexterityContent.UID of <Image at ", "").replace(">>", "")
						print( obj.absolute_url().replace("http://nohost/skipshistorie", "http://skipshistorie.lokalhistorie.org") )



				obj.text = RichTextValue(str(soup))
				modified(obj)

	transaction.commit()
