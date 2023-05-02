#python 3
#bin/instance run  name.py

from zope.lifecycleevent import modified
import plone.api
from zope.component.hooks import setSite
from plone.app.textfield import RichText
from plone.app.textfield.value import RichTextValue
from plone.rfc822.interfaces import IPrimaryFieldInfo
from plone import api

#Dont need all these
from plone.uuid.interfaces import IUUID
from zope.intid.interfaces import IIntIds
from Products.CMFCore.utils import getToolByName
from z3c.relationfield import RelationValue
from zope.interface import Interface
from zope import component
from zope.intid import IntIds
from zope.intid.interfaces import IIntIds
from zope.component import getUtility
from zExceptions import NotFound
from zope.lifecycleevent import modified
import transaction
from bs4 import BeautifulSoup

#Replace 'skipshistorie' with your own site name
setSite(app['skipshistorie'])
brains = app.skipshistorie.portal_catalog(portal_type="Document", sort_on="modified", sort_order='ascending')
#Test sith one doucment
#brains = app.skipshistorie.portal_catalog(id="brg54900000100000-skipsliste")

portal = api.portal.get()

ant = 0
#initids = getUtility(IIntIds)
if brains:
	print('Total  objects counted: ')
	print(len(brains))


	#for index, brain in enumerate(brains):
	for brain in  brains:
		obj = None
		obj = brain.getObject()
		#if index % 1000 == 1:
		#	print(index)


		tekst = obj.text
		if tekst != None:
			oldtext = tekst.raw
		else:
			continue

		soup = BeautifulSoup(oldtext, 'html.parser')

		try:


			for reflink in soup.find_all('a'):

				ref = reflink['href']

				if ref and 'file' in ref:
					#import pdb; pdb.set_trace()
					folder_parts = ref.split("/")
					index = None
					if 'skipshistorie' in folder_parts:
						indeks  = folder_parts.index('skipshistorie')

					if indeks:
						folder_path = '/' + '/'.join(folder_parts[(indeks-1):])

					found_items = None
					try:
						#import pdb; pdb.set_trace()
						found_items = plone.api.content.find(id=id)
						#import pdb; pdb.set_trace()
						print('found it')
						abc =123

					#probably dont need all these
					except AttributeError:
						found_items = None
					except NotFound:
						found_items = None
					except IndexError:
						found_items = None


					if found_items and len(found_items==1):
						ref_uid = found_items[0].UID()
						new_url= "resolveuid/"  + str(ref_uid)
						reflink['href'] = new_url
						ant += 1
						if (ant % 1000 == 1):
							#print('transaction')
							transaction.commit()

				if ref and not 'resolveuid' in ref and not 'http' in ref and not 'file' in ref and not 'mailto' in ref:

					url =  ref.split("/")
					id = url[:-1]
					if id == []:
						id = ref
					#folder_path = folder_path.replace("../", "").replace("--", "-").replace("-.", ".").replace("..", ".")
					folder_path = folder_path.replace("../", "").replace("--", "-").replace("-.", "-").replace("..", ".")
					#folder_path = folder_path.replace("(", "").replace(")", "")
					id = id.replace("--", "-").replace("-.", ".")
					id =  id.replace("%C3%86", "251ca")
					id =  id.replace.replace("%C3%B8", "o")
					id = id.replace("--", "-").replace(".html", "")


					found_items = None
					try:
						#import pdb; pdb.set_trace()
						found_items = plone.api.content.find(id=id)
						#import pdb; pdb.set_trace()
						print('found it')
						abc =123

					#probably dont need all these
					except AttributeError:
						found_items = None
					except NotFound:
						found_items = None
					except IndexError:
						found_items = None


					if found_items and len(found_items==1):
						ref_uid = found_items[0].UID()
						new_url= "resolveuid/"  + ref_uid
						reflink['href'] = new_url
						ant += 1
						if (ant % 100 == 1):
							#print('transaction')
							transaction.commit()
					else:
						#print('---------------')
						print('did not find: ')
						print(reflink)
						#print(obj.Title())
						#print(folder_path)





		except TypeError:
			#import pdb; pdb.set_trace()
			#transaction.commit()
			print('type error')
			print(reflink)
			abc = 123

		except KeyError as ke:
			#a without hfref, mostly 'bad html' skip these
			#print(ke)
			#abc = 123
			#print('key error')
			#print(reflink)
			abc = 1


		except AttributeError:
			print('attribute eror')

			#print(brain.getPath())
			print(id)
			#import pdb; pdb.set_trace()
			aaa = 1


		obj.text = RichTextValue(str(soup))
		#Probably
		#modified(obj)



transaction.commit()

print(ant)
