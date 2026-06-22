import flet as ft

def tela_consultas(page: ft.Page, voltar_para):
    page.clean()

    def voltar(e):
        voltar_para(page)

    page.add(
        ft.Text("Tela de Consultas", size=24, weight=ft.FontWeight.BOLD),
        ft.ElevatedButton(
            "Voltar",
            on_click=voltar
        )
    )