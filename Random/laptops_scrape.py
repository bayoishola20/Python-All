# python3 web_scrapping1.py
#=============== Scrapping newegg.com for laptops/notebooks ===========#
import requests
from bs4 import BeautifulSoup as soup

req = requests.get('https://www.newegg.com/Laptops-Notebooks/Category/ID-223?Tid=17489')
type(req)
# req.text

site = soup(req.text, "html.parser")
# print(site.prettify())
# type(site)

# Grab laptops containers
containers = site.findAll("div", {"class": "item-container"})
# print(len(containers))
# containers[0]
# items_card = containers[0].div.div.a
# items_title = containers[0].div.div.a.img["title"]

output = "Random/laptops.xlsx"
f = open(output, "w+")
headers = "Brand Name, Title, Price, Shipping \n"

f.write(headers)

for container in containers:
    brand_name = container.div.div.a.img["title"]
    brand_title = container.findAll("a", {"class":"item-title"})[0].text.replace(",", "")
    brand_price = container.findAll("li", {"class":"price-current"})[0].text.replace("\n\n|\n","").replace("\n–\n\n","").strip()
    brand_ship = container.findAll("li", {"class":"price-ship"})[0].text.strip()
    
    print("brand name" + brand_name)
    print("brand_title" + brand_title)
    print("brand_price" + brand_price)
    print("brand_ship" + brand_ship)

    f.write(brand_name + "," + brand_title + "," + brand_price + "," + brand_ship + "\n" )

f.close()