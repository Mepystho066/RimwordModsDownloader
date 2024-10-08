from flet import * 
from components.features.BarSeleccion import BarView
from logic.linkProgressing import *
#from logic.fileExtractData import *
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
        
        self.pick_files_dialog =FilePicker(on_result=self.pick_files_result)
        self.selected_files = Text()
        self.pathFile = Text()
        self.addFile = ElevatedButton("Pick file",icon=icons.UPLOAD_FILE,on_click=lambda _: self.pick_files_dialog.pick_files())
        self.addFileContent  = ElevatedButton("Add File Content",on_click=self.stractFiledata)
        #self.expand=True
        #self.updatListLinks= 
        #print(self.page.width)
        self.controls=[Row(
                    controls=[
                        self.addLink,
                        self.addBotton,
                        self.downloadBotton,             
                        self.addFile,
                        self.selected_files,
                        self.addFileContent
                    ]
                ),  
                self.listLinks,    
        ] 


    def pick_files_result(self, e:FilePickerResultEvent):
        #print(e.files,"\n",e.path)
        #self.addFile
        self.selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        )
        self.pathFile.value =( ", ".join(map(lambda f: f.path, e.files)) )
        
        self.update()
  
    def deletObjet(self,objet):
        self.listLinks.controls.remove(objet)
        self.update()

    def downloadContent(self,objet):
        
        pass

    def stractFiledata(self,objet):
        info = open(self.pathFile.value,"r")
        links = info.read().split("\n")
        #print(links)
        for i in links:            
            if i == "":  pass
            dataLink=topMods(i)
            data = asyncio.run(dataLink.mostrar())
            print(data[0],"\n",data[1],"\n",data[2])
            bar = BarView(data[0],i,data[1],self.deletObjet)
            self.listLinks.controls.append( 
                bar
            )
            self.addLink.value = ""
            self.update()

    def button_clicked(self,e):
        ## Esto fue  lo que se modifico 
        dataLink=topMods(self.addLink.value)
        data = asyncio.run(dataLink.mostrar())
        print(data)
        bar = BarView(data[0],self.addLink.value,data[1],self.deletObjet)
        self.listLinks.controls.append( 
            bar
        )
        self.addLink.value = ""
        self.update()
        
"""
Idea  que se me ocurre, agregar un borrar todos o seleccionados

se pude intentar hacer agregandolo a otra lista la cual altera el color para mostrar que esta seleccionada

"""

