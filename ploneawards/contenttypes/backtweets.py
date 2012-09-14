import urllib
from urllib2 import urlopen
from bs4 import BeautifulSoup


def backtweets(url):
    """Crawl the backtweets site and return number of tweets on <url>
    """
    backurl = 'http://backtweets.com/search/?q=%s' % urllib.quote(url)
    u = urlopen(backurl)
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


if __name__ == '__main__':
    # for fast prototyping
    url = 'bit.ly/Sazv3E'
    count = backtweets(url)
    print(count)
