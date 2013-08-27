# -*- coding: utf-8 -*-

from ploneawards.contenttypes.nominationfolder import INominationFolder
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
        self.portal.invokeFactory('Folder', 'test-folder')
        setRoles(self.portal, TEST_USER_ID, ['Member'])
        self.folder = self.portal['test-folder']
        self.folder.invokeFactory(
            'ploneawards.contenttypes.nominationfolder', 'nf1',)
        self.nf1 = self.folder['nf1']

    def test_adding(self):
        self.assertTrue(INominationFolder.providedBy(self.nf1))

    def test_fti(self):
        fti = queryUtility(
            IDexterityFTI, name='ploneawards.contenttypes.nominationfolder')
        self.assertIsNotNone(fti)

    def test_schema(self):
        fti = queryUtility(IDexterityFTI,
                           name='ploneawards.contenttypes.nominationfolder')
        schema = fti.lookupSchema()
        self.assertEqual(INominationFolder, schema)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI,
                           name='ploneawards.contenttypes.nominationfolder')
        factory = fti.factory
        new_object = createObject(factory)
        self.assertTrue(INominationFolder.providedBy(new_object))

    def test_selectable_as_folder_default_view(self):
        self.folder.setDefaultPage('nf1')
        self.assertEqual(self.folder.default_page, 'nf1')
