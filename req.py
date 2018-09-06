# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 20:56:05 2018

@author: dell
"""

import requests
import webbrowser
param = {"wd":"python"}
r = requests.get('http://www.baidu.com/s', params = param)
print(r.url)
webbrowser.open(r.url)

data = {'firstname':'yaju', 'lastname':'niubi'}
r = requests.post('http://pythonscraping.com/pages/files/processing.php', data = data)
print(r.text)

file = {'uploadFile':open('C:/Users/dell/Desktop/123/RegEx.png', 'rb')}
r = requests.post('http://pythonscraping.com/pages/files/processing2.php', files = file)
print(r.text)

payload = {'username':'Yaju', 'password':'password'}
r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', data = payload)
print(r.cookies.get_dict())

r = requests.get('http://pythonscraping.com/pages/cookies/profile.php', cookies = r.cookies)
print(r.text)

session = requests.Session()
payload = {'username':'Yaju', 'password':'password'}
r = session.post('http://pythonscraping.com/pages/cookies/welcome.php', data = payload)
print(r.cookies.get_dict())

r = session.get("http://pythonscraping.com/pages/cookies/profile.php")
print(r.text)