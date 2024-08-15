from flet import *
from components.ListLinks import LinksComponent
from components.DownloadInfo import DataSheet
from logic.fileExtractData import *

"""
Lista de mejoras:
Organizar los colores 
quitar el emoji y agregar otro 
"""
class Main:

    def __init__(self,page:Page):
        super().__init__()
        self.page= page 
        self.AppView()
        
       # self.page.debug=True

    def AppView(self):
        self.ListaTest = LinksComponent()
        self.data = DataSheet()
        self.addFile = ElevatedButton("Add File")
        self.header = Container(
                    Row(controls={
                        self.data,
                        self.addFile,
                    },
                    alignment= alignment.bottom_center
                    ),
                        #alignment=alignment.bottom_right,
                        
                )
        self.body = Column(
                controls=[
                    Container(
                        self.ListaTest,
                        #width = self.page.window_width,
                        height=500,
                        padding=2,
                        bgcolor=colors.SURFACE_TINT,
                        border_radius=6
                    ),
                    
                ]
                
            )   
        
       #print(ReadFile("App/Test/webs.txt"))
        self.page.add(
            self.header,
            self.body
        )
        
app(target=Main)
