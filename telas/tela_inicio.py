import flet as ft
from telas.tela_paciente import tela_pacientes
from telas.tela_profissional import tela_profissionais
from telas.tela_consulta import tela_consultas
from telas.tela_relatorios import tela_relatorios

def tela_inicio(page: ft.Page):
    page.clean()

    page.add(
        ft.Container(
            width=2000,
            height=800,
            bgcolor=ft.Colors.GREY_100,
            padding=20,
            border_radius=10,
            content=ft.Column(
                controls=[
                   ft.Text("Bem-vindo ao KJ Clínicas!", 
                    size=24, 
                    weight=ft.FontWeight.BOLD),

                    ft.GridView(
                            width=2000,
                            height=100,
                            runs_count=2,
                            spacing=8,
                            controls= [
                                ft.Container(ft.FilledButton(
                                                "Pacientes",
                                                on_click=lambda _: tela_pacientes(page, tela_inicio)),
                                    width=100, height=100, bgcolor=ft.Colors.PRIMARY, border_radius=8
                                ),
                                ft.Container( ft.FilledButton(
                                                "Profissionais",
                                                on_click=lambda _: tela_profissionais(page, tela_inicio)),
                                    width=100, height=100, bgcolor=ft.Colors.SECONDARY, border_radius=8
                                ),
                                ft.Container( ft.FilledButton(
                                                "Consultas",
                                                on_click=lambda _: tela_consultas(page, tela_inicio)),
                                    width=100, height=100, bgcolor=ft.Colors.TERTIARY, border_radius=8
                                ),
                                ft.Container( ft.FilledButton(
                                                "Relatórios",
                                                on_click=lambda _: tela_relatorios(page, tela_inicio)),
                                    width=100, height=100, bgcolor=ft.Colors.ERROR, border_radius=8
                                ),
                            ],
                        )
                ]
            )

        ),
        
    )
    
