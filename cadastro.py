import flet as ft

def main(page: ft.Page):
    page.title = "Cadastro de Usuário"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Criar os campos de entrada
    nome_input = ft.TextField(label="Nome", width=300)
    email_input = ft.TextField(label="Email", width=300)
    senha_input = ft.TextField(label="Senha", width=300, password=True)

    # Criar o botão de cadastro
    cadastrar_button = ft.ElevatedButton(text="Cadastrar", on_click=lambda e: cadastrar_usuario(nome_input.value, email_input.value, senha_input.value))

    # Adicionar os componentes à página
    page.add(
        ft.Column(
            [
                nome_input,
                email_input,
                senha_input,
                cadastrar_button
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )