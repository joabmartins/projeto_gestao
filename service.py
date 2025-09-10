import database_queries as query
import api_dados_abertos as api
import json

def cadastrar_deputados():
    data = api.get_deputados()
    count = 1
    size = len(data)

    for deputado in data:
        print(f"salvando{count} de {size}:{deputado['nome']}")
        total_gastos = get_total_despesas(deputado['id'])
        print(f"O deputado {deputado['nome']} teve gasto total de {total_gastos}")
        query.inserir_deputado(deputado, total_gastos)
        count+=1

def get_total_despesas(id):
    data = api.get_despesas(id)
    total_gastos = 0
    for despesa in data:
        print(f"Salvando despesa {despesa.get("valorLiquido", 0)} de {id}")
        total_gastos += despesa.get("valorLiquido", 0)
    return total_gastos
# comandos a serem executados apenas uma vez
# query.criar_tabela_deputados()
cadastrar_deputados()