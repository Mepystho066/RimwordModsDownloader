import asyncio
import aiohttp
from aiohttp import web 
from bs4 import BeautifulSoup
import time
import random
import os 

async def fetchContent(link,name):
        directory = "App/downloads"

        file_path = os.path.join(directory, name)

        if not os.path.exists(directory):
          os.makedirs(directory)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)  Chrome/91.0.4472.124'}
        #time.sleep(random.randint(3,6))
        params={
        #'api_key': 'YOUR_API_KEY',
        #'url': 'http://url', ## Cloudflare protected website 
        #'bypass': 'cloudflare_level_1',
        }
        await asyncio.sleep(random.uniform(3, 5))
        async with aiohttp.ClientSession(cookie_jar=aiohttp.CookieJar()) as session:  
           # time.sleep(random.randint(1,2))
            async with session.get(link, headers=headers,params=params) as response:
              #return await response.text
              if response.status == 200:
                with open(file_path , "wb" ) as file: 
                  while True: 
                    data = await response.content.read(1024)
                    if not data:
                      break
                  file.write(data)
                print("Descarga exitosa")
              else :
                print("Error en la descarga del Mod")

# https://rimworldbase.com/tribal-essentials-mod/

if __name__ == "__main__": 
  asyncio.run(fetchContent("https://rimworldbase.com/tribal-essentials-mod/", "test.zip"))
