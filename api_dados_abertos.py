import requests
import json

def get_request(url):
    response = requests.get(url)
    if response.status_code == 200:
        #print(json.dumps(response.json(), indent=2))
        return response.json()
    else:
        print(f"erro ao buscar dados da url {response.status_code}")

def get_deputados():
    deputados_url = 'https://dadosabertos.camara.leg.br/api/v2/deputados'
    data = get_request(deputados_url)
    return data.get("dados")
#get_request('https://dadosabertos.camara.leg.br/api/v2/deputados')

def get_despesas(id_deputados):
    print(id_deputados)
    despesas_url = f"https://dadosabertos.camara.leg.br/api/v2/deputados/{id_deputados}/despesas"
    data = get_request(despesas_url)
    return data.get("dados")