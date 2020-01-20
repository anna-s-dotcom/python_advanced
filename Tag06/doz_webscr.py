# https://webscraper.io/test-sites/tables
import requests
from bs4 import BeautifulSoup

r = requests.get('https://webscraper.io/test-sites/tables')

soup = BeautifulSoup(r.text, 'html.parser')

# print(soup.table.prettify())
tables = soup.find_all('table')

# print(len(tables))
# print(tables[0].prettify())
# print(tables[0].thead)

rows = tables[0].find_all('tr')

header = rows[0].find_all('th')

for elem in header:
    print(elem.text, end = '\t')
print()
for row in rows[1:]:
    data = row.find_all('td')
    for elem in data:
        print(elem.text, end = '\t')
    print()
