#UTF-8
from plone.app.contenttypes.interfaces import IDocument
from plone.app.contenttypes.interfaces import IFolder
from plone.indexer import indexer
import plone.api


#from plone.indexer.decorator import indexer
#import six
#from plone.dexterity.utils import safe_unicode
#from plone.dexterity.utils import safe_utf8

@indexer(IDocument)
def idnewIndexer(self):
    return str(self.idnew)


@indexer(IDocument)
def off_nrIndexer(self):
    return str(self.off_nr)

@indexer(IDocument)
def konstruksjonIndexer(self):
    if self.portal_type=="skip":
        #import pdb; pdb.set_trace()
        return str(self.konstruksjon)



@indexer(IFolder)
def antallIndexer(self):
    if self.portal_type=="rederi":
        antall  = len(plone.api.content.find(self, portal_type="skip"))
        self.antall = antall
        return antall
    if self.portal_type=="Folder":
        self = self.aq_parent
        antall  = len(plone.api.content.find(self, portal_type="skip"))
        self.antall = antall
        return antall
    else:
        return None

@indexer(IFolder)
def tilIndexer(self):
    if self.portal_type=="rederi":
        antall  = len(plone.api.content.find(self, portal_type="skip"))
        self.til = tuple(range(1, antall))
        return self.til
    if self.portal_type=="Folder":
        self = self.aq_parent
        antall  = len(plone.api.content.find(self, portal_type="skip"))
        self.til = tuple(range(1, antall))
        return self.til
    else:
        return None
