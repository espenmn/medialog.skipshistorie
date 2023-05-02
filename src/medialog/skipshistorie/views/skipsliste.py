from Acquisition import aq_inner
from plone.app.dexterity import _
from plone.batching import Batch
from plone.registry.interfaces import IRegistry
from Products.Five import BrowserView
from zope.component import getMultiAdapter
from zope.component import getUtility
import plone.api


class FolderView(BrowserView):
    def __init__(self, context, request):
        super().__init__(context, request)

        self.plone_view = getMultiAdapter((context, request), name="plone")
        self.portal_state = getMultiAdapter(
            (context, request), name="plone_portal_state"
        )
        self.pas_member = getMultiAdapter((context, request), name="pas_member")


    def batch(self):
        batch = self.context.restrictedTraverse('@@contentlisting')(sort_on='sortable_title', batch=True, b_size=40);
        return batch

    def normalizeString(self, text):
        return self.plone_view.normalizeString(text)

    def toLocalizedTime(self, time, long_format=None, time_only=None):
        return self.plone_view.toLocalizedTime(time, long_format, time_only)

    @property
    def friendly_types(self):
        return self.portal_state.friendly_types()

    @property
    def isAnon(self):
        return self.portal_state.anonymous()

    @property
    def navigation_root_url(self):
        return self.portal_state.navigation_root_url()

    @property
    def use_view_action(self):
        registry = getUtility(IRegistry)
        return registry.get("plone.types_use_view_action_in_listings", [])


    @property
    def no_items_message(self):
        return _(
            "description_no_items_in_folder",
            default="There are currently no items in this folder.",
        )
