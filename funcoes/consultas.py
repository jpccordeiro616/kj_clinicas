from funcoes.pacientes import buscar_pacientes
from funcoes.profissionais import buscar_profissional


HORARIOS = ("08:00", "09:00", "10:00", "11:00", "14:00", "15:00", "16:00")


def consulta_ocupada(profissional, data, horario):
    with open("consultas.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(",")

            if len(dados) < 6:
                continue

            if dados[2] == profissional and dados[3] == data and dados[4] == horario:
                return True

    return False


def paciente_existe(cpf):
    return buscar_pacientes(cpf) is not None


def profissional_existe(codigo):
    return buscar_profissional(codigo) is not None


def calcular_valor(tipo, dias_retorno=0):
    if tipo == "Particular":
        return 180

    elif tipo == "Convênio":
        return 80

    elif tipo == "Retorno":
        if dias_retorno <= 30:
            return 0
        return 100

    return 0


def agendar_consulta(paciente, profissional, data, horario, tipo, dias_retorno=0):
    if not paciente_existe(paciente):
        return "Paciente não cadastrado"

    if not profissional_existe(profissional):
        return "Profissional não cadastrado"

    if consulta_ocupada(profissional, data, horario):
        return "Horário ocupado"

    valor = calcular_valor(tipo, dias_retorno)

    with open("consultas.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(
            f"{paciente},{profissional},{data},{horario},{tipo},{valor}\n"
        )

    return "OK"


def listar_consultas():
    lista = []

    with open("consultas.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(",")

            if len(dados) < 6:
                continue

            lista.append({
                "paciente": dados[0],
                "profissional": dados[1],
                "data": dados[2],
                "horario": dados[3],
                "tipo": dados[4],
                "valor": dados[5]
            })

    return lista


def cancelar_consulta(paciente, data, horario):
    linhas = []

    with open("consultas.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(",")

            if len(dados) < 6:
                continue

            if not (dados[0] == paciente and dados[2] == data and dados[3] == horario):
                linhas.append(linha)

    with open("consultas.txt", "w", encoding="utf-8") as arquivo:
        for l in linhas:
            arquivo.write(l)