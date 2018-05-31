# python3 web_scrapping1.py
#=============== Scrapping newegg.com for laptops/notebooks ===========#
import requests
from bs4 import BeautifulSoup as soup

req = requests.get('https://www.newegg.com/Laptops-Notebooks/Category/ID-223?Tid=17489')
type(req)
# req.text

site = soup(req.text, "html.parser")
print(site.prettify())
type(site)

links = site.select('img')

for link in links:
    print(link, end='\n')