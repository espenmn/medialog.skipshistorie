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

brains = app.skipshistorie.portal_catalog(id="osl36919500100000-stalheim")
#brains = app.skipshistorie.portal_catalog(id="fre54119730200000-cape-york")

	#import pdb; pdb.set_trace()

if brains:
	print('Total  objects: ')
	print(len(brains))
	ant = 0

	for brain in brains:
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

			print(obj.absolute_url().replace("http://nohost/skipshistorie/", "http://skipshistorie.lokalhistorie.org/"))
			primary_field = IPrimaryFieldInfo(obj)
			if isinstance(primary_field.field, RichText):
					if obj.text:
						oldtext = obj.text.raw
						soup = BeautifulSoup(oldtext, 'html.parser')
						findText = [
							['bemanning', ' Bemanning (crew): '],
							['bemanning', ' Bemanning (crew):'],
							['bemanning', 'Bemanning (crew): '],
							['bemanning', 'Bemanning (crew):'],
							['bnr', ' Bnr (Sno).:'],
							['bnr', 'Bnr (Sno).: '],
							['bnr', 'Bnr (Sno).:'],
							['bnr', 'Bnr(Sno).: '],
							['bnr', 'Bnr (Sno).:'],
							['bnr', 'Bnr (Sno):'],
							['byggeaar', ' Bygge&aring;r (year built):'],
							['byggeaar', ' Byggeår (year built):'],
							['byggeaar', 'Byggeår (year built): '],
							['byggeaar', 'Byggeår (year built):'],
							['dekkmaskineri', ' Dekksmaskineri '],
							['dekkmaskineri', ' Dekksmaskineri'],
							['dekkmaskineri', 'Dekksmaskineri '],
							['dekkmaskineri', 'Dekksmaskineri'],
							['dimensjoner', ' Dimensjoner (size):'],
							['dimensjoner', 'Dimensjoner (size): '],
							['dimensjoner', 'Dimensjoner (size):'],
							['disponent', ' Disponent (manager): '],
							['disponent', ' Disponent (manager):'],
							['disponent', 'Disponent (manager):'],
							['eier', ' Eier (owner):'],
							['eier', ' Eier (owner):'],
							['eier', 'Eier (owner): '],
							['eier', 'Eier (owner):'],
							['eier', 'Eier (owner):'],
							['fart', ' Fart/forbr. (speed/cons.): '],
							['fart', ' Fart/forbr. (speed/cons.): '],
							['fart', 'Fart/forbr. (speed/cons.): '],
							['fart', 'Fart/forbr. (speed/cons.):'],
							['flagg', ' Flagg (flag): '],
	                        ['flagg', ' Flagg (flag):'],
		                    ['flagg', 'Flagg (flag):'],
							['fremdrift', ' Fremdrift (propulsion): '],
							['fremdrift', ' Fremdrift (propulsion):'],
							['fremdrift', 'Fremdrift (propulsion): '],
							['fremdrift', 'Fremdrift (propulsion):'],
  		                    ['havn', ' Havn (port):'],
							['havn', ' Havn(port):'],
		                    ['havn', 'Havn (port):'],
							['havn', 'Havn (port):'],
							['havn', 'Havn(port):'],
							['havn', 'Havn(port): '],
							['historikk', ' Historikk:'],
							['historikk', 'Historikk: '],
							['historikk', 'Historikk:'],
							['history', ' History in English:'],
							['history', 'History in English: '],
							['history', 'History in English:'],
							['hjelpemaskineri', ' Hjelpemaskineri (aux): '],
							['hjelpemaskineri', ' Hjelpemaskineri (aux):'],
							['hjelpemaskineri', 'Hjelpemaskineri (aux): '],
							['hjelpemaskineri', 'Hjelpemaskineri (aux):'],
							['kallesignal', ' Kallesignal (Call sign.):'],
							['kallesignal', ' Kallesignal (Call sign): '],
							['kallesignal', 'Kallesignal (Call sign.): '],
							['kallesignal', 'Kallesignal (Call sign):'],
							['kallesignal',' Kallesignal (Call sign):'],
							['kjeler', ' Kjele(r) (boiler): '],
							['kjeler', ' Kjele(r) (boiler):'],
							['kjeler', ' Kjeler (boiler): '],
							['kjeler', ' Kjeler (boiler):'],
							['kjeler', ' Kjeler (boilers): '],
							['kjeler', ' Kjeler (boilers):'],
							['kjeler', 'Kjele(r) (boiler): '],
							['kjeler', 'Kjele(r) (boiler):'],
							['kjeler', 'Kjeler (boiler): '],
							['kjeler', 'Kjeler (boiler):'],
							['kjeler', 'Kjeler (boilers): '],
							['kjeler', 'Kjeler (boilers):'],
							['kjolemaskineri', ' Kjølemaskineri '],
							['kjolemaskineri', ' Kjølemaskineri '],
							['kjolemaskineri', ' Kjølemaskineri'],
							['kjolemaskineri', ' Kjølemaskineri'],
							['kjolemaskineri', 'Kjølemaskineri'],
							['kjolemaskineri', 'Kjølemaskineri'],
							['kjolemaskineri', 'Kjølemaskineri'],
							['kjolemaskineri', 'Kjølemaskineri'],
							['klasse', ' Klasse (Class).: '],
							['klasse', ' Klasse (Class).:'],
							['klasse', ' Klasse(Class).: '],
							['klasse', 'Klasse (Class).:'],
							['klasse', 'Klasse (Class'],
							['klasse', ' Klasse (Class'],
							['kommunikasjon', ' Kommunikasjon (comm.): '],
							['kommunikasjon', ' Kommunikasjon (comm.):'],
							['kommunikasjon', 'Kommunikasjon (comm.): '],
							['kommunikasjon', 'Kommunikasjon (comm.):'],
							['kommunikasjon', ' Kommunikasjon'],
							['lasthandtering', ' Lasthåndtering'],
							['lasthandtering', ' Lasthåndtering'],
							['lasthandtering', ' Lasthåndtering '],
							['lasthandtering', 'Lasthåndtering '],
							['lasthandtering', 'Lasthåndtering'],
							['manouvering', ' Manøversystemer ' ],
							['manouvering', ' Manøversystemer' ],
							['manouvering', 'Manøversystemer ' ],
							['manouvering', 'Manøversystemer ' ],
							['manouvering', 'Manøversystemer' ],
							['navigasjonsutstyr',  ' Navigasjonsutstyr: '],
							['navigasjonsutstyr',  ' Navigasjonsutstyr:'],
							['navigasjonsutstyr',  'Navigasjonsutstyr: '],
							['navigasjonsutstyr',  'Navigasjonsutstyr:'],
							['off_nr', ' Off. no: '],
							['off_nr', ' Off. no:'],
							['off_nr', ' Off. no:'],
							['off_nr', ' Off. nr.:'],
							['off_nr', ' Off.no: '],
							['off_nr', ' Off.no:'],
							['off_nr', 'Off.no (IMO):'],
							['off_nr', 'Off.no: '],
							['off_nr', 'Off.no:'],
							['power', ' Fart/forbr.(speed/cons.): '],
							['power', ' Fart/forbr.(speed/cons.):'],
							['power', ' Tot. el. kraft (el. power): '],
							['power', ' Tot. el. kraft (el. power):'],
							['power', ' Tot.el.kraft (el.power):'],
							['power', 'Fart/forbr.(speed/cons.): '],
							['power', 'Fart/forbr.(speed/cons.):'],
							['power', 'Tot. el. kraft (el. power): '],
							['power', 'Tot. el. kraft (el. power):'],
							['power', 'Tot.el.kraft (el.power): '],
							['shipyard', ' Bygger (yard):'],
							['shipyard', 'Bygger (yard): '],
							['shipyard', 'Bygger (yard):'],
							['skipstype', ' Type:'],
							['skipstype', 'Type: '],
							['skipstype', 'Type:'],
						    ['skipstype', 'Type'],
							['tonnasje', ' Tonnasje (Tonnage) '],
							['tonnasje', ' Tonnasje (Tonnage):'],
							['tonnasje', ' Tonnasje (Tonnage):'],
							['tonnasje', ' Tonnasje (Tonnage)'],
							['tonnasje', 'Tonnasje (Tonnage) '],
							['tonnasje', 'Tonnasje (Tonnage): '],
							['tonnasje', 'Tonnasje (Tonnage):'],
							['tonnasje', 'Tonnasje (Tonnage)'],

						]



						for entry in findText:
							#import pdb; pdb.set_trace()
							findField = soup.find(text=entry[1])

							if findField:
									#import pdb; pdb.set_trace()
									#print('setting field')
									#print(entry[0])
									the_td = findField.find_parent('td')
									the_td['class'] = 'scraped'
									the_td = findField.find_parent('td').find_next('td')
									the_td['class'] = 'scraped'

									#if getattr(obj, entry[0]):
									#import pdb; pdb.set_trace()
									if len(str(getattr(obj, entry[0])))>=2:
											#try:
											value = findField.find_parent('td').find_next('td').text
											if len(str(value)) >= 2:
												setattr(obj, entry[0], value)

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
									bilde.find_parent('tr')['class'] = 'with-image'
								except TypeError:
									abc = '123'
									print('error')
									#Do nothing

						obj.text = RichTextValue(str(soup))
						obj.setTitle(obj.Title().title())
						ant = ant + 1
						modified(obj)
						if ant % 100 == 1:
							print('transaction')
							transaction.commit()
						#modified(obj)



		except KeyError as ke:
			#import pdb; pdb.set_trace()
			my_id  = brain.id
			print('eroor ke')

			print(ke)


					##move transaction to end of loop
	print(ant)
	transaction.commit()
