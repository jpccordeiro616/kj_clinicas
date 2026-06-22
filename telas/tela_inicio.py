import flet as ft

def tela_login(page: ft.Page):
    page.title = "Tela de Login"
    page.add(
        ft.GridView(
            width=5000, height=5000,
            runs_count=2,
            spacing=8,
            controls=[
                ft.Container(
                    ft.Button("Login",color=ft.Colors.WHITE, bgcolor=ft.Colors.BLUE),
                    width=1000, height=500, bgcolor=ft.Colors.BLUE, border_radius=8
                ),
                ft.Container(
                    ft.Button("Registrar",color=ft.Colors.WHITE, bgcolor=ft.Colors.GREEN),
                    width=1000, height=500, bgcolor=ft.Colors.GREEN, border_radius=8
                ),  
            ],
        )   
    )

ft.run(tela_login)