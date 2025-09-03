import requests
import json

def get_request(url):
     response = requests.get(url)
     if response.status_code == 200:
          print("Dados JSON recebidos com sucesso!")
          return response.json()
          # print(len(parlamentares_list))
          # print(json.dumps(parlamentares_list[0:5], indent=2))
     else:
          print(f"Erro ao buscar os dados de {url}: {response.status_code}")
          return None

def get_parlamentares():
     '''
     {
     "id": 220560,
     "uri": "https://dadosabertos.camara.leg.br/api/v2/deputados/220560",
     "nome": "Thiago de Joaldo",
     "siglaPartido": "PP",
     "uriPartido": "https://dadosabertos.camara.leg.br/api/v2/partidos/37903",
     "siglaUf": "SE",
     "idLegislatura": 57,
     "urlFoto": "https://www.camara.leg.br/internet/deputado/bandep/220560.jpg",
     "email": "dep.thiagodejoaldo@camara.leg.br"
     },
     '''
     parlamentares_url = 'https://dadosabertos.camara.leg.br/api/v2/deputados'
     data = get_request(parlamentares_url)
     return data.get("dados")

def get_despesas(id_parlamentar):
     '''
     {
     "ano": 2025,
     "mes": 6,
     "tipoDespesa": "MANUTEN\u00c7\u00c3O DE ESCRIT\u00d3RIO DE APOIO \u00c0 ATIVIDADE PARLAMENTAR",
     "codDocumento": 7933669,
     "tipoDocumento": "Nota Fiscal Eletr\u00f4nica",
     "codTipoDocumento": 4,
     "dataDocumento": "2025-06-17T00:00:00",
     "numDocumento": "6654",
     "valorDocumento": 394.4,
     "urlDocumento": "http://www.camara.leg.br/cota-parlamentar/nota-fiscal-eletronica?ideDocumentoFiscal=7933669",
     "nomeFornecedor": "WMS COMERCIO DE ARTIGOS DE PAPELARIA LTDA",
     "cnpjCpfFornecedor": "12132854000100",
     "valorLiquido": 394.4,
     "valorGlosa": 0.0,
     "numRessarcimento": "",
     "codLote": 2146432,
     "parcela": 0
     },
     '''
     # despesas_url = 'https://dadosabertos.camara.leg.br/api/v2/deputados/220560/despesas'
     despesas_url = f'https://dadosabertos.camara.leg.br/api/v2/deputados/{id_parlamentar}/despesas'
     data = get_request(despesas_url)
     return data.get("dados")