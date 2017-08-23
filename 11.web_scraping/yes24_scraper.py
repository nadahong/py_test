import requests
from bs4 import BeautifulSoup


def main():
    res = requests.get('http://www.yes24.com/24/category/bestseller')
    soup = BeautifulSoup(res.text, 'lxml')
    # #bestList > ol > li.num1 > p.copy > a
    for list in soup.select('#bestList > ol > li'):
        print(list.find('p', class_='copy').find('a').text)


main()