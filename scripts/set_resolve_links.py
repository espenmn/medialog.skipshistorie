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

#initids = getUtility(IIntIds)
if brains:
	print('Total  objects counted: ')
	print(len(brains))

	ant = 0
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
				folder_path = None

				if ref:
					ref = ref.replace("../", "").replace("--", "-").replace("-.", "-").replace("..", ".")
					ref = ref.replace("(", "").replace(")", "")
					ref = ref.replace("---", "-").replace("-.", ".").replace("--", "-")
					ref = ref.replace("%C3%86", "251ca")
					ref = ref.replace("%C3%B8", "o")

					ref = ref.replace("%C3%B8", "251cy")
					ref = ref.replace("%C3%98", "o")
					ref = ref.replace("%C3%86", "251")
					ref = ref.replace("Ö", "2560")
					ref = ref.replace("%C3%96", "2560")
					ref = ref.replace("http://nohost", "")
					ref = ref.replace("tekster/bilder", "bilder")
					ref = ref.replace("%C3%86", "251ca").replace("yekster", "tekster")
					ref = ref.replace.replace("%C3%B8", "o").replace("htm", "")

				if ref and 'file' in ref:
					import pdb; pdb.set_trace()
					folder_parts = ref.split("/")
					index = None
					if 'skipshistorie' in folder_parts:
						indeks  = folder_parts.index('skipshistorie')

					if indeks:
						folder_path = '/' + '/'.join(folder_parts[indeks-1:])
						folder_path = folder_path.replace("/skipsdokumenter", "")

				if ref and not 'resolveuid' in ref and not 'http' in ref and not 'file' in ref and not 'mailto' in ref:
					#folder_path = '/'.join(obj.aq_parent.aq_parent.aq_parent.getPhysicalPath())
					import pdb; pdb.set_trace()
					url =  obj.absolute_url().split("/")
					folder_path = '/' +  '/'.join(url[3:-2]) + "/" + ref
					#folder_path = folder_path.replace("../", "").replace("--", "-").replace("-.", ".").replace("..", ".")
					folder_path = folder_path.replace("../", "").replace("--", "-").replace("-.", "-").replace("..", ".")
					folder_path = folder_path.replace("(", "").replace(")", "")
					folder_path = folder_path.replace("---", "-").replace("-.", ".").replace("--", "-")
					folder_path = folder_path.replace("%C3%86", "251ca")
					folder_path = folder_path.replace("%C3%B8", "o")

					folder_path = folder_path.replace("%C3%B8", "251cy")
					folder_path = folder_path.replace("%C3%98", "o")
					folder_path = folder_path.replace("%C3%86", "251")
					folder_path = folder_path.replace("Ö", "2560")
					folder_path = folder_path.replace("%C3%96", "2560")
					folder_path = folder_path.replace("http://nohost", "")
					folder_path = folder_path.replace("tekster/bilder", "bilder")
					folder_path = folder_path.replace("%C3%86", "251ca").replace("yekster", "tekster")
					folder_path = folder_path.replace.replace("%C3%B8", "o").replace("htm", "")
					#folder_path = folder_path.replace("(", "")
					#folder_path = folder_path.replace(")", "")
					#folder_path = folder_path.replce("/tekster/bilder", "/bilder")
					#folder_path = folder_path.replace("../", "../")

				found_items = None
				try:
					#import pdb; pdb.set_trace()
					if folder_path:

						found_items = plone.api.content.get(path=folder_path)
						print('found it')



				except AttributeError:
						found_items = None
				except NotFound:
						found_items = None
				except IndexError:
						found_items = None

				if not found_items:
						try:
							if folder_path:
								folder_path = obj.aq_parent.absolute_url() + "/" + ref
								found_items = plone.api.content.get(path=folder_path)


						#probably dont need all these
						except AttributeError:
							found_items = None
						except NotFound:
							found_items = None
						except IndexError:
							found_items = None

				if not found_items:
						try:
							if folder_path:
								folder_path =  "/skipshistorie/" + ref
								found_items = plone.api.content.get(path=folder_path)


						#probably dont need all these
						except AttributeError:
							found_items = None
						except NotFound:
							found_items = None
						except IndexError:
							found_items = None

				if not found_items:
						try:
							if folder_path:
								folder_path = obj.aq_parent.aq_parent.absolute_url() + "/" + ref
								found_items = plone.api.content.get(path=folder_path)


						#probably dont need all these
						except AttributeError:
							found_items = None
						except NotFound:
							found_items = None
						except IndexError:
							found_items = None

				if found_items:
						ref_uid = found_items.UID
						new_url= "resolveuid/"  + str(ref_uid)
						reflink['href'] = new_url
						ant += 1
						if (ant % 1000 == 1):
							#print('transaction')
							transaction.commit()
				else:
						#print('---------------')
						print('did not find: ')
						print(folder_path)
						#print(obj.Title())
						#print(folder_path)





		except TypeError:
			import pdb; pdb.set_trace()
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


		except AttributeError as at:
			print(at)
			print('attribute eror')

			print(ref)
			import pdb; pdb.set_trace()
			aaa = 1


		obj.text = RichTextValue(str(soup))
		#Probably
		#modified(obj)



transaction.commit()

#print(ant)
