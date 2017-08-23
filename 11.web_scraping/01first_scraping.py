import requests
from requests.exceptions import ConnectionError
import itertools


def download(url):
    print('Downloading:', url)
    try:
        html = requests.get(url)
    except ConnectionError as err:
        print(err)
        html = None
    return html


def main():

    for page in itertools.count(1):

        html = download('http://example.webscraping.com/view/-%d' % page)
        if html == 'Invalid record':
            break
        else:
            print(html.text)


if __name__ == '__main__':
    main()
