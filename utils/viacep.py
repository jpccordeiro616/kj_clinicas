import requests

def buscar_cep(cep):
    cep = cep.replace("-", "").replace(".", "")

    response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")

    if response.status_code == 200:
        dados = response.json()

        if "erro" in dados:
            return None

        return {
            "rua": dados.get("logradouro"),
            "bairro": dados.get("bairro"),
            "cidade": dados.get("localidade"),
            "estado": dados.get("uf")
        }

    return None