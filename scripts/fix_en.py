#python 3
#from plone.indexer import indexer


from zope.component.hooks import setSite
from zope.lifecycleevent import modified
import transaction
from plone import api


setSite(app['skipshistorie'])


print("ready!")

#brains = app.skipshistorie.portal_catalog(portal_type=["Image", "File", "Document"])
brains = app.skipshistorie.portal_catalog(id="klipp-fra-gamle-dager")

brains = app.skipshistorie.portal_catalog()


if brains:
    print('Total  objects: ')
    print(len(brains))
    ant = 0
    for brain in  reversed(brains):
        if  "." in brain.id:
            print(brain.id)
            try:
                #import pdb; pdb.set_trace()
                obj = brain.getObject()
            
                
                print(obj.id)
                ide = obj.id.replace(" ", "-").lower()
                ide = ide.replace('.', '-' )
                api.content.rename(obj=obj, new_id=ide)
                modified(obj)
                transaction.commit()
                print(obj.id)
                a =  1
            except KeyError:
                a = 1
                
