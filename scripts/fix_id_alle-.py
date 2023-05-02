#python 3
#from plone.indexer import indexer


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
        if '..' in obj.id:
        	print(obj.id)
        if '-.' in obj.id:
        	print(obj.id)
        
        ide = obj.id.replace('-.', '.')
        ide = ide.replace('..', '.')
        api.content.rename(obj=obj, new_id=ide)
        modified(obj)
 

transaction.commit()

print(ant)
