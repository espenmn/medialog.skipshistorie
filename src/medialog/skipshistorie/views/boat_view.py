# -*- coding: utf-8 -*-

# from medialog.skipshistorie import _
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface


# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class IBoatView(Interface):
    """ Marker Interface for IBoatView"""


@implementer(IBoatView)
class BoatView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('boat_view.pt')

    def __call__(self):
        # Implement your own actions:
        return self.index()
