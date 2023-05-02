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


#brains = app.skipshistorie.portal_catalog(id="dra439-sigurd-bruusgaard")

ant = 0

#if brains:
for brain in  brains:
    #print('-')
    try:
        obj = brain.getObject()
    except KeyError as ke:
        print('key error')
        #import pdb; pdb.set_trace()
        if not "osl" in brain.getPath():
            print('http://xweb14d.plana.dk:8980/' + brain.getPath())
        #print(ke)
        
    if brain.id != obj.id:
        ant+=1
        #brain.id = obj.id
        #transaction.commit()
        #import pdb; pdb.set_trace()
        
        
    if "osl317" in brain.id:
        print('oslo')
        #import pdb; pdb.set_trace()
        #obj = brain.getObject()
        #api.content.rename(obj=obj, new_id=brain.id)
        
print(ant)
    
            