import flet as ft
from funcoes.consultas import HORARIOS


def limpar(resultado):
    resultado.controls.clear()


# Consultas por profissional
def mostrar_profissionais(resultado):
    limpar(resultado)

    profissionais = {}

    with open("consultas.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(",")

            if len(dados) < 6:
                continue

            profissional = dados[1]

            if profissional not in profissionais:
                profissionais[profissional] = 0

            profissionais[profissional] += 1

    for prof, total in profissionais.items():
        resultado.controls.append(
            ft.Text(
                f"Profissional {prof}: {total} consulta(s)"
            )
        )

    resultado.update()


# Consultas por tipo
def mostrar_tipos(resultado):
    limpar(resultado)

    tipos = {
        "Particular": 0,
        "Convênio": 0,
        "Retorno": 0
    }

    with open("consultas.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(",")

            if len(dados) < 6:
                continue

            tipo = dados[4]

            if tipo in tipos:
                tipos[tipo] += 1

    for tipo, total in tipos.items():
        resultado.controls.append(
            ft.Text(
                f"{tipo}: {total}"
            )
        )

    resultado.update()


# Faturamento previsto
def mostrar_faturamento(resultado):
    limpar(resultado)

    total = 0

    with open("consultas.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(",")

            if len(dados) < 6:
                continue

            total += float(dados[5])

    resultado.controls.append(
        ft.Text(
            f"Faturamento previsto: R$ {total:.2f}"
        )
    )

    resultado.update()


# Consultas por bairro
def mostrar_bairros(resultado):
    limpar(resultado)

    bairros = {}

    with open("pacientes.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(",")

            if len(dados) < 7:
                continue

            bairro = dados[5]

            if bairro not in bairros:
                bairros[bairro] = 0

            bairros[bairro] += 1

    for bairro, total in bairros.items():
        resultado.controls.append(
            ft.Text(
                f"{bairro}: {total} paciente(s)"
            )
        )

    resultado.update()


# Horários ocupados e livres
def mostrar_horarios(resultado):
    limpar(resultado)

    ocupados = []

    with open("consultas.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(",")

            if len(dados) < 6:
                continue

            ocupados.append(dados[3])

    resultado.controls.append(
        ft.Text(
            "Horários ocupados:",
            weight=ft.FontWeight.BOLD
        )
    )

    for h in ocupados:
        resultado.controls.append(
            ft.Text(h)
        )

    resultado.controls.append(
        ft.Divider()
    )

    resultado.controls.append(
        ft.Text(
            "Horários livres:",
            weight=ft.FontWeight.BOLD
        )
    )

    for h in HORARIOS:
        if h not in ocupados:
            resultado.controls.append(
                ft.Text(h)
            )

    resultado.update()