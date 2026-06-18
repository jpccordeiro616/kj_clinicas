import flet as ft

def main(page: ft.Page):
    page.title = "KJ Clinicas"

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.Icons.MENU),
        title=ft.Text("KJ Clinicas", size=20, weight=ft.FontWeight.BOLD),
        bgcolor=ft.Colors.SURFACE_CONTAINER,
        actions=[
            ft.IconButton(ft.Icons.SEARCH),
            ft.IconButton(ft.Icons.MORE_VERT),
        ],
    )

    cpf = ft.TextField(label="CPF", width=300)
    telefone = ft.TextField(label="Telefone", width=300)
    cep = ft.TextField(label="CEP", width=300)

    page.add(cpf, telefone, cep)

ft.run(main)