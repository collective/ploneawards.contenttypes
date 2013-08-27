# -*- coding: utf-8 -*-

from ploneawards.contenttypes.nomination import INomination
from ploneawards.contenttypes.testing import INTEGRATION_TESTING
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest


class CoverIntegrationTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory(
            'ploneawards.contenttypes.nominationfolder', 'test-folder')
        setRoles(self.portal, TEST_USER_ID, ['Member'])
        self.folder = self.portal['test-folder']
        self.folder.invokeFactory(
            'ploneawards.contenttypes.nomination', 'n1',)
        self.n1 = self.folder['n1']

    def test_adding(self):
        self.assertTrue(INomination.providedBy(self.n1))

    def test_fti(self):
        fti = queryUtility(
            IDexterityFTI, name='ploneawards.contenttypes.nomination')
        self.assertIsNotNone(fti)

    def test_schema(self):
        fti = queryUtility(
            IDexterityFTI, name='ploneawards.contenttypes.nomination')
        schema = fti.lookupSchema()
        self.assertEqual(INomination, schema)

    def test_factory(self):
        fti = queryUtility(
            IDexterityFTI, name='ploneawards.contenttypes.nomination')
        factory = fti.factory
        new_object = createObject(factory)
        self.assertTrue(INomination.providedBy(new_object))

    def test_selectable_as_folder_default_view(self):
        self.folder.setDefaultPage('n1')
        self.assertEqual(self.folder.default_page, 'n1')
