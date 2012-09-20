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

    entry_credits = schema.TextLine(
        title=_(u"Nominee"),
        required=True,
        default=u"",
        description=_(u"The name of the person who deserves this award"),
    )

    information = RichText(
        title=_(u"Detailed information about the nomination"),
        required=True,
        default=u"",
        description=_(u"Tell us why this is special and deserves attention")
    )

    image = NamedImage(
        title=_(u"A fullscreen image that illustrates the innovation"),
        required=True,
        description=_(u"Please upload a 1024x768 image in 4x3 aspect ratio. "
                      u"We're going to present this at the conference, "
                      u"so make it big and splashy. And remember: "
                      u"you can turn *anything* into a screenshot..."),
    )
    entry_submitter = schema.TextLine(
        title=_(u"Proposer"),
        required=True,
        default=u"",
        description=_(u"Your name"),
    )

    link = schema.TextLine(
        title=_(u"Link"),
        required=False,
        default=u"",
        description=_(u"A hyperlink to learn more about the nomination"),
    )

# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.


class Nomination(dexterity.Item):
    grok.implements(INomination)

    # Add your class methods and properties here


@grok.subscribe(INomination, IObjectAddedEvent)
def notifyOrganization(nomination, event):
    mail_host = getToolByName(nomination, 'MailHost')
    portal_url = getToolByName(nomination, 'portal_url')
    portal = portal_url.getPortalObject()
    if not portal.email_from_address:
        return

    from_ = '%s <%s>' % (portal.email_from_address,
                         portal.email_from_name)
    to_email = 'guido.stevens@cosent.nl'
    subject = "[ploneawards] %s" % nomination.title
    message = message_template % (nomination.entry_submitter,
                                  nomination.title,
                                  nomination.description,
                                  nomination.absolute_url())
    mail_host.send(message, to_email, from_, subject)


message_template = """A nomination was submitted by %s

%s

%s

%s
"""
