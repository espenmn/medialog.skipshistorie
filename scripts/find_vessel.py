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

folders = app.skipshistorie.portal_catalog(portal_type="Folder", sort_on="modified", sort_order='ascending')

for folder in folders:


	#import pdb; pdb.set_trace()

	rederinummer = folder.getObject().rederinummer

	if rederinummer:

		brains = plone.api.content.find(context=folder.getObject(), portal_type="Document")
		if brains:
			ant = 0

			for brain in brains:
				obj = brain.getObject()
				if not obj.vessel:
					primary_field = IPrimaryFieldInfo(obj)
					if isinstance(primary_field.field, RichText):
						if obj.text:
							oldtext = obj.text.raw
							soup = BeautifulSoup(oldtext, 'html.parser')

							#import pdb; pdb.set_trace()
							#look_for = '(' + rederinummer

							for elem in soup(text=re.compile(r'\(' + rederinummer)):
								#import pdb; pdb.set_trace()
								words = elem.strip().split(' ')
								#tittel = words[1] + ' '.join(words[2:-2]).title().replace("  ", " ")
								#obj.setTititle(tittel)
								#tittel = tittel.replace(" ", "")
								#obj.year = int(words[0])
								obj.vessel = words[-1].replace("(", "").replace(")", "")
								#import pdb; pdb.set_trace()
								print(obj.vessel)
								#text_element = elem.find_parent('tr')
								#text_element['class'] = 'scraped'



								obj.text = RichTextValue(str(soup))
								ant = ant + 1
								modified(obj)
								if ant % 100 == 1:
									print('transaction')
									transaction.commit()

							#transaction.commit()
							#modified(obj)


transaction.commit()
