import flet as ft

def main(page: ft.Page):
    page.title = "Cadastro de Usuário"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def cadastrar(e):
        nome = nome_input.value
        email = email_input.value
        senha = senha_input.value
        # Aqui você pode adicionar a lógica para salvar os dados do usuário
        print(f"Nome: {nome}, Email: {email}, Senha: {senha}")
        nome_input.value = ""
        email_input.value = ""
        senha_input.value = ""
        page.update()

    nome_input = ft.TextField(label="Nome", width=300)
    email_input = ft.TextField(label="Email", width=300)
    senha_input = ft.TextField(label="Senha", width=300, password=True)
    cadastrar_button = ft.ElevatedButton(text="Cadastrar", on_click=cadastrar)

    page.add(nome_input, email_input, senha_input, cadastrar_button)
    
ft.run(main)