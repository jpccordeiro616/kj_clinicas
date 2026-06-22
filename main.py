import flet as ft
from telas.tela_inicio import tela_inicio

def main(page: ft.Page):
    page.title = "KJ Clínicas"
    page.window_width = 400
    page.window_height = 600
    page.window_resizable = False
    page.theme_mode = ft.ThemeMode.LIGHT

    tela_inicio(page)

ft.run(main)