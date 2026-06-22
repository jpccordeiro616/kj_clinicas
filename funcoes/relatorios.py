def consultas_por_profissional():
    resultados = {}
    with open("consultas.txt", "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(",")
            codigo = dados[1]
            if codigo in resultados:
                resultados[codigo] += 1
            else:
                resultados[codigo] = 1
    return resultados

def consultas_por_tipo():
    resultados = {}
    with open("consultas.txt", "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")
            tipo = dados[4]
            if tipo in resultados:
                resultados[tipo] += 1
            else:
                resultados[tipo] = 1
    return resultados

def faturamento_total():
    total = 0
    with open("consultas.txt", "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")
            valor = float(dados[5])
            total += valor
    return total