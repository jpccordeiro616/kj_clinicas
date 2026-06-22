from pacientes import buscar_pacientes
from profissionais import buscar_profissional

def agendar_consultas(cpf, codigo, data, horario, tipo, valor):
    with open("consultas.txt", "a") as arquivo:
        arquivo.write(f"{cpf},{codigo},{data},{horario},{tipo},{valor}\n")

def calcular_valor(tipo):
    if tipo == "Particular":
        return 180
    elif tipo == "Convênio":
        return 80
    elif tipo == "Retorno":
        return 100
    
def horario_ocupado(codigo_profissional, data, horario):
    with open("consultas.txt", "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(",")
            if dados[1] == codigo_profissional and dados[2] == data and dados[3] == horario:
                return True
    return False

def agendar_consulta(cpf, codigo, data, horario, tipo):
    paciente = buscar_pacientes(cpf)

    if paciente == None:
        print("Paciente não encontrado.")
        return
    
    profissionais = buscar_profissional(codigo)

    if profissionais == None:
        print("Profissional não encontrado.")
        return
    
    if horario_ocupado(codigo, data, horario):
        print("Horário ocupado.")
        return
    
    valor = calcular_valor(tipo)
    
    with open("consultas.txt", "a") as arquivo:
        arquivo.write(f"{cpf},{codigo},{data},{horario},{tipo},{valor}\n")

    return "Consulta agendada com sucesso."

def cancelar_consulta(cpf, codigo, data, horario):
    consultas = []
    with open("consultas.txt", "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(",")
            if not (dados[0] == cpf and dados[1] == codigo and dados[2] == data and dados[3] == horario):
                consultas.append(linha)
    
    with open("consultas.txt", "w") as arquivo:
        for consulta in consultas:
            arquivo.write(consulta)

    return "Consulta cancelada com sucesso."

def listar_consultas():
    consultas = []
    with open("consultas.txt", "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(",")
            consultas.append(dados)
    return consultas