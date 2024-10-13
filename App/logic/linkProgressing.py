import asyncio
import aiohttp
from aiohttp import web 
from bs4 import BeautifulSoup
import time
import random

"""
Cada clase define una pagina web
"""

class topMods:
    
    def __init__(self, link):
        self.link = link
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)  Chrome/91.0.4472.124'}
        self.params={
      #'api_key': 'YOUR_API_KEY',
      #'url': 'http://url', ## Cloudflare protected website 
      'bypass': 'cloudflare_level_1',}
    async def fetchContent(self,linkData = None ):
        if linkData is None:
            linkData = self.link
        #time.sleep(random.randint(3,6))
        await asyncio.sleep(random.uniform(3, 5))
        async with aiohttp.ClientSession(cookie_jar=aiohttp.CookieJar()) as session:  
           # time.sleep(random.randint(1,2))
            async with session.get(linkData, headers=self.headers,params=self.params) as response:
                return await response.text()

    async def stractModName(self):
        time.sleep(random.randint(1,2))
        webContent = await self.fetchContent()
        visibleWebContent = BeautifulSoup(webContent, 'html.parser')
        h1_tag = visibleWebContent.find('h1')
        return h1_tag.text

    async def stractImage(self):
        time.sleep(random.randint(1,2))
        webContent = await self.fetchContent()
        getImage = BeautifulSoup(webContent, 'html.parser')
        enlaces_mega = getImage.find_all('img', src=lambda src: src and ('.webp' in src))# or '.jpg' in src ) )
        return [img['src'] for img in enlaces_mega]

    async def extract_mega_url(self):
        time.sleep(random.randint(1,2))
        webContent= await self.fetchContent()
        visibleWebContent = BeautifulSoup(webContent, 'html.parser')
        enlaces_mega =visibleWebContent.find_all('a' , href= lambda href : href and 'sharemods' in href)
        link = [a['href'] for a in enlaces_mega]
        #Actualizar todos los componentes de link para que ya no sean link[0]
        return link

    async def extract_mega_url2(self):
        time.sleep(random.randint(1,2))
        link = await self.extract_mega_url()
        print("depu" + link[0])
        webContent= await self.fetchContent(link[0])
        visibleWebContent = BeautifulSoup(webContent, 'html.parser')
        button = visibleWebContent.find("button",{'id':'downloadbtn'})
        #info = web.Response(button)
        #linkStract = "https://modsfire.com"+button["href"]
        
        #async with aiohttp.ClientSession() as session:
        #    # Simulamos un POST, dependiendo de los datos requeridos
        #    async with session.post(linkStract, data={'key': 'value'}) as response:
        #        content = await response.text() 
        #        info = BeautifulSoup(content,'html.parser')
        print(visibleWebContent)

        #webContent2= await self.fetchContent(linkStract)
        #visibleWebContent2 = BeautifulSoup(webContent2, 'html.parser')
        #button2 = visibleWebContent.find("a",{'class':'download-button'})#, href= lambda href : href and '/d/' in href)
        #print(button2)
      
        return ""# finalLink


    async def mostrar(self):
        complemento = self.link.split("/")
        mod_name_task = self.stractModName()
        image_urls_task = self.stractImage()
        mega = self.extract_mega_url()
        mega2= self.extract_mega_url2()
        mod_name = await mod_name_task
        image_urls = await image_urls_task
        linkMega = await mega
        linkMega2 = await mega2
        print(linkMega2)
        name = mod_name.replace("\n","")
        name =  name.replace("        ","")
        contenido = f'https://{complemento[2]}{image_urls[0]}'
        
        return name,contenido,linkMega[0], linkMega2

async def LinkList(lista:[]):
    tasks = [StractLink(link).mostrar() for link in lista]
    results = await asyncio.gather(*tasks)
    return results
"""
async def run_program(link):
    tiempo_inicial = time.time()
    data = StractLink(link)
    result = await data.mostrar()
    print(result)
    tiempo_final = time.time()
    print("Tiempo total:", tiempo_final - tiempo_inicial)
"""

## TESTS

##if __name__ =="__main__":
##    info = topMods("https://top-mods.com/mods/rimworld/other/13165-ebsg-framework.html")    
##    
##    info2 = asyncio.run(info.extract_mega_url2())
##    print(info2)
