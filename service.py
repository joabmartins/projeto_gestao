import database_queries as query
import api_dados_abertos as api

#query.criar_tabela_deputados()
#comandos a serem executados apenas uma vez

def cadastrar_deputados():
    data = api.get_deputados()
   # data = data[:10] quando quer salvar apenas os 10 primeiros
    count = 1
    size = len(data) #10

    for deputado in data:
        print(f"Salvando {count} de {size}: {deputado['nome']}")
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

cadastrar_deputados()