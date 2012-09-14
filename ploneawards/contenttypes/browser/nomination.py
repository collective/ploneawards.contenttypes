from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class NominationView(BrowserView):
    """Standalone view for a nomination.
    """

    index = ViewPageTemplateFile("templates/nomination.pt")

    def render(self):
        return self.index()

    def __call__(self):
        return self.render()
