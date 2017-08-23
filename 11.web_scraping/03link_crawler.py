import requests
from bs4 import BeautifulSoup


res = requests.get('http://example.webscraping.com/index/1')
soup = BeautifulSoup(res.text, 'lxml')

for link in soup.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])

