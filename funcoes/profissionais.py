def cadastrar_profissional(codigo, nome, especialidade):
    with open("profissionais.txt", "a") as arquivo:
        arquivo.write(f"{codigo},{nome},{especialidade}\n")

def buscar_profissional(codigo):
    with open("profissionais.txt", "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(",")
            if dados[0] == codigo:
                profissional = {
                    "codigo": dados[0],
                    "nome": dados[1],
                    "especialidade": dados[2]
                }
                return profissional
    return None

