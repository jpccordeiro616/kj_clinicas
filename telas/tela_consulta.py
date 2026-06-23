import flet as ft
from funcoes.consultas import (
    agendar_consulta,
    listar_consultas,
    cancelar_consulta,
    HORARIOS
)


def tela_consultas(page: ft.Page, voltar_para):
    page.clean()

    paciente = ft.TextField(label="CPF do Paciente")
    profissional = ft.TextField(label="Código do Profissional")
    data = ft.TextField(label="Data (dd/mm/aaaa)")
    horario = ft.Dropdown(
        label="Horário",
        options=[ft.dropdown.Option(h) for h in HORARIOS]
    )
    tipo = ft.Dropdown(
        label="Tipo",
        options=[
            ft.dropdown.Option("Particular"),
            ft.dropdown.Option("Convênio"),
            ft.dropdown.Option("Retorno"),
        ]
    )

    cancelar_paciente = ft.TextField(label="CPF para cancelar")
    cancelar_data = ft.TextField(label="Data cancelar")
    cancelar_horario = ft.TextField(label="Horário cancelar")

    resultado = ft.Column()

    def agendar(e):
        resultado.controls.clear()

        resp = agendar_consulta(
            paciente.value,
            profissional.value,
            data.value,
            horario.value,
            tipo.value
        )

        resultado.controls.append(ft.Text(resp))

        page.update()

    def listar(e):
        resultado.controls.clear()

        for c in listar_consultas():
            resultado.controls.append(
                ft.Text(
                    f"{c['data']} {c['horario']} | Pac: {c['paciente']} | Prof: {c['profissional']} | {c['tipo']} | R${c['valor']}"
                )
            )

        page.update()

    def cancelar(e):
        resultado.controls.clear()

        cancelar_consulta(
            cancelar_paciente.value,
            cancelar_data.value,
            cancelar_horario.value
        )

        resultado.controls.append(ft.Text("Consulta cancelada (se existia)"))
        page.update()

    page.add(
        ft.Text("CONSULTAS", size=24, weight=ft.FontWeight.BOLD),

        paciente,
        profissional,
        data,
        horario,
        tipo,

        ft.ElevatedButton("Agendar", on_click=agendar),

        ft.Divider(),

        ft.ElevatedButton("Listar Consultas", on_click=listar),

        ft.Divider(),

        cancelar_paciente,
        cancelar_data,
        cancelar_horario,

        ft.ElevatedButton("Cancelar Consulta", on_click=cancelar),

        resultado,

        ft.ElevatedButton("Voltar", on_click=lambda e: voltar_para(page))
    )