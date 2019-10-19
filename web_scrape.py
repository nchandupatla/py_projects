from urllib.request import urlopen
from bs4 import BeautifulSoup
from scrape import scrape

url = "https://www.bbc.com/sport/football/46897172"
response = scrape(url, "story-body sp-story-body gel-body-copy", "p")
if response:
    print(response)
else:
    print('no response')