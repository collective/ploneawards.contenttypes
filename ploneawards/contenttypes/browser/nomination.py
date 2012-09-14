from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class NominationView(BrowserView):
    """Standalone view for a nomination.

    Re-uses the carousel-view to fill the #carousel slot.
    """

    index = ViewPageTemplateFile("templates/nomination.pt")

    def render(self):
        return self.index()

    def __call__(self):
        return self.render()


