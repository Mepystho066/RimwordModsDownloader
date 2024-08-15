from flet import * 
from features.BarSeleccion import BarView
from features.components.linkProgressing import StractLink
import asyncio

# Es recomendable no utilizar ni altura ni ancho predetermiado 

"""
Agregar alerta cuando no se tiene ninguna informacion
Para la barras se puedan utilizar en todo el area se necesita utilziar 
"""

class LinksComponent(Column):
    def __init__(self):
        super().__init__()
        self.addLink = TextField(label="Add link")
        self.addBotton = ElevatedButton(text="add", on_click=self.button_clicked)
        self.listLinks = Row(spacing=2, wrap=True,auto_scroll=True,scroll=True,height=500)
        self.downloadBotton = ElevatedButton(text="Download all", on_click=self.downloadContent)
        self.buttonDownloadTxt = FilePicker()
        
        
        #self.expand=True
        #self.updatListLinks= 
        #print(self.page.width)
        self.controls=[Row(
                    controls=[
                        self.addLink,
                        self.addBotton,
                        self.downloadBotton,
                        
                        
                    ]
                ),
                
                self.listLinks,
                
        ]
    
    
    
    def deletObjet(self,objet):
        self.listLinks.controls.remove(objet)
        self.update()

    def downloadContent(self,objet):
        #self.listLinks.controls.remove(objet)
        self.update()

    def button_clicked(self,e):
        
        ## Esto fue  lo que se modifico 
        dataLink=StractLink("https://rimworldbase.com/?upd=1720848762542")
        data = asyncio.run(dataLink.mostrar())
        print(data[0],"\n",data[1],"\n",data[2])
        bar = BarView(data[0],self.addLink.value,data[1][0],self.deletObjet)
        self.listLinks.controls.append( 
            bar
        )
        self.addLink.value = ""
        
        self.update()
        
"""
Idea  que se me ocurre, agregar un borrar todos o seleccionados

se pude intentar hacer agregandolo a otra lista la cual altera el color para mostrar que esta seleccionada

"""

