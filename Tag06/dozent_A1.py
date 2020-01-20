# Lies die Tablle: 'Table without thead tag' ein.
# (3. Tablle auf: 'https://webscraper.io/test-sites/tables')
# Gib die Daten als Liste von Listen aus.

import requests
from bs4 import BeautifulSoup

r = requests.get('https://webscraper.io/test-sites/tables')
soup = BeautifulSoup(r.text, 'html.parser')
table = soup.find_all('table')[2]
header = table.find_all('th')
new_table = []

templist = []
for th in header:
    templist.append(th.text)
new_table.append(templist)

# print(new_table)
for row in table.find_all('tr')[1:]:
    templist = []
    for td in row.find_all('td'):
        templist.append(td.text)
    new_table.append(templist)
print(new_table)
