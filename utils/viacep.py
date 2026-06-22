import requests

url = f"https://viacep.com.br/ws/<CEP>/json/"

response = requests.get(url)
dados = response.json()
