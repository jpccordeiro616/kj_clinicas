import flet as ft
from telas.tela_paciente import tela_pacientes
from telas.tela_profissional import tela_profissionais
from telas.tela_consulta import tela_consultas
from telas.tela_relatorios import tela_relatorios

def tela_inicio(page: ft.Page):
    page.clean()

    page.add(
        ft.Text("Bem-vindo ao KJ Clínicas!", 
                size=24, 
                weight=ft.FontWeight.BOLD)
    ,
    ft.ElevatedButton(
        "Pacientes",
        on_click=lambda _: tela_pacientes(page, tela_inicio)
    ),
    ft.ElevatedButton(
        "Profissionais",
        on_click=lambda _: tela_profissionais(page, tela_inicio)
    ),
    ft.ElevatedButton(
        "Consultas",
        on_click=lambda _: tela_consultas(page, tela_inicio)
    ),
    ft.ElevatedButton(
        "Relatorios",
        on_click=lambda _: tela_relatorios(page, tela_inicio)
    ))
