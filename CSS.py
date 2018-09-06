# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 17:27:00 2018

@author: dell
"""
from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("https://morvanzhou.github.io/static/scraping/list.html").read().decode('utf-8')
print(html)

soup = BeautifulSoup(html, features = 'lxml')

month = soup.find_all('li', {"class":"month"})
for i in month:
    print(i.get_text())
    
jan = soup.find('ul', {"class":'jan'})
d_jan = jan.find_all('li')
for i in d_jan:
    print(i.get_text())