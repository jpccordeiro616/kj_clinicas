import flet as ft
from funcoes.pacientes import cadastrar_paciente, buscar_pacientes, listar_pacientes
from utils.viacep import buscar_cep

def tela_pacientes(page: ft.Page, voltar_para):
    page.clean()
    def voltar(e):
        voltar_para(page)

    nome = ft.TextField(label="Nome")
    cpf = ft.TextField(label="CPF")
    telefone = ft.TextField(label="Telefone")
    cep = ft.TextField(label="CEP")
    rua = ft.TextField(label="Rua")
    bairro = ft.TextField(label="Bairro")
    cidade = ft.TextField(label="Cidade")

    cpf_busca = ft.TextField(label="CPF para busca")
    resultado = ft.Column()

    def preencher_endereco(e):
        from utils.viacep import buscar_cep
        endereco = buscar_cep(cep.value)

        dados = buscar_cep(cep.value)
        if dados:
            rua.value = dados.get("rua", "")
            bairro.value = dados.get("bairro", "")
            cidade.value = dados.get("cidade", "")
        else:
            resultado.controls.clear()
            resultado.controls.append(ft.Text("CEP não encontrado."))
            
        page.update()
    cep.on_blur = preencher_endereco
    def salvar(e):
        cadastro = cadastrar_paciente(
            nome.value,
            cpf.value,
            telefone.value,
            cep.value,
            rua.value,
            bairro.value,
            cidade.value)
        
        resultado.controls.clear()

        if cadastro:
            resultado.controls.append(ft.Text("Paciente cadastrado com sucesso!"))
            nome.value = ""
            cpf.value = ""
            telefone.value = ""
            cep.value = ""
            rua.value = ""
            bairro.value = ""
            cidade.value = ""
        else:
            resultado.controls.append(ft.Text("CPF já cadastrado."))

        page.update()

    def buscar(e):
        resultado.controls.clear()
        paciente = buscar_pacientes(cpf_busca.value)
        
        if paciente:
            resultado.controls.append(
                ft.Text(f"Nome: {paciente['nome']}, CPF: {paciente['cpf']}, Telefone: {paciente['telefone']}, CEP: {paciente['cep']}, Rua: {paciente['rua']}, Bairro: {paciente['bairro']}, Cidade: {paciente['cidade']}")
            )
        else:
            resultado.controls.append(ft.Text("Paciente não encontrado."))
        page.update()

    def listar(e):
        resultado.controls.clear()
        pacientes = listar_pacientes()

        for p in pacientes:
            resultado.controls.append(
                ft.Text(f"Nome: {p[0]}, CPF: {p[1]}, Telefone: {p[2]}, CEP: {p[3]}, Rua: {p[4]}, Bairro: {p[5]}, Cidade: {p[6]}")
            )
        page.update()

    page.add(
        ft.Text("PACIENTES", size=24, weight=ft.FontWeight.BOLD),
        nome,
        cpf,
        telefone,
        cep,
        rua,
        bairro,
        cidade,
        ft.ElevatedButton(
            "Cadastrar",
            on_click=salvar
        ),
        ft.Divider(),
        cpf_busca,
        ft.Row([
            ft.ElevatedButton("Buscar", on_click=buscar),
            ft.ElevatedButton("Listar", on_click=listar),
            ft.ElevatedButton("Voltar", on_click=voltar)
        ]),
        resultado

    )