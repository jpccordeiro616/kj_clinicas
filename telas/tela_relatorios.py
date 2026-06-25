import flet as ft
from funcoes.relatorios import (
    consultas_por_profissional,
    consultas_por_tipo,
    faturamento_total
)

def tela_relatorios(page: ft.Page, voltar_para):
    page.clean()

    resultado = ft.Column()

    def mostrar_profissionais(e):
        resultado.controls.clear()

        dados = consultas_por_profissional()

        resultado.controls.append(ft.Text("Consultas por Profissional"))

        for codigo, quantidade in dados.items():
            resultado.controls.append(
                ft.Text(f"Profissional {codigo}: {quantidade}")
            )

        page.update()

    def mostrar_tipos(e):
        resultado.controls.clear()

        dados = consultas_por_tipo()

        resultado.controls.append(ft.Text("Consultas por Tipo"))

        for tipo, quantidade in dados.items():
            resultado.controls.append(
                ft.Text(f"{tipo}: {quantidade}")
            )

        page.update()

    def mostrar_faturamento(e):
        resultado.controls.clear()

        total = faturamento_total()

        resultado.controls.append(
            ft.Text(f"Faturamento Total: R$ {total:.2f}")
        )

        page.update()

    page.add(
        ft.Text(
            "RELATÓRIOS",
            size=24,
            weight=ft.FontWeight.BOLD
        ),

        ft.ElevatedButton(
            "Consultas por Profissional",
            on_click=mostrar_profissionais
        ),

        ft.ElevatedButton(
            "Consultas por Tipo",
            on_click=mostrar_tipos
        ),

        ft.Divider(),

        resultado,

        ft.ElevatedButton(
            "Voltar",
            on_click=lambda e: voltar_para(page)
        )
    )