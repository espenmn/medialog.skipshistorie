#python 3
#bin/instance stop; bin/instance run  change_titlec.py  -O skipshistorie

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


from inspect import currentframe, getframeinfo

#frameinfo = getframeinfo(currentframe())
cf = currentframe()



setSite(app['skipshistorie'])

brains = app.skipshistorie.portal_catalog(sort_on="modified", sort_order="ascending")
#brains = app.skipshistorie.portal_catalog(Title=".htm")
#brains = app.skipshistorie.portal_catalog(portal_type="Image")
#brains = app.skipshistorie.portal_catalog(id="brg554oairgens")



#if brains:
try:
	print('Total  objects counted: ')
	print(len(brains))

	ant = 0
	xxx = 0
	for brain in  brains:
		obj = None
		id = brain.id
		if id.endswith("-1") or id.endswith("-2"):
			#import pdb;pdb.set_trace()
			obj = brain.getObject()
			newid = id.replace("-1", "").replace("-2", "")
			if len(newid) > 5:
				print(id)
				try:
					plone.api.content.rename(obj=obj, new_id=newid)
					transaction.commit()
				except KeyError as k:
					print(k)

		if brain.Title == "":
			try:
				# Use regular expressions to find the index of the last number in the string
				#removed
				#import pdb; pdb.set_trace()
				obj = brain.getObject()
				cut = obj.id.find('-')
				obj.setTitle(obj.id[cut+1:].title().replace("-", " "))
				#api.content.rename(obj=obj, new_id=ide)

			except  KeyError:
				print('key error')
				import pdb; pdb.set_trace()
				xxx = xxx + 1

			if (isinstance(brain.Title, str)):
				abc = 1
			else:
				abc=1
				print('else')
				#import pdb; pdb.set_trace()


	print(xxx)


	print(ant)
	transaction.commit()

except KeyError:
	#794065
	print('keyerror')
