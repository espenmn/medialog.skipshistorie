#python 3

import pandas as pd
import openpyxl
from zope.lifecycleevent import modified
import plone.api
from zope.component.hooks import setSite
import transaction

setSite(app['skipshistorie'])
excelfile = '27april.xlsx'

from pandas import *

df = pd.read_excel('27april.xlsx')
print(df)

my_dict = df.to_dict(orient='index')

def add_metadata(brain):
    obj = brain.getObject()
    skipsnavn = []
    for key, value in my_dict[i].items():

        #print(key)
        if key=='skipstype':
            key = 'skipstype__bruk_'
        if key=='signal':
            key = 'kallesignal'

        if key=='type':
            key = 'skipstype'
        if key=='del':
            key = 'del_'
        if key=='kjøp':
            key = 'kjop'
        if key=='årsak':
            key = 'arsak'

        key = key.lower().replace(" ", "")
        if value == ' ':
            value = ''


        #import pdb; pdb.set_trace()
        if obj.id == 'brg22118840200000-amicitia':
            import pdb; pdb.set_trace()
        if value and str(value).lower() != 'nan' and not "skipsnavn" in key:
            #import pdb; pdb.set_trace()
            field_type = type(getattr(obj, key))
            print(key);
            print(field_type)
            print(value)
            print("----------")
            if key in ["tdw", ""]:
                setattr(obj, key, int(float(value)))
            elif key in ["grt", "brt", "nrt",  "tilgang"]:
                #import pdb; pdb.set_trace()
                setattr(obj, key, int(float(value)))
            else:
                #import pdb; pdb.set_trace()
                if isinstance(value, float):
                    value=int(value)
                setattr(obj, key, str(value))
        else:
            #import pdb; import pdb; pdb.set_trace()
            #setattr(obj, key, None)
            if "skipsnavn" in key and str(value).lower() != 'nan':
                skipsnavn.append(str(value))
    if skipsnavn:
        setattr(obj, "skipsnavn", ", ".join(skipsnavn) )

    #import pdb; pdb.set_trace()
    #if obj.bnr and obj.bnr != None and obj.bnr != 'None':
    #    if obj.bnr == '':
    #        setattr(obj, "bnr", None )
    #    else:
    #        print(obj.bnr)
    #        setattr(obj, "bnr", int(obj.bnr) )



#Main script here
# Iterate the loop to read the cell values
#in case we just want to rerun some
for i in range(0, len(my_dict)):
    old_id = my_dict[i].get('ID old')
    if old_id:
        #plone_titel = my_dict[i].get('vessel').replace(" ", "-")
        plone_id = str(old_id)
        #+ '00000-' + plone_titel
        #plone_id = plone_id.lower().replace("ø", "o")
        #plone_id = plone_id.lower().replace("å", "a")

        #brains = app.skipshistorie.portal_catalog(id=plone_id)
        brains = app.skipshistorie.portal_catalog(vessel=plone_id)


        if brains and len(brains)==1:

            add_metadata(brains[0])
            transaction.commit()
        else:
            #brains = app.skipshistorie.portal_catalog(portal_type="Document")
            #import pdb; pdb.set_trace()
            print('did not find')
            print(old_id)

            found = 0
            #if brains:
            #    for brain in brains:
                    #print(brain.id)
            #        if brain.id.startswith(old_id):
            #            found = 1
            #            add_metadata(brain)
            #    if found == 0:
            #        print('Not found: ' + old_id + ' ' + plone_titel)
