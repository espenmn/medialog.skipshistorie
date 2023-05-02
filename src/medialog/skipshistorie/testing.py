# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import medialog.skipshistorie


class MedialogSkipshistorieLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=medialog.skipshistorie)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'medialog.skipshistorie:default')


MEDIALOG_SKIPSHISTORIE_FIXTURE = MedialogSkipshistorieLayer()


MEDIALOG_SKIPSHISTORIE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(MEDIALOG_SKIPSHISTORIE_FIXTURE,),
    name='MedialogSkipshistorieLayer:IntegrationTesting',
)


MEDIALOG_SKIPSHISTORIE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(MEDIALOG_SKIPSHISTORIE_FIXTURE,),
    name='MedialogSkipshistorieLayer:FunctionalTesting',
)


MEDIALOG_SKIPSHISTORIE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        MEDIALOG_SKIPSHISTORIE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='MedialogSkipshistorieLayer:AcceptanceTesting',
)
