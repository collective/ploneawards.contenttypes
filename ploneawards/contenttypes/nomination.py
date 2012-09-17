import logging

from five import grok
from plone.directives import dexterity, form
from zope import schema

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage

from plone.app.textfield import RichText
from ploneawards.contenttypes import MessageFactory as _

from zope.app.container.interfaces import IObjectAddedEvent
from Products.CMFCore.utils import getToolByName

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


# Interface class; used to define content-type schema.

class INomination(form.Schema, IImageScaleTraversable):
    """
    Nomination Type
    """

    information = RichText(
        title=_(u"Detailed information about the entry"),
        required=True,
        default=u"",
    )
    image = NamedImage(
        title=_(u"A fullscreen image that illustrates the innovation"),
        required=False,
        description=_(u"Please upload an image"),
    )
    entry_credits = schema.TextLine(
        title=_(u"Entry credits"),
        required=True,
        default=u"",
        description=_(u"who created the innovation"),
    )
    entry_submitter = schema.TextLine(
        title=_(u"Entry submitter"),
        required=True,
        default=u"",
        description=_(u"who submitted the entry"),
    )

    link = schema.TextLine(
        title=_(u"Link"),
        required=True,
        default=u"",
        description=_(u"A hyperlink to learn more"),
    )

# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.


class Nomination(dexterity.Item):
    grok.implements(INomination)

    # Add your class methods and properties here

    def votes(self):
        return -2


@grok.subscribe(INomination, IObjectAddedEvent)
def notifyOrganization(training, event):
    mail_host = getToolByName(training, 'MailHost')
    portal_url = getToolByName(training, 'portal_url')
    portal = portal_url.getPortalObject()
    sender = portal.getProperty('email_from_address')
    to_email = 'guido.stevens@cosent.nl'
    from_ = '%s <%s>' % (portal.email_from_address, portal.email_from_name)

    if not sender:
        return

    subject = "New Talk submitted"
    message = "A nomination called '%s' was submitted here %s" % (
        training.title, training.absolute_url(),)
    mail_host.send(message, to_email, from_, subject)
