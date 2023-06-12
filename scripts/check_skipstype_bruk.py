#python 3
#from plone.indexer import indexer


from zope.component.hooks import setSite
from zope.lifecycleevent import modified
import transaction
from plone import api

from plone.app.uuid.utils import uuidToObject


setSite(app['skipshistorie'])



brains = app.skipshistorie.portal_catalog(portal_type=["skip"], sort_on="modified", sort_order='descending')
#brains = app.skipshistorie.portal_catalog(id= "dur90919590100000-a-e-larsen")


a = 0

#if brains:
for brain in  brains:
    #print('-')
    #import pdb; pdb.set_trace()
    a +=1
    obj = brain.getObject()
    skipstype = obj.skipstype__bruk_
    if skipstype == '':
        obj.skipstype__bruk_ = None
        modified(obj)
    konstruksjon = obj.konstruksjon
    if konstruksjon == '':
        obj.konstruksjon = None
        modified(obj)
    havn = obj.havn
    if havn == '':
        obj.havn = None
        modified(obj)
    flagg = obj.flagg
    if flagg == '':
        obj.flagg = None
        modified(obj)

    if a % 400 == 1:
        transaction.commit()
        print('kommit')

transaction.commit()
