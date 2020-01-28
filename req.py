import requests
from bs4 import BeautifulSoup
#https://webscraper.io/
r=requests.get("https://webscraper.io/test-sites/tables")

# print(r.text)
#holt sich die HTML Struktur der URL Adresse
soup=BeautifulSoup(r.text, "html.parser")
# print(soup.prettify())
#nur ein title der seite wird ausgedrückt
# print(soup.table.prettify())
tables=soup.findall("table")
print(len(tables))

# print(tables[0].prettify())
rows=tables[0].findall("tr")

print(row.find.all)

print(rows[0].findall("th"))

for elem in header:
    print(elem.text, end="\t")

print()

for row in rows[1:]:
    data=row.findall("td")
    for elem in data:
        print(elem.text, end="/t")
    print()
