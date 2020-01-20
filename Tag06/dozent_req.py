import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.google.com')

# print(r.text)
soup = BeautifulSoup(r.text, 'html.parser')

# print(soup.prettify())

print(soup.title.string)
# print(soup.head.title.text)

# https://webscraper.io/test-sites/tables
