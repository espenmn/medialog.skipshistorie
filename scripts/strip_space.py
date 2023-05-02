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
#brains = app.skipshistorie.portal_catalog(id="hal70519060100000-france")

	#import pdb; pdb.set_trace()

if brains:
	print('Total  objects: ')
	print(len(brains))
	ant = 0

	for brain in brains:
						obj = brain.getObject()
						 
						ant += 1
			
						findText = [
							['bemanning', ' Bemanning (crew): '],
							['bnr', ' Bnr (Sno).:'],
							['byggeaar', ' Bygge&aring;r (year built):'],
							['dekkmaskineri', ' Dekksmaskineri '],
							['dimensjoner', 'Dimensjoner (size): '],
							['disponent', 'Disponent (manager):'],
							['eier', ' Eier (owner):'],
							['eier', 'Eier (owner):'],
							['fart', 'Fart/forbr. (speed/cons.):'],
							['flagg', 'Flagg (flag):'],
							['fremdrift', 'Fremdrift (propulsion):'],
  		                    ['havn', 'Havn(port): '],
							['hjelpemaskineri', ' Hjelpemaskineri (aux): '],
							['kallesignal', ' Kallesignal (Call sign.):'],
							['kjeler', 'Kjeler (boilers):'],
							['kjolemaskineri', 'Kjølemaskineri'],
							['klasse', ' Klasse (Class'],
							['kommunikasjon', 'Kommunikasjon (comm.):'],
							['lasthandtering', 'Lasthåndtering'],
							['manouvering', 'Manøversystemer' ],
							['navigasjonsutstyr',  'Navigasjonsutstyr:'],
							['off_nr', 'Off.no:'],
							['power', 'Tot. el. kraft (el. power):'],
							['power', 'Tot.el.kraft (el.power): '],
							['shipyard', ' Bygger (yard):'],
							['skipstype', 'Type'],
							['tonnasje', 'Tonnasje (Tonnage): '],
							
						]



						#import pdb; pdb.set_trace()
						for entry in findText:
							my_attribute = getattr(obj, entry[0])
							
							if my_attribute != None:
							    my_attribute = my_attribute.strip() 
							if my_attribute == " ":
								my_attribute = ""
							
							if   getattr(obj, entry[0]) != my_attribute:
								setattr(obj, entry[0], my_attribute)
							
							
						modified(obj)
						if ant % 100 == 1:
							print('transaction')
							transaction.commit()
						#modified(obj)


  
	print(ant)
	transaction.commit()

