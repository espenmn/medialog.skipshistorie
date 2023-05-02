# -*- coding: utf-8 -*-
from __future__ import absolute_import

#from Acquisition import aq_inner
from medialog.skipshistorie import _
from plone import schema
from plone.app.portlets.portlets import base
from plone.app.portlets.portlets.navigation import Assignment
from plone.app.portlets.portlets.navigation import INavigationPortlet
from plone.app.portlets.portlets.navigation import Renderer as NavRenderer
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
#from z3c.form import field
#from zope.component import getMultiAdapter
from zope.interface import implementer
from zope.interface import Interface


#import json
#import six.moves.urllib.request, six.moves.urllib.parse, six.moves.urllib.error
#import six.moves.urllib.request, six.moves.urllib.error, six.moves.urllib.parse



class IMedialogNavigationPortlet(INavigationPortlet):
    """A portlet"""

class NRenderer(NavRenderer):
   @property
   def available(self):
       if self.context.idnew:
           return False
       rootpath = self.getNavRootPath()
       if rootpath is None:
           return False

       if self.data.bottomLevel < 0:
           return True

       tree = self.getNavTree()
       return len(tree["children"]) > 0


class NAssignment(Assignment):
    @property
    def title(self):
        """
        Display the name in portlet mngmt interface
        """
        return _("innhold")



class IMetadataPortlet(IPortletDataProvider):
    """A portlet to show metadata"""


@implementer(IMetadataPortlet)
class Assignment(base.Assignment):
    title = _("label_metadata", default="Teknisk info")


class AddForm(base.NullAddForm):
    def create(self):
        return Assignment()


class MRenderer(base.Renderer):
    _template = ViewPageTemplateFile('metadata.pt')


    def __init__(self, *args):
        base.Renderer.__init__(self, *args)
    #    context = aq_inner(self.context)

    def show(self):
        if hasattr(self.context, 'vessel') and self.context.vessel != None and self.context.vessel != '':
            return True
        if hasattr(self.context, 'eier') and self.context.eier != None and self.context.eier != '':
            return True
        else:
            return False

    def render(self):
        return self._template()

    @property
    def available(self):
        if hasattr(self.context, 'vessel') and self.context.vessel != None and self.context.vessel != '':
            return True
        if hasattr(self.context, 'eier') and self.context.eier != None and self.context.eier != '':
            return True
        else:
            return False
