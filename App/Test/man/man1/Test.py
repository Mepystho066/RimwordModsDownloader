import flet as ft

def main(page):
    
    texto1 = ft.Text("asdasdas",width=200)
    texto2 = ft.Text("asdasdas",width=200)
    texto3 = ft.Text("asdasdas",width=200)
    
    row =  ft.Row(controls=[texto1,texto2,texto3],wrap=True)
    page.update()
    page.add(
        row
    )


ft.app(main)