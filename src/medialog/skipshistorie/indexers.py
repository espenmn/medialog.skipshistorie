#UTF-8
from plone.app.contenttypes.interfaces import IDocument
from plone.indexer import indexer


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
