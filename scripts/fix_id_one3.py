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

#if brains:
for brain in  brains:
    #print('-')
    if "dra439" in brain.id:
        import pdb; pdb.set_trace()
        print('one')
        if "sigurd" in brain.id:
            print('two')
            if "bruusgaard" in brain.id:
                import pdb; pdb.set_trace()
                print('ost')
    