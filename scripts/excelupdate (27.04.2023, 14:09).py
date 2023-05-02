#python 3

import pandas as pd
import openpyxl
from zope.lifecycleevent import modified
import plone.api
from zope.component.hooks import setSite
import transaction

setSite(app['skipshistorie'])
excelfile = '/Users/rolf/Desktop/xxxl.xlsx'

from pandas import *

df = pd.read_excel('xxxl.xlsx')
print(df)

my_dict = df.to_dict(orient='index')

def add_metadata(brain):
    obj = brain.getObject()
    for key, value in my_dict[i].items():
        #print(key)
        if key=='skipstype':
            key = 'skipstype_d'
        if key=='signal':
            key = 'kallesignal'

        if key=='type':
            key = 'skipstype'
        if key=='del':
            key = 'del_'


        if value and str(value).lower() != 'nan':
            setattr(obj, key.lower().replace(" ", ""), value)
        else:
            #import pdb; import pdb; pdb.set_trace()
            setattr(obj, key.lower().replace(" ", ""), None)


#Main script here
# Iterate the loop to read the cell values
#in case we just want to rerun some
for i in range(0, len(my_dict)):
    old_id = my_dict[i].get('ID old')
    plone_titel = my_dict[i].get('vessel').replace(" ", "-")
    plone_id = str(old_id) + '00000-' + plone_titel
    plone_id = plone_id.lower().replace("ø", "o")
    plone_id = plone_id.lower().replace("å", "a")

    brains = app.skipshistorie.portal_catalog(id=plone_id)

    if brains:
        add_metadata(brains[0])
    else:
        brains = app.skipshistorie.portal_catalog(portal_type="Document")
        #import pdb; pdb.set_trace()

        found = 0
        if brains:
            for brain in brains:
                #print(brain.id)
                if brain.id.startswith(old_id):
                    found = 1
                    add_metadata(brain)
            if found == 0:
                print('Not found: ' + old_id + ' ' + plone_titel)
        transaction.commit()
