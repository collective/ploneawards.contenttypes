import urllib
from urllib2 import urlopen
from bs4 import BeautifulSoup
import time
from plone.memoize import ram
import logging

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
    # any exceptions thrown here should be caught outside the cache
    u = urlopen(backurl(url))
    html = u.read()
    u.close()

    soup = BeautifulSoup(html)
    # this will break if backtweet html changes...
    try:
        results = soup.find(id='results') \
            .find('div', 'title').find('span', 'blue').string
        return int(results)
    except AttributeError:
        # this is valid and indicates: no tweets
        # return a cacheable result count
        return 0


def backurl(url):
    return 'http://backtweets.com/search/?q=%s' % urllib.quote(url)


if __name__ == '__main__':
    # for fast prototyping
    url = 'bit.ly/Sazv3E'
    count = backtweets(url)
    print(count)
