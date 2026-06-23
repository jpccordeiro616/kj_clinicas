def cadastrar_paciente(nome, cpf, telefone, cep, rua, bairro, cidade):
    with open("pacientes.txt", "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(",")
            if dados[1] == cpf:
                return False
    with open("pacientes.txt", "a") as arquivo:
        arquivo.write(f"{nome},{cpf},{telefone},{cep},{rua},{bairro},{cidade}\n")
    return True

def buscar_pacientes(cpf):
    with open("pacientes.txt", "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(",")
            if dados[1] == cpf:
                paciente = {
                    "nome": dados[0],
                    "cpf": dados[1],
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
