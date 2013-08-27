# -*- coding: utf-8 -*-

from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing.z2 import ZSERVER_FIXTURE


class Fixture(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import ploneawards.contenttypes
        self.loadZCML(package=ploneawards.contenttypes)

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup
        self.applyProfile(portal, 'ploneawards.contenttypes:default')

FIXTURE = Fixture()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,),
    name='ploneawards.contenttypes:Integration',
)


FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE, ZSERVER_FIXTURE),
    name='ploneawards.contenttypes:Functional',
)
