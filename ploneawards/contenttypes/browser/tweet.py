import urllib


def tweettext(nomination):
    return nomination.entry_credits \
        + " deserves a Plone Award for " \
        + '"' + nomination.Title() + '"!'


def tweeturl(nomination):
    fields = dict(hashtags='ploneawards',
                  url=nomination.absolute_url(),
                  related='ploneawards',
                  text=tweettext(nomination),
                  )
    return "https://twitter.com/intent/tweet?" + urllib.urlencode(fields)
