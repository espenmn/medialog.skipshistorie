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

brains = app.skipshistorie.portal_catalog()
    #import pdb; pdb.set_trace()

if brains:
    print('Total  objects: ')
    print(len(brains))
    ant = 0
    for brain in brains:
        ant+=1

        if ' '  in brain.id:
             id = brain.id
             print(id)
             obj = brain.getObject()
             obj.id = obj.id.replace(' ', '-')
             print(obj.id)
             modified(obj)





        #import pdb; pdb.set_trace()
        if '%20' in brain.id:
            id = brain.id
            print(id)
            brain.id = id.replace('%20', '-')

        if '%20' in brain.absolute_url():
            #id = brain.id
            print(id)
            #brain.id = id.replace('%20', '-')


    transaction.commit()