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

#if brains:
for brain in  brains:
    try:
        uuid = brain.UID
        obj = uuidToObject(uuid)
        #.replace('', ' ')
        if ' ' in brain.id:
            obj = brain.getObject()
            ide = obj.id.replace(' ', '-')
            ide = ide.replace('-', ' ')
            s = ide
        
            for i in range(len(s)):
                if s[i] == ' ':
                    abc=1
                    try:
                        ide = (s[:i] + '-' + s[i+1:])
                        brain.id = ide
                        obj.id = ide
                        api.content.rename(obj=obj, new_id=ide)
                        #obj.reindexObject()
                    except ValueError:
                        #import pdb; pdb.set_trace()
                        #print('http://xweb14d.plana.dk:8980/' + brain.getPath().replace(' ', '%20'))
                        abc=1
                    except KeyError:
                        print('key error  1 -----------------')
                        #import pdb; pdb.set_trace()
                        #print('http://xweb14d.plana.dk:8980/' + brain.getPath().replace(' ', '%20'))
                        
                    except TypeError:
                        print('type error 1')
                        #import pdb; pdb.set_trace()
                        #print('http://xweb14d.plana.dk:8980/' + brain.getPath().replace(' ', '%20'))
                        
                    finally:
                        #import pdb; pdb.set_trace()
                        print('finally 1')
                        #print('http://xweb14d.plana.dk:8980/' + brain.getPath().replace(' ', '%20'))
                        
                        #nothing
                        
    except ValueError:
        abc=1
        print('value error 2')
        
    except KeyError as e:
        #import pdb; pdb.set_trace()
        #brain.id = ide
        #obj.id = ide
        ant+=1
        #api.content.rename(obj=obj, new_id=ide, safe_id=True)
        #obj.id= brain.id
        brain.id=obj.id
        #nid = brain.id + '___'
        obj.items = []
        obj.aq_parent.items = []
        newid = brain.id.replace('-1', '')
        api.content.rename(obj=obj, new_id=newid)
        obj.reindexObject()
        obj.aq_parent.reindexObject()
        transaction.commit()
        print(e)
        print('key error 2')
        api.content.rename(obj=obj, new_id=newid.replace(' ', '-'))
        #import pdb; pdb.set_trace()
                        
    except TypeError:
        abc=1
        print('type error 2')
        
    

transaction.commit()

print(ant)
