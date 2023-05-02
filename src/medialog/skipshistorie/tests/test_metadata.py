# -*- coding: utf-8 -*-
from medialog.skipshistorie.testing import MEDIALOG_SKIPSHISTORIE_FUNCTIONAL_TESTING
from medialog.skipshistorie.testing import MEDIALOG_SKIPSHISTORIE_INTEGRATION_TESTING
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.portlets.interfaces import IPortletType
from zope.component import getUtility

import unittest


class PortletIntegrationTest(unittest.TestCase):

    layer = MEDIALOG_SKIPSHISTORIE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.app = self.layer['app']
        self.request = self.app.REQUEST
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_metadata_is_registered(self):
        portlet = getUtility(
            IPortletType,
            name='medialog.skipshistorie.portlets.Metadata',
        )
        self.assertEqual(portlet.addview, 'medialog.skipshistorie.portlets.Metadata')


class PortletFunctionalTest(unittest.TestCase):

    layer = MEDIALOG_SKIPSHISTORIE_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
