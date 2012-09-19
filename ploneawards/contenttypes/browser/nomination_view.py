from Products.Five import BrowserView

from ploneawards.contenttypes.backtweets import backtweets, backurl
from tweet import tweettext, tweeturl


class NominationView(BrowserView):
    """Standalone view for a nomination.
    """

    # this class is used with multiple templates

    @property
    def votes(self):
        return backtweets(self.context.absolute_url())

    @property
    def tweettext(self):
        return tweettext(self.context)

    @property
    def tweeturl(self):
        return tweeturl(self.context)

    @property
    def backurl(self):
        return backurl(self.context.absolute_url())
