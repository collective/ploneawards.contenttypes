from plone.app.controlpanel.security import ISecuritySchema
from plone.dexterity.utils import createContentInContainer


def setupVarious(context):

    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.

    if context.readDataFile('ploneawards.contenttypes_various.txt') is None:
        return

    # Add additional setup code here

    # put on self reg
    portal = context.getSite()
    ISecuritySchema(portal).enable_self_reg = True

    # members folder
    portal_type = "fourdigits.dexteritycontenttypes.folder"
    id = "members"
    if id not in portal.objectIds():
        title = u"Members"
        members = createContentInContainer(
                                    portal,
                                    id=id,
                                    title=title,
                                    checkConstraints=False,
                                    portal_type=portal_type)


    # nomination folder
    portal_type = "ploneawards.contenttypes.nominationfolder"
    id = "nominations"
    if id not in portal.objectIds():
        title = u"Nominations"
        nominations = createContentInContainer(
                                    portal,
                                    id=id,
                                    title=title,
                                    checkConstraints=False,
                                    portal_type=portal_type)
