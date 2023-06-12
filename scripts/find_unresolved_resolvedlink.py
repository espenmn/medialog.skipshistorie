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
#brains = app.skipshistorie.portal_catalog(id="lagt-ut-i-2015")

	#import pdb; pdb.set_trace()

if brains:
	print('Total  objects: ')
	print(len(brains))
	ant = 0
	count = 0

	for brain in brains:
		count += 1
		changed = 0
		obj = brain.getObject()

		if obj.text:

			print('.', end="")
			#souptext = obj.text.output

			oldtext = obj.text.raw
			soup = BeautifulSoup(oldtext, 'html.parser')

			lenker = soup.find_all('a')

			if lenker:
				for lenke in lenker:

					try:
						lenketext = lenke['href']
						changed = 1
						if " for" in lenketext:
							#import pdb; pdb.set_trace()
							print(lenke['href'])
							print(obj.absolute_url)

						if not 'resolve' in lenketext:
							if not'http' in lenketext:
								#import pdb; pdb.set_trace()
								#print(lenke['href'])
								abc = 1

						if 'DexterityContent.UID' in lenketext:

							lenke['href'] = lenke['href'].replace("resolveuid/<bound method DexterityContent.UID of <File at ", "").replace("skipshistorie/", "")
							lenke['href'] = lenke['href'].replace("resolveuid/<bound method DexterityContent.UID of <Document at ", "").replace("skipshistorie/", "")
							lenke['href'] = lenke['href'].replace("resolveuid/<bound method DexterityContent.UID of <Folder at ", "").replace("skipshistorie/", "")
							lenke['href'] = lenke['href'].replace("resolveuid/&lt;bound method DexterityContent.UID of Image at ", "").replace("&gt;&gt", "").replace("skipshistorie/", "")
							lenke['href'] = lenke['href'].replace("resolveuid/<bound method DexterityContent.UID of <Image at ","").replace(">>", "").replace("skipshistorie/", "")
							if "UID" in lenke['href']:
								#import pdb; pdb.set_trace()
								print(lenke['href'])
								print(obj.absolute_url)
					except KeyError:
						abc=1

		if changed != 0:
			obj.text = RichTextValue(str(soup))
			modified(obj)

	transaction.commit()
