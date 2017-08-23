import requests
from bs4 import BeautifulSoup


res = requests.get('http://example.webscraping.com')

soup = BeautifulSoup(res.text, 'lxml')

print(soup.body)
