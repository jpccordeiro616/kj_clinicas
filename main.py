import flet as ft
from telas.tela_inicio import tela_inicio

def main(page: ft.Page):
    page.title = "KJ Clínicas"
    tela_inicio(page)

ft.run(main)