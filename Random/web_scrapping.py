# python3 web_scrapping.py
import requests
import bs4 #beautifulsoup

req = requests.get('https://learncodeonline.in/')
type(req)
# req.text

soup = bs4.BeautifulSoup(req.text, 'lxml')
type(soup)

links = soup.select('img')

for link in links:
    print(link, end='\n')
