import requests

def get_request(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(response.content)
    else:
        print("Erro ao buscar dados da url")

get_request("https://dadosabertos.camara.leg.br/api/v2/deputados")