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
#brains = app.skipshistorie.portal_catalog(id="brg54119150100000-breim")

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
			print(obj.absolute_url())
			primary_field = IPrimaryFieldInfo(obj)
			if isinstance(primary_field.field, RichText):
					if obj.text:
						oldtext = obj.text.raw
						soup = BeautifulSoup(oldtext, 'html.parser')
						findText = [
							['havn', ' Havn(port):'],

  		                    ['havn', ' Havn (port):'],
		                    ['havn', 'Havn (port):'],
							['havn', 'Havn (port):'],
		                    ['flagg', 'Flagg (flag):'],
	                        ['flagg', ' Flagg (flag):'],
							['flagg', ' Flagg (flag): '],
						    ['skipstype', 'Type'],
							['skipstype', 'Type:'],
							['skipstype', 'Type: '],
							['skipstype', ' Type:'],
							['eier', ' Eier (owner):'],
							['eier', ' Eier (owner):'],
							['eier', 'Eier (owner):'],
							['eier', 'Eier (owner): '],
							['eier', 'Eier (owner):'],
							['navigasjonsutstyr',  'Navigasjonsutstyr:'],
							['navigasjonsutstyr',  ' Navigasjonsutstyr:'],
							['navigasjonsutstyr',  ' Navigasjonsutstyr: '],
							['navigasjonsutstyr',  'Navigasjonsutstyr: '],
							['disponent', 'Disponent (manager):'],
							['disponent', ' Disponent (manager):'],
							['disponent', ' Disponent (manager): '],
							['bnr', ' Bnr (Sno).:'],
							['bnr', 'Bnr (Sno).:'],
							['bnr', 'Bnr (Sno).: '],
							['bnr', 'Bnr(Sno).: '],
							['byggeaar', ' Byggeår (year built):'],
							['byggeaar', 'Byggeår (year built):'],
							['byggeaar', 'Byggeår (year built): '],
							['byggear', ' Bygge&aring;r (year built):'],
							['klasse', 'Klasse (Class).:'],
							['klasse', ' Klasse (Class).:'],
							['klasse', ' Klasse (Class).: '],
							['klasse', ' Klasse(Class).: '],
							['lasthandtering', ' Lasthåndtering'],
							['lasthandtering', 'Lasthåndtering'],
							['lasthandtering', 'Lasthåndtering '],
							['lasthandtering', 'Lasthåndtering '],
							['kjolemaskineri', 'Kjølemaskineri'],
							['kjolemaskineri', ' Kjølemaskineri'],
							['kjolemaskineri', 'Kjølemaskineri'],
							['kjolemaskineri', ' Kjølemaskineri '],
							['tonnasje', ' Tonnasje (Tonnage):'],
							['tonnasje', 'Tonnasje (Tonnage):'],
							['tonnasje', 'Tonnasje (Tonnage): '],
							['tonnasje', ' Tonnasje (Tonnage):'],
							['tonnasje', ' Tonnasje (Tonnage)'],
							['tonnasje', ' Tonnasje (Tonnage) '],
							['tonnasje', 'Tonnasje (Tonnage) '],
							['tonnasje', 'Tonnasje (Tonnage)'],
							['dimensjoner', 'Dimensjoner (size):'],
							['dimensjoner', ' Dimensjoner (size):'],
							['dimensjoner', 'Dimensjoner (size): '],
							['shipyard', 'Bygger (yard):'],
							['shipyard', ' Bygger (yard):'],
							['shipyard', 'Bygger (yard): '],
							['lasthandtering', ' Lasthåndtering'],
							['lasthandtering', 'Lasthåndtering'],
							['lasthandtering', 'Lasthåndtering '],
							['lasthandtering', 'Lasthåndtering '],
							['kjolemaskineri', 'Kjølemaskineri'],
							['kjolemaskineri', ' Kjølemaskineri'],
							['kjolemaskineri', 'Kjølemaskineri'],
							['kjolemaskineri', ' Kjølemaskineri '],
							['kallesignal',' Kallesignal (Call sign):'],
							['kallesignal', 'Kallesignal (Call sign):'],
							['kallesignal', ' Kallesignal (Call sign): '],
							['kallesignal', ' Kallesignal (Call sign.):'],
							['kallesignal', 'Kallesignal (Call sign.): '],
							['off_nr', 'Off.no: '],
							['off_nr', ' Off.no:'],
							['off_nr', ' Off.no: '],
							['off_nr', 'Off.no:'],
							['off_nr', ' Off. nr.:'],
							['off_nr', ' Off. no:'],
							['off_nr', ' Off. no: '],
							['off_nr', ' Off. no:'],
							['off_nr', 'Off.no (IMO):'],

							['manouvering', ' Manøversystemer' ],
							['manouvering', ' Manøversystemer ' ],
							['manouvering', 'Manøversystemer' ],
							['manouvering', 'Manøversystemer ' ],
							['manouvering', 'Manøversystemer ' ],
							['dekkmaskineri', ' Dekksmaskineri'],
							['dekkmaskineri', 'Dekksmaskineri'],
							['dekkmaskineri', ' Dekksmaskineri '],
							['dekkmaskineri', 'Dekksmaskineri '],
							['kommunikasjon', 'Kommunikasjon (comm.):'],
							['kommunikasjon', ' Kommunikasjon (comm.):'],
							['kommunikasjon', ' Kommunikasjon (comm.): '],
							['kommunikasjon', 'Kommunikasjon (comm.): '],
							['fremdrift', 'Fremdrift (propulsion):'],
							['fremdrift', 'Fremdrift (propulsion): '],
							['fremdrift', ' Fremdrift (propulsion):'],
							['fremdrift', ' Fremdrift (propulsion): '],
							['fart', 'Fart/forbr. (speed/cons.): '],
							['fart', ' Fart/forbr. (speed/cons.): '],
							['fart', 'Fart/forbr. (speed/cons.):'],
							['fart', ' Fart/forbr. (speed/cons.): '],
							['hjelpemaskineri', 'Hjelpemaskineri (aux):'],
							['hjelpemaskineri', ' Hjelpemaskineri (aux):'],
							['hjelpemaskineri', ' Hjelpemaskineri (aux): '],
							['hjelpemaskineri', 'Hjelpemaskineri (aux): '],
							['power', ' Tot. el. kraft (el. power):'],
							['power', 'Tot. el. kraft (el. power):'],
							['power', ' Tot. el. kraft (el. power): '],
							['power', 'Tot. el. kraft (el. power): '],
							['power', 'Fart/forbr.(speed/cons.):'],
							['power', ' Fart/forbr.(speed/cons.): '],
							['power', ' Fart/forbr.(speed/cons.):'],
							['power', 'Fart/forbr.(speed/cons.): '],
							['power', ' Tot.el.kraft (el.power):'],
							['power', 'Tot.el.kraft (el.power): '],

							['kjeler', ' Kjeler (boiler): '],
							['kjeler', 'Kjeler (boiler): '],
							['kjeler', ' Kjeler (boiler):'],
							['kjeler', 'Kjeler (boiler):'],
							['kjeler', 'Kjele(r) (boiler):'],
							['kjeler', ' Kjele(r) (boiler):'],
							['kjeler', 'Kjele(r) (boiler): '],
							['kjeler', ' Kjele(r) (boiler): '],
							['kjeler', ' Kjeler (boilers): '],
							['kjeler', 'Kjeler (boilers):'],
							['kjeler', ' Kjeler (boilers):'],
							['kjeler', 'Kjeler (boilers): '],
							['bemanning', 'Bemanning (crew): '],
							['bemanning', ' Bemanning (crew): '],
							['bemanning', ' Bemanning (crew):'],
							['bemanning', 'Bemanning (crew):'],
							['historikk', 'Historikk:'],
							['historikk', ' Historikk:'],
							['historikk', 'Historikk: '],
							['history', 'History in English:'],
							['history', 'History in English: '],
							['history', ' History in English:'],
						]

						for entry in findText:
							#import pdb; pdb.set_trace()
							findField = soup.find(text=entry[1])

							if findField:
								#import pdb; pdb.set_trace()
								print('setting field')
								print(entry[0])
								the_td = findField.find_parent('td')
								the_td['class'] = 'scraped'
								the_td = findField.find_parent('td').find_next('td')
								the_td['class'] = 'scraped'
								if not(getattr(obj, entry[0]) and (len(str(getattr(obj, entry[0]))))>=2):

									try:
										value = findField.find_parent('td').find_next('td').text


										if len(value) >= 2:
											#import pdb; pdb.set_trace()
											setattr(obj, entry[0], value)


									except AttributeError:
										abv = "123"
										#import pdb; pdb.set_trace()
										#print(obj.Title())
									except ValueError:
										abv = "123"
										#import pdb; pdb.set_trace()
										#	print(obj.Title())

						obj.text = RichTextValue(str(soup))
						ant = ant + 1
						if ant % 100 == 1:
							transaction.commit()
						#modified(obj)



		except KeyError as ke:
			#import pdb; pdb.set_trace()
			my_id  = brain.id

			print(ke)


					##move transaction to end of loop
	print(ant)
	transaction.commit()
