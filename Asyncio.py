# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 18:50:25 2018

@author: dell
"""

import time
import asyncio
"""
def job(t):
    print('Start job', t)
    time.sleep(t)
    print('Job', t, ' takes ', t, ' s')

def main():
    [job(t) for t in range(1, 3)]
    
t1 = time.time()
main()
print('NO async total time :', time.time() - t1)

async def job(t):
    print('Start job', t)
    await asyncio.sleep(t)
    print('Job', t, ' takes ', t, ' s')

async def main(loop):
    tasks = [loop.create_task(job(t)) for t in range(1, 3)]
    await asyncio.wait(tasks)

t1 = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()
print('Async total time: ', time.time() - t1)
"""

#import requests

URL = 'https://morvanzhou.github.io/'

"""
def normal():
    for i in range(2):
        r = requests.get(URL)
        url = r.url
        print(url)
        
t1 = time.time()
normal()
print('Normal total time:', time.time() - t1)
"""

import aiohttp

async def job(session):
    response = await session.get(URL)
    return str(response.url)

async def main(loop):
    async with aiohttp.ClientSession() as session:
        tasks = [loop.create_task(job(session)) for i in range(2)]
        finished, unfinished = await asyncio.wait(tasks)
        all_results = [r.result() for r in finished]
        print(all_results)
    
t1 = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()
print('Async total time:', time.time() - t1)
