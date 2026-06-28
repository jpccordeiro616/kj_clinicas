import flet as ft
from funcoes.relatorios import *

def tela_relatorios(page: ft.Page, voltar_para):
    page.clean()

    resultado = ft.Column(scroll=ft.ScrollMode.AUTO)

    page.add(
        ft.Column(
            [
                ft.Text(
                    "Relatórios",
                    size=28,
                    weight=ft.FontWeight.BOLD
                ),

                ft.Row([
                    ft.ElevatedButton(
                        "Consultas por Profissional",
                        on_click=lambda e: mostrar_profissionais(resultado)
                    ),
                    ft.ElevatedButton(
                        "Consultas por Tipo",
                        on_click=lambda e: mostrar_tipos(resultado)
                    ),
                ]),

                ft.Row([
                    ft.ElevatedButton(
                        "Total Previsto de Faturamento",
                        on_click=lambda e: mostrar_faturamento(resultado)
                    ),
                    ft.ElevatedButton(
                        "Pacientes por Bairro",
                        on_click=lambda e: mostrar_bairros(resultado)
                    ),
                ]),

                ft.Row([
                    ft.ElevatedButton(
                        "Horários Livres e Ocupados",
                        on_click=lambda e: mostrar_horarios(resultado)
                    ),
                ]),

                ft.Divider(),

                resultado,

                ft.ElevatedButton(
                    "Voltar",
                    on_click=lambda e: voltar_para(page)
                )
            ]
        )
    )