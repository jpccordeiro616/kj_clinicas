import flet as ft

def tela_pacientes(page: ft.Page):
    page.clean()

    page.add(
        ft.Text("Tela de Pacientes", size=24, weight=ft.FontWeight.BOLD),
        ft.ElevatedButton(
            "Voltar",
            on_click=lambda _: page.go_back()
        )
    )