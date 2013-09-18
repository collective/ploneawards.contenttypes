# -*- coding: utf-8 -*-

from plone.memoize import ram
from urllib2 import urlopen

import json
import logging
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def backtweets(url):
    """Crawl the backtweets site and return number of tweets on <url>
    """
    if url == '':
        logger.error('empty url, aborting backtweets crawl')
        return -1
    # delegate to avoid caching exceptions
    try:
        return _backtweets(url)
    # catch exceptions outside of the cache
    except Exception:
        logger.exception("Cannot get votes from backtweet for: %s", url)
        return -1


# cache tweet count for five minutes
@ram.cache(lambda *args: (args, time.time() // (60 * 5)))
def _backtweets(url):
    """A cacheable vote counter that avoids caching errors
    by not catching many exceptions."""
    logger.debug("Refreshing vote count for: %s" % url)
    # any exceptions thrown here should be caught outside the cache
    return _tweets(url) + _likes(url)


def _tweets(url):
    """Use Twitter API to return the number of 'tweets' of url.

    The API returns something like this:

    {u'count': 511, u'url': u'http://plone.org/'}
    """
    API_URL = u'http://urls.api.twitter.com/1/urls/count.json?url='
    info = json.load(urlopen(API_URL + url))
    return int(info[u'count'])


def _likes(url):
    """Use Facebook API to return the number of 'likes' of url.

    The API returns something like this:

    {u'http://plone.org': {u'id': u'http://plone.org', u'shares': 380}}

    Note that 'shares' is included only if the url has 'likes' indeed.
    """
    try:
        API_URL = u'https://graph.facebook.com/?ids='
        info = json.load(urlopen(API_URL + url))
        info = info[url]
        return int(info[u'shares']) if u'shares' in info else 0
    except TypeError:
        # this is valid and indicates: no info
        # return a cacheable result count
        return 0


def backurl(url):
    return 'http://tagboard.com/ploneawards'


if __name__ == '__main__':
    # for fast prototyping
    url = 'http://plone.org'
    print _tweets(url)
    print _likes(url)
    print backtweets(url)
