# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 19:43:35 2018

@author: dell
"""

import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://morvanzhou.github.io/static/scraping/table.html").read().decode('utf-8')
#print(html)

soup = BeautifulSoup(html, features = 'lxml')

img_links = soup.find_all("img", {"src":re.compile('.*?\.jpg')})
for i in img_links:
    print(i['src'])
    
course_links = soup.find_all('a', {'href':re.compile('https://morvan.*')})
for link in course_links:
    print(link['href'])

