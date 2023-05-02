#python 3

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


setSite(app['skipshistorie'])

brains = app.skipshistorie.portal_catalog(portal_type="Folder")
    #import pdb; pdb.set_trace()

if brains:
    print('Total  objects: ')
    print(len(brains))
    ant = 0
    for brain in brains:
        ant+=1
        obj = brain.getObject()
        
        if obj.id.lower().startswith("barber"):
        	import pdb; pdb.set_trace() 
        	
        if brain.id.lower().startswith("barber"):
        	import pdb; pdb.set_trace() 

        if ' '  in obj.id:
             print(id)

             obj.id = obj.id.replace(' ', '-')
             print(obj.id)
             modified(obj)





        #import pdb; pdb.set_trace()
        if '%20' in obj.id:
            id = obj.id
            print(id)
            obj.id = id.replace('%20', '-')
            modified(obj)

        if '%20' in obj.absolute_url():
            #id = obj.id
            print(id)
            #obj.id = id.replace('%20', '-')


    transaction.commit()