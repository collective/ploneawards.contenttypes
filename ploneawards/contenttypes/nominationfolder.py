from five import grok
from plone.directives import dexterity, form
from plone.namedfile.interfaces import IImageScaleTraversable
# Interface class; used to define content-type schema.


class INominationFolder(form.Schema, IImageScaleTraversable):
    """
    INominationFolder Type
    """

# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.


class NominationFolder(dexterity.Container):
    grok.implements(INominationFolder)
