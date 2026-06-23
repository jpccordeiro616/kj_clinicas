import flet as ft
from funcoes.profissionais import (
    cadastrar_profissional,
    buscar_profissional,
    listar_profissionais
)


def tela_profissionais(page: ft.Page, voltar_para):
    page.clean()

    nome = ft.TextField(label="Nome")
    especialidade = ft.TextField(label="Especialidade")
    codigo = ft.TextField(label="Código")

    codigo_busca = ft.TextField(label="Código para busca")

    resultado = ft.Column()

    def salvar(e):
        ok = cadastrar_profissional(
            nome.value,
            especialidade.value,
            codigo.value
        )

        resultado.controls.clear()

        if ok:
            resultado.controls.append(ft.Text("Profissional cadastrado com sucesso!", color="green"))

            nome.value = ""
            especialidade.value = ""
            codigo.value = ""
        else:
            resultado.controls.append(ft.Text("Código já cadastrado!", color="red"))

        page.update()


    def buscar(e):
        resultado.controls.clear()

        prof = buscar_profissional(codigo_busca.value)

        if prof:
            resultado.controls.append(
                ft.Text(
                    f"{prof['nome']} | {prof['especialidade']} | {prof['codigo']}"
                )
            )
        else:
            resultado.controls.append(ft.Text("Profissional não encontrado"))

        page.update()

    def listar(e):
        resultado.controls.clear()

        for p in listar_profissionais():
            resultado.controls.append(
                ft.Text(
                    f"{p['nome']} | {p['especialidade']} | {p['codigo']}"
                )
            )

        page.update()

    page.add(
        ft.Text("PROFISSIONAIS", size=24, weight=ft.FontWeight.BOLD),

        nome,
        especialidade,
        codigo,

        ft.ElevatedButton("Cadastrar", on_click=salvar),

        ft.Divider(),

        codigo_busca,
        ft.Row([
            ft.ElevatedButton("Buscar", on_click=buscar),
            ft.ElevatedButton("Listar", on_click=listar),
        ]),

        resultado,

        ft.ElevatedButton("Voltar", on_click=lambda e: voltar_para(page))
    )