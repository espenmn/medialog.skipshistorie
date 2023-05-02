#python 3
#from plone.indexer import indexer


from zope.component.hooks import setSite
from zope.lifecycleevent import modified
import transaction
from plone import api

from plone.app.uuid.utils import uuidToObject


setSite(app['skipshistorie'])


print("ready!!!")

#brains = app.skipshistorie.portal_catalog(portal_type=["Image", "File", "Document"])
#brains = app.skipshistorie.portal_catalog(portal_type=["Folder"])
#brains = app.skipshistorie.portal_catalog()
#brains = app.skipshistorie.portal_catalog(id="osl436onstad shipping")
brains = app.skipshistorie.portal_catalog()

ant = 0

if brains:
    try:
    	#if ant == 0:
        print('trying')

        for brain in reversed(brains):
            #import pdb; pdb.set_trace()

            try:
                uuid = brain.UID
                obj = uuidToObject(uuid)
                ide = brain.id.replace(' ', '-')
                ide = ide.replace('zzz', '-')
                #brain.id = ide
                #ide = ide.replace(' ', '-')
                #ide = ide.replace(' ', '-')
                #ide = ide.replace(' ', '-')
                #ide = ide.replace(' ', '-')
                #ide = brain.id.replace('yyy', '-').replace('xxx', '')
                if ' ' in brain.id:
                    #obj = brain.getObject()
                    #print(ide)
                    obj = brain.getObject()
                    obj.id = ide.replace(' ', '-')
                    brain.id = ide.replace(' ', '-')
                    #api.content.rename(obj=obj, new_id=ide.replace('-', 'zzz'), safe_id=True)
                    api.content.rename(obj=obj, new_id=ide.strip(), safe_id=True)
                    #obj.reindexObject()
                    print('reindex')
            except KeyError:
                #import pdb; pdb.set_trace()
                print("Key error")
                print(brain.id)
                ant+=1
            except ValueError:
                #import pdb; pdb.set_trace()
                print("value error")
                print(brain.id)
                ant+=1

    except ValueError:
	    print("value error:")
	    print(brain.Title)
    except KeyError:
        print("Key error:")
        print(brain.id)

    transaction.commit()

print(ant)
