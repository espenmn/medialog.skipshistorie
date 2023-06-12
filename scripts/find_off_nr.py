#python 3
#bin/instance stop; bin/instance run  find_havn_etc.py  -O skipshistorie
#DexterityContent.UID o

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

brains = app.skipshistorie.portal_catalog(portal_type=["Document", "skip"], sort_on="modified", sort_order='descending')
#brains = app.skipshistorie.portal_catalog(id="brg21320100600000-skandi-aker")

	#import pdb; pdb.set_trace()

if brains:
	print('Total  objects: ')
	print(len(brains))
	ant = 0
	count = 0

	for brain in brains:
			count += 1

			obj = brain.getObject()
			if count % 100 == 1:
				print(count)
				print(obj.Title())

			#print(obj.Title)
			try:
				if '- ' in obj.Title():
					print('12k34')
					abd = 1234
					#import pdb; pdb.set_trace()
			except TypeError:
				#import pdb; pdb.set_trace()
				obj.Title = obj.Title()

			if hasattr(obj, 'havn'):
				if obj.havn and obj.portal_type=="Documemt":
					print('changed one')
					obj.portal_tupe = "skip"

			#print(obj.absolute_url().replace("http://nohost/skipshistorie/", "http://skipshistorie.lokalhistorie.org/"))
			primary_field = IPrimaryFieldInfo(obj)
			if isinstance(primary_field.field, RichText):
				if obj.text:
					oldtext = obj.text.output
					oldtext = oldtext.replace(' lang="NO-BOK"', "")
					oldtext = oldtext.replace(' lang="EN-US"', "")
					oldtext = oldtext.replace("</span><span>", "").replace("  ", " ").replace("  ", " ")
					soup = BeautifulSoup(oldtext, 'html.parser')

					#indField = soup.find(text=entry[1])

					findText = [

						['off_nr', 'Off. nr.:'],

					]



					#import pdb; pdb.set_trace()
					if obj.off_nr == '' or obj.off_nr == None:


						for entry in findText:
							#import pdb; pdb.set_trace()
							#print(entry)
							findField = soup.find(text=entry[1])

							if findField:
								#print('found')
								#print(entry[0])
								#import pdb; pdb.set_trace()
								#print('setting field')
								#print(entry[0])
								the_td = findField.find_parent('td')
								the_td['class'] = 'scraped'
								the_td = findField.find_parent('td').find_next('td')
								the_td['class'] = 'scraped'

								#if getattr(obj, entry[0]):
								#import pdb; pdb.set_trace()
								if len(str(getattr(obj, entry[0])))<=5:
											#try:
											value = findField.find_parent('td').find_next('td').text
											value = value.strip().replace("  ", " ")
											if len(str(value)) >= 2:
												print('value set')
												setattr(obj, entry[0], value)
												#print(obj.absolute_url().replace("http://nohost/skipshistorie/", "http://skipshistorie.lokalhistorie.org/"))


											#except AttributeError:
											#abv = "123"
											#import pdb; pdb.set_trace()
											#print(obj.Title())
											#except ValueError:
											#abv = "123"
											#import pdb; pdb.set_trace()
											#	print(obj.Title())

						# Find all <td> tags that contain an <img> tag
						bilder = soup.find_all('img')

						# Add a CSS class to each <td> tag
						if bilder:
							for bilde in bilder:
								#my_tr = bilde.find_parent('td')
								#my_tr['class'] = 'with-image'
								try:
									abc = '123'
									#bilde.find_parent('tr')['class'] = 'with-image'
								except TypeError:
									abc = '123'
									print('error')
									#Do nothing

						if obj.portal_type == 'skip':
							hist_type= type(obj.historikk)

							if  str(hist_type) == "<class 'str'>":
								obj.historikk = RichTextValue(obj.historikk)

							hist_type= type(obj.history)
							if  str(hist_type) == "<class 'str'>":
								obj.history = RichTextValue(obj.history)

						obj.text = RichTextValue(str(soup))
						#obj.setTitle(obj.Title().title())
						ant = ant + 1
						modified(obj)
						if ant % 100 == 1:
							print('transaction')
							transaction.commit()



	print(ant)
	transaction.commit()
