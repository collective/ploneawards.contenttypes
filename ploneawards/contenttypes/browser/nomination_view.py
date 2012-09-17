import urllib
from Products.Five import BrowserView

from ploneawards.contenttypes.backtweets import backtweets, backurl


class NominationView(BrowserView):
    """Standalone view for a nomination.
    """

    # this class is used with multiple templates

    @property
    def votes(self):
        return backtweets(self.context.absolute_url())

    @property
    def tweettext(self):
        return self.context.entry_credits \
            + " deserves a Plone Award for " \
            + '"' + self.context.Title() + '"!'

    @property
    def tweeturl(self):
        fields = dict(hashtags='ploneawards',
                      url=self.context.absolute_url(),
                      related='ploneawards',
                      text=self.tweettext,
                      )
        return "https://twitter.com/intent/tweet?" + urllib.urlencode(fields)

    @property
    def backurl(self):
        return backurl(self.context.absolute_url())
