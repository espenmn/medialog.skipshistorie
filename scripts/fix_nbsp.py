#python 3
#bin/instance stop; bin/instance run  change_titlec.py  -O skipshistorie
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



#brains = app.skipshistorie.portal_catalog(portal_type="Image")
brains = app.skipshistorie.portal_catalog(portal_type="skip")
#brains = app.skipshistorie.portal_catalog(id="kristiansundsrederier")
#brains = brg54419170320001-karen.jpg


#import pdb; pdb.set_trace()
if brains:
	print('Total  objects counted: ')
	print(len(brains))

	ant = 0
	xxx = 0
	for brain in  brains:
			obj = None
			obj = brain.getObject()

			#primary_field = IPrimaryFieldInfo(obj)
			#if isinstance(primary_field.field, RichText):
			if obj.text:
				primary_field = IPrimaryFieldInfo(obj)
				if isinstance(primary_field.field, RichText):
					oldtext = obj.text.output
					oldtext = oldtext.replace('-nbsp;', '&nbsp;')

					obj.text = RichTextValue(oldtext)
					modified(obj)





	print(ant)
	transaction.commit()
