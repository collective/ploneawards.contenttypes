from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class NominationFolderView(BrowserView):
    """Standalone view for a nomination folder.
    """

    index = ViewPageTemplateFile("templates/nominationfolder.pt")

    def render(self):
        return self.index()

    def __call__(self):
        return self.render()


