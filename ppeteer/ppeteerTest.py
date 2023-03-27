import requests

from pyquery import PyQuery as pq

def init():
    url = 'http://quotes.toscrape.com/js/'

    response = requests.get(url)

    doc = pq(response.text)

    print('Quotes:', doc('.quote').length)


if __name__ == '__main__':
    init()