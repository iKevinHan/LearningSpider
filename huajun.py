# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.onlinedown.net/hits/windows/2/")
soup = BeautifulSoup(r.text, 'lxml')
# print(soup, type(soup))

print (len(soup.find_all("a", "title")))
for a in soup.find_all("a", "title"):
    print (a.text)

print (len(soup.find_all("span", "size")))
for a in soup.find_all("span", "size"):
    print(a.text)

print (len(soup.find_all("span", "lan")))
for a in soup.find_all("span", "lan"):
    print(a.text)

print (len(soup.find_all("span", "pop")))
for a in soup.find_all("span", "pop"):
    print(a.text)

print (len(soup.find_all("span", "dro")))
for a in soup.find_all("span", "dro"):
    print(a.text)

print (len(soup.find_all("span", "time")))
for a in soup.find_all("span", "time"):
    print(a.text)