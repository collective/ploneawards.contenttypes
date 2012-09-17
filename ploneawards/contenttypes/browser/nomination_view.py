from Products.Five import BrowserView

from ploneawards.contenttypes.backtweets import backtweets


class NominationView(BrowserView):
    """Standalone view for a nomination.
    """

    # this class is used with multiple templates

    def votes(self):
        return backtweets(self.context.absolute_url())
