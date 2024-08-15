from flet import *

"""
self.image No funciona en la parte web
"""
class BarView(Container):
    def __init__(self,name,link,image,barforDelet):
        super().__init__()
        #self.image = Test
        self.name = Text(name ,max_lines=1, width=200,overflow=TextOverflow.ELLIPSIS,theme_style=TextThemeStyle.TITLE_LARGE)
        self.link =  Text(link,max_lines=1, width=200 ,overflow=TextOverflow.ELLIPSIS)
        self.image = Image(src=f'{image}',width=100,height=100)
        self.editName= TextField()
        self.editLink= TextField()
        self.barforDelet = barforDelet
        #self.expand=True
        self.width=400
        self.height=100
        self.border_radius=6
        self.bgcolor=colors.SURFACE_VARIANT
        self.botones = Container(
                        Row(
                            controls=[
                                IconButton(icon=icons.EDIT,on_click=self.barEdit),
                                IconButton(icon=icons.DELETE,on_click=self.barDelet)
                             ]
                        ),
                        visible=False,
                     )
        

        self.structure = Container(
            
            Row(  

                controls=[
                    Container(
                        self.image,
                        ),
                    
                    Column(  
                        controls=[
                        self.name,
                        self.link,
                        ],
                    ),
                    self.botones 
                
                ],
                
                #vertical_alignment=CrossAxisAlignment.CENTER,
                #alignment=MainAxisAlignment.SPACE_BETWEEN,
                
                
            ),
         
            on_click= self.viewBottons,
        )

        self.editStructure=Container( 
            Row( 
                controls=[
                    Column(  
                        controls=[
                        self.editName,
                        self.editLink,
                        ]

                        ),
                        Row(
                            controls=[
                                IconButton(icon=icons.EDIT,on_click=self.saveEdit),
                             ]
                        )         
                ],
                #vertical_alignment=CrossAxisAlignment.CENTER,
                #alignment=MainAxisAlignment.SPACE_BETWEEN,
                

            ),
            bgcolor= colors.SURFACE_VARIANT,
            border_radius=6,
            visible=False,
        )
        
        ## Component Controls 
        self.content=( Row(controls=[self.structure,self.editStructure]))
        
    def barEdit(self,e):
        self.editName.value= self.name.value
        self.editLink.value= self.link.value
        self.editStructure.visible=True
        self.structure.visible=False
        
        #print("Se queire editar")
        self.update()

    def saveEdit(self,e):
        self.name.value= self.editName.value
        self.link.value= self.editLink.value
        self.structure.visible=True
        self.editStructure.visible=False
        self.update()
        #print("Se duardo la edicion")
    
    def viewBottons(self,e):
        self.botones.visible= True if self.botones.visible == False else False
        #if (self.botones.visible == False):
        #    self.botones.visible=True
        #    self.structure.content.width=500
        #else:
        #    self.botones.visible=False
        #    self.structure.width=400
        self.update()
    
    def barDelet(self,bar):
        self.barforDelet(self)