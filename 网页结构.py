# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 18:39:50 2018

@author: dell
"""
from urllib.request import urlopen
import re

html = urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('utf-8')

#print(html)

res = re.findall(r"<title>(.+?)</title>", html)
print("\nPage title is: ", res[0])

res2 = re.findall(r"<p>(.*?)</p>", html, flags = re.DOTALL)
print("\nPage paragraph is: ", res2[0])

res3 = re.findall(r'href="(.*?)"', html)
print("\nAll links: ", res3)