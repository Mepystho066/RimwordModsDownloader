import asyncio
import aiohttp
from bs4 import BeautifulSoup
import time
class StractLink:
    def __init__(self, link):
        self.link = link
        self.headers = {'User-Agent': 'Mozilla/5.0'}

    async def fetchContent(self):
       async with aiohttp.ClientSession() as session:
            async with session.get(self.link, headers=self.headers) as response:
                return await response.text()

    async def stractModName(self):
        webContent = await self.fetchContent()
        visibleWebContent = BeautifulSoup(webContent, 'html.parser')
        h1_tag = visibleWebContent.find('h1')
        return h1_tag.text if h1_tag else None

    async def stractImage(self):
        webContent = await self.fetchContent()
        getImage = BeautifulSoup(webContent, 'html.parser')
        enlaces_mega = getImage.find_all('img', src=lambda src: src and ('.jpeg' in src or '.jpg' in src ) )
        return [img['src'] for img in enlaces_mega]

    async def extract_mega_url(self):
        webContent= await self.fetchContent()
        visibleWebContent = BeautifulSoup(webContent, 'html.parser')
        enlaces_mega =visibleWebContent.find_all('a' , href= lambda href : href and 'mediafire' in href)
        return [a['href'] for a in enlaces_mega]

    async def mostrar(self):
        mod_name_task = self.stractModName()
        image_urls_task = self.stractImage()
        mega = self.extract_mega_url()
        mod_name = await mod_name_task
        image_urls = await image_urls_task
        linkMega = await mega
        return mod_name,image_urls,mega
        
async def LinkList(lista:[]):
    tasks = [StractLink(link).mostrar() for link in lista]
    results = await asyncio.gather(*tasks)
    return results

async def run_program(link):
    tiempo_inicial = time.time()
    data = StractLink(link)
    result = await data.mostrar()
    print(result)
    tiempo_final = time.time()
    print("Tiempo total:", tiempo_final - tiempo_inicial)
