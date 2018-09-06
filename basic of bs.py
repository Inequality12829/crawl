# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 20:37:50 2018

@author: dell
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('utf-8')
#print(html)

soup = BeautifulSoup(html, features = 'lxml')
print(soup.h1)

print('\n', soup.p)

all_href = soup.find_all('a')
print('\n', all_href)
all_href = [I['href'] for I in all_href]
print('\n', all_href)