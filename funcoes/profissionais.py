def codigo_existe(codigo):
    try:
        with open("profissionais.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(",")
                if len(dados) > 1 and dados[2] == codigo:
                    return True
    except FileNotFoundError:
        pass

    return False


def cadastrar_profissional(nome, especialidade, codigo):
    if codigo_existe(codigo):
        return False

    with open("profissionais.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome},{especialidade},{codigo}\n")

    return True


def listar_profissionais():
    lista = []

    try:
        with open("profissionais.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(",")

                if len(dados) < 3:
                    continue

                lista.append({
                    "nome": dados[0],
                    "especialidade": dados[1],
                    "codigo": dados[2]
                })
    except FileNotFoundError:
        pass

    return lista


def buscar_profissional(codigo):
    try:
        with open("profissionais.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(",")

                if len(dados) < 3:
                    continue

                if dados[2] == codigo:
                    return {
                        "nome": dados[0],
                        "especialidade": dados[1],
                        "codigo": dados[2]
                    }
    except FileNotFoundError:
        pass

    return None