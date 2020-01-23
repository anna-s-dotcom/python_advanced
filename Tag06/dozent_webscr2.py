# https://webscraper.io/test-sites/e-commerce/allinone

import requests
from bs4 import BeautifulSoup
URL = 'https://webscraper.io'
r = requests.get(URL+'/test-sites/e-commerce/allinone')
soup = BeautifulSoup(r.text, 'html.parser')

# col-sm-4 col-lg-4 col-md-4

wares = soup.find_all('div', class_ = 'col-sm-4 col-lg-4 col-md-4')

# print(len(wares))

# hole preis und name des Produkts
price = float(wares[0].h4.text[1:])
name = wares[0].a['title']

# folge dem Link zur Detailbeschreibung:
link = wares[0].a['href']
new_r = requests.get(URL + link)
new_soup = BeautifulSoup(new_r.text, 'html.parser')

# Detailbeschreibung:
print(new_soup.find('p', class_="description").text)
print(name, price)
