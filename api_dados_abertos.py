import requests
import json

def get_request(url):
    response = requests.get(url)
    if response.status_code == 200:
        #print(json.dumps(response.json(), indent=2))
        return response.json()
    else:
        print("Erro ao buscar dados da url")
        return None

def get_deputados():
    deputados_url = 'https://dadosabertos.camara.leg.br/api/v2/deputados'
    data = get_request(deputados_url)
    return data.get("dados")

def get_despesas(id_deputado):
    despesas_url = f'https://dadosabertos.camara.leg.br/api/v2/deputados/{id_deputado}/despesas'
    data = get_request(despesas_url)
    return data.get("dados")

#https://codeshare.io/5R86YO
