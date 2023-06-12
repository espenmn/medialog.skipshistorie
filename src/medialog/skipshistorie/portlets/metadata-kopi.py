# -*- coding: utf-8 -*-
from __future__ import absolute_import

from Acquisition import aq_inner
from medialog.skipshistorie import _
from plone import schema
from plone.app.portlets.navigation import Renderer as NavRenderer
from plone.app.portlets.portlets import base
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from z3c.form import field
from zope.component import getMultiAdapter
from zope.interface import implementer

import json


#import six.moves.urllib.request, six.moves.urllib.parse, six.moves.urllib.error
#import six.moves.urllib.request, six.moves.urllib.error, six.moves.urllib.parse



class Nenderer(NavRenderer):
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


class IMetadataPortlet(IPortletDataProvider):
    title = schema.TextLine(
       title=_(u'Portlet title'),
       required=True,
       default=u'Metadata'
     )


@implementer(IMetadataPortlet)
class Assignment(base.Assignment):
    schema = IMetadataPortlet

    @property
    def title(self):
        return _(u'Metadata')


class AddForm(base.AddForm):
    schema = IMetadataPortlet
    form_fields = field.Fields(IMetadataPortlet)
    label = _(u'Metadata portlet')
    description = _(u'This portlet displays metadata info')

    def create(self, something):
        return Assignment(
             enabled = True
    )


class EditForm(base.EditForm):
    schema = IMetadataPortlet
    form_fields = field.Fields(IMetadataPortlet)
    label = _(u'Change title')
    description = _(u'This portlet displays metadata info')


class MRenderer(base.Renderer):
    #schema = IMetadataPortlet
    _template = ViewPageTemplateFile('metadata.pt')

    def __init__(self, *args):
        base.Renderer.__init__(self, *args)
        context = aq_inner(self.context)
        portal_state = getMultiAdapter(
            (context, self.request),
            name=u'plone_portal_state'
        )
        self.anonymous = portal_state.anonymous()

    def render(self):
        return self._template()

    @property
    def available(self):
        """Show the portlet only if there are one or more elements and
        not an anonymous user."""
        return True
        #return not self.anonymous and self._data()

    def get_idold(self):
        return self.context.idold

    def get_idnew(self):
        return self.context.idnew

    def get_vessel(self):
        return self.context.vessel

    def get_skipstype(self):
        return self.context.skipstype

    def get_grt(self):
        return self.context.grt

    def get_tdw(self):
        return self.context.tdw

    def get_purch(self):
        return self.context.purch

    def get_del(self):
        return self.context.del_

    def get_shipyard(self):
        return self.context.shipyard

    def get_ex(self):
        return self.context.ex

    def get_yno(self):
        return self.context.yno

    def get_owneri(self):
        return self.context.owneri

    def get_senerenorsk(self):
        return self.context.senerenorsk

    def get_sold(self):
        return self.context.sold

    def get_to(self):
        return self.context.to
