#python 3
#from plone.indexer import indexer


from zope.component.hooks import setSite
from zope.lifecycleevent import modified
import transaction
from plone import api


setSite(app['skipshistorie'])


print("ready")

#brains = app.skipshistorie.portal_catalog(portal_type=["Image", "File", "Document"])
brains = app.skipshistorie.portal_catalog()
#brains = app.skipshistorie.portal_catalog(id="osl436onstad shipping")


if brains:
    print('Total  objects: ')
    print(len(brains))
    ant = 0
    for brain in reversed(brains):
        #print(brain.id)
        #import pdb; pdb.set_trace()
        #print('lets go')
        
        

        if ' '  in brain.id:
             ide = brain.id.replace(' ', '-')
             ide = ide.replace('-1', '')
             ide = ide.replace(' ', '-')
             ide = ide.replace(' ', '-')
             
             try:
             	obj = brain.getObject()
             	#print(brain.id) 
             	api.content.rename(obj=obj, new_id=ide)
             	#obj.reindexObject()
             except KeyError: 
             	print("Key error: " + brain.portal_type )
             	#obj.id = brain.id; 
             	#nid = brain.id + '-1';  
             	#api.content.rename(obj=obj, new_id=nid)
             	#import pdb; pdb.set_trace()
             	ant+=1
        
             except ValueError: 
             	print("value error" + brain.portal_type)
             	ant+=1
        
                #import pdb; pdb.set_trace()
                #api.content.rename(obj=brain.getObject, new_id=ide, safe_id=True)
             	
             	#obj.id = ide
             
             
            
             
             #tried all combinations of this
             #obj.reindexObject(idxs=['id'])
             #obj.reindexObject(idxs=['getId'])
             #obj.reindexObject()
             #obj.reindexObject(idxs=['modified'])
             #obj.reindexObject()
             #and this outside of loop (and also inside, just to be sure)
             #transaction.commit()

    transaction.commit()
    
print(ant)
             