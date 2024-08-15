from flet import * 


class DataSheet(Column):
    def __init__(self):
        super().__init__()
        #self.width =400,
        self.controlMensage = ListView(spacing=10, padding=20,height=100,visible=False)
        self.infoBottom = ElevatedButton(text="info",on_click=self.viewControllMensaje )
        self.texto = Text("")
        #self.addInfo(self.texto)
        self.estructure = Row(
                controls=[
                    self.infoBottom,
                    self.controlMensage
                ]
        )
        self.controls =[
            self.estructure
            
        ]


    def viewControllMensaje(self,e):
        self.controlMensage.visible= True if self.controlMensage.visible == False else False
        self.update()
    
    def addInfo(self,e):
        self.controlMensage.controls.append(Text(e))
        self.update()

        
