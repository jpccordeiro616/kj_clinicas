def cadastrar_paciente(nome, cpf, telefone, cep):
    with open("pacientes.txt", "a") as arquivo:
        arquivo.write(f"{nome},{cpf},{telefone},{cep}\n")

def buscar_pacientes(cpf):
    with open("pacientes.txt", "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(",")
            if dados[0] == cpf:
                paciente = {
                    "cpf": dados[0],
                    "nome": dados[1],
                    "telefone": dados[2],
                    "cep": dados[3],
                    "rua": dados[4],
                    "bairro": dados[5],
                    "cidade": dados[6]
                }
                return paciente
    return None

def listar_pacientes():
    pacientes = []
    with open("pacientes.txt", "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(",")
            pacientes.append(dados)
    return pacientes
