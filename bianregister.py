# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

url='https://sy.lianjia.com/ershoufang/pg'
# url = 'https://sy.lianjia.com/ershoufang/hepingqu/'
heade={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}#请求头，模拟浏览器登陆


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