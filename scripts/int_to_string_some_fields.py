#python 3

import pandas as pd
import openpyxl
from zope.lifecycleevent import modified
import plone.api
from zope.component.hooks import setSite
import transaction

setSite(app['skipshistorie'])



brains = app.skipshistorie.portal_catalog(portal_type=["Document", "skip"], sort_on="modified", sort_order='descending')

myList = [
'fangstutstyr',
'bemanning',
'bnr',
'byggeaar',
'dekkmaskineri',
'dimensjoner',
'disponent',
'eier',
'fart',
'flagg',
'fremdrift',
'havn',
'historikk',
'history',
'hjelpemaskineri',
'kallesignal',
'kjeler',
'kjolemaskineri',
'klasse',
'kommunikasjon',
'lasthandtering',
'manouvering',
'navigasjonsutstyr',
'off_nr',
'power',
'shipyard',
'skipstype',
'tonnasje',
'eier',
'skipstype',
'flagg',
'havn',
]



for brain in brains:
    obj = brain.getObject()
    skipsnavn = []
    #import pdb; pdb.set_trace()
    for key in myList:
        try:
            value = getattr(obj, key)
            if key  == "tdw":
                setattr(obj, key, int(float(value)))
            elif key in ["grt", "brt", "nrt",  "tilgang"]:
                #import pdb; pdb.set_trace()
                setattr(obj, key, int(float(value)))
            else:
                #import pdb; pdb.set_trace()
                if isinstance(value, float):
                    value=int(value)
                    setattr(obj, key, str(value))
        except AttributeError:
            print(obj)
    modified(obj)

transaction.commit()
