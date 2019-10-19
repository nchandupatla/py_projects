from urllib.request import urlopen
from bs4 import BeautifulSoup

def scrape(url, cls, attr):
    page = ''
    try:
        page = urlopen(url)
    except Exception as e:
        print("Error opening the URL", e)

    soup = BeautifulSoup(page, 'html.parser')
    content = soup.find('div', {"class": cls})
    if content:
        article = ''
        for i in content.findAll(attr):
            article = article + ' ' +  i.text
        return article
