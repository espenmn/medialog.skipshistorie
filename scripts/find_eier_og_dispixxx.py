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
#brains = app.skipshistorie.portal_catalog(id="osl48219450100000-finnes")

     #import pdb; pdb.set_trace()

if brains:
     print('Total  objects: ')
     print(len(brains))
     ant = 0
     for brain in  brains:
         obj = brain.getObject()
         print(obj.Title)
         try:
             if '- ' in obj.Title:
                  import pdb; pdb.set_trace()
         except TypeError: 
             #import pdb; pdb.set_trace()
             obj.Title = obj.Title()
         primary_field = IPrimaryFieldInfo(obj)
         if isinstance(primary_field.field, RichText):
                 if obj.text:
                     oldtext = obj.text.raw
                     soup = BeautifulSoup(oldtext, 'html.parser')


                     findText = [
                         ['eier', ' Eier (owner):'],
                         ['eier', 'Eier (owner):'],
                         ['eier', 'Eier (owner): '],
                         ['disponent', 'Disponent (manager):'],
                         ['disponent', ' Disponent (manager):'],
                         ['disponent', ' Disponent (manager): '],
                         ['bnr', ' Bnr (Sno).:'],
                         ['bnr', 'Bnr (Sno).:'],
                         ['bnr', 'Bnr (Sno).: '],
                         ['byggeaar', ' Byggeår (year built):'],
                         ['byggeaar', 'Byggeår (year built):'],
                         ['byggeaar', 'Byggeår (year built): '],
                         ['byggear', ' Bygge&aring;r (year built):'],
                         ['klasse', 'Klasse (Class).:'],
                         ['klasse', ' Klasse (Class).:'],
                         ['klasse', ' Klasse (Class).: '],
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
                         ['off_nr', 'Off.no: '],
                         ['off_nr', ' Off.no:'],
                         ['off_nr', ' Off.no: '],
                         ['off_nr', 'Off.no:'],

                     ]

                     for entry in findText:
                         #import pdb; pdb.set_trace()
                         findField = soup.find(text=entry[1])

                         if findField:
                             try:
                                value = findField.find_parent('td').find_next('td').text
                                if len(value) >= 3:
                                    #import pdb; pdb.set_trace()
                                    setattr(obj, entry[0], value)


                             except AttributeError:
                                 #import pdb; pdb.set_trace()
                                 print(obj.Title)
                             except ValueError:
                                 #import pdb; pdb.set_trace()
                                 print(obj.Title)


                     ##move transaction to end of loop
     print(ant)
     transaction.commit()
