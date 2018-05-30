# python3 web_scrapping.py
import requests
from bs4 import BeautifulSoup as soup

req = requests.get('https://learncodeonline.in/')
type(req)
# req.text

site = soup(req.text, 'lxml')
type(site)

links = site.select('img')

for link in links:
    print(link, end='\n')
