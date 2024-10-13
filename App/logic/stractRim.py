import asyncio
import aiohttp
from bs4 import BeautifulSoup
import time
import random

class rimworld:
    def __init__(self, link):
        self.link = link
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)  Chrome/91.0.4472.124'}
        self.params={
      #'api_key': 'YOUR_API_KEY',
      #'url': 'http://url', ## Cloudflare protected website 
      'bypass': 'cloudflare_level_1',}
    async def fetchContent(self):
        #time.sleep(random.randint(3,6))
        await asyncio.sleep(random.uniform(3, 5))
        async with aiohttp.ClientSession(cookie_jar=aiohttp.CookieJar()) as session:  
           # time.sleep(random.randint(1,2))
            async with session.get(self.link, headers=self.headers,params=self.params) as response:
                return await response.text()

    async def stractModName(self):
        time.sleep(random.randint(1,2))
        webContent = await self.fetchContent()
        visibleWebContent = BeautifulSoup(webContent, 'html.parser')
        h1_tag = visibleWebContent.find('h1')
        return h1_tag

    async def stractImage(self):
        time.sleep(random.randint(1,2))
        webContent = await self.fetchContent()
        getImage = BeautifulSoup(webContent, 'html.parser')
        enlaces_mega = getImage.find_all('img', src=lambda src: src and ('.jpg' in src))# or '.jpg' in src ) )
        return [img['src'] for img in enlaces_mega]

    async def extract_mega_url(self):
        time.sleep(random.randint(1,2))
        webContent= await self.fetchContent()
        visibleWebContent = BeautifulSoup(webContent, 'html.parser')
        enlaces_mega =visibleWebContent.find_all('a' , href= lambda href : href and 'download' in href)
        return [a['href'] for a in enlaces_mega]

    async def mostrar(self):
        mod_name_task = self.stractModName()
        image_urls_task = self.stractImage()
        mega = self.extract_mega_url()
        mod_name = await mod_name_task
        image_urls = await image_urls_task
        linkMega = await mega
        return mod_name,image_urls,linkMega
