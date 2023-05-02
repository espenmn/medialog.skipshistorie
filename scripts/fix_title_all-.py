#python 3
#from plone.indexer import indexer
#sudo bin/instance run fix_title_all-.py

from zope.component.hooks import setSite
from zope.lifecycleevent import modified
import transaction
from plone import api

from plone.app.uuid.utils import uuidToObject


setSite(app['skipshistorie'])


print("ready!!!")
brains = app.skipshistorie.portal_catalog()

ant = 0

print(len(brains))
#if brains:
for brain in  brains:
    	#try:
        obj = brain.getObject()
        if '..' in obj.Title() or '-.' in obj.Title() or '-1' in obj.Title():
        	print(obj.Title())
        
        	ide = obj.Title().replace('-.', '.')
        	ide = ide.replace('..', '.')
        	ide = ide.replace('-1', '')
        	obj.setTitle(ide)
        	modified(obj)
 

transaction.commit()

print(ant)
