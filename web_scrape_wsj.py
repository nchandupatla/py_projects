# https://www.wsj.com/
from urllib.request import urlopen
from bs4 import BeautifulSoup
from scrape import scrape

url = "https://www.wsj.com/"
response = scrape(url, "style--column--2ACCiqoG style--column-top--3JPwdFp1 style--column-4--21WwDm3f", "p")
if response:
    print(response)
else:
    print('no response')

