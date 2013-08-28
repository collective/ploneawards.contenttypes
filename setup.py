# -*- coding:utf-8 -*-

from setuptools import find_packages
from setuptools import setup

version = '0.2.dev0'
long_description = (
    open('README.rst').read() + '\n' +
#    open('CONTRIBUTORS.rst').read() + '\n' +
    open('CHANGES.rst').read()
)

setup(name='ploneawards.contenttypes',
      version=version,
      description="Content types for the Plone Awards site.",
      long_description=long_description,
      classifiers=[
          "Development Status :: 4 - Beta",
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Framework :: Plone :: 4.3",
          "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Topic :: Software Development :: User Interfaces",
      ],
      keywords='',
      author='',
      author_email='',
      url='https://github.com/collective/ploneawards.contenttypes',
      license='GPLv2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ploneawards'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'beautifulsoup4',
          'collective.carousel>1.6.1',  # TODO: move this out of here
          'collective.dexteritytextindexer',
          'collective.z3cform.datetimewidget',
          'plone.app.dexterity[grok,relations]',
          'plone.app.referenceablebehavior',
          'plone.app.versioningbehavior',
          'plone.directives.dexterity',
          'plone.directives.form',
          'plone.formwidget.namedfile',
          'plone.memoize',
          'plone.namedfile[blobs]',
          'Products.CMFCore',
          'Products.GenericSetup',
          'setuptools',
          'zope.i18nmessageid',
          'zope.schema',
      ],
      extras_require={
          'test': [
              'plone.app.testing',
              'plone.testing',
              'zope.component',
          ],
      },
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
