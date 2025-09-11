import database_queries as query
import api_dados_abertos as api
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def cadastrar_deputados():
    data = api.get_deputados()
    #data = data[:10]
    count = 1
    size = len(data)

    for deputado in data:
        print(f"salvando {count} de {size}: {deputado['nome']}")
        total_gastos = get_total_despesas(deputado['id'])
        print(f"O deputado {deputado['nome']} teve gasto total de {total_gastos})")
        query.inserir_deputado(deputado, total_gastos)
        count+=1
        
def get_total_despesas(id):
    data = api.get_despesas(id)
    total_gastos = 0
    for despesa in data:
        print(f"Salvando despesas {despesa.get("valorLiquido", 0)} de {id}")
        total_gastos += despesa.get("valorLiquido", 0)
    return total_gastos

# comandos a serem executados apenas uma vez
#query.criar_tabela_deputados()
#cadastrar_deputados()

def apresentar_dados():
    gastos_partido = query.get_all_gastos_by_partido()
    gastos_uf = query.get_all_gastos_by_uf()
    df = pd.DataFrame(gastos_partido, columns=['partido', 'gastos_totais'])
    df_uf = pd.DataFrame(gastos_uf ,columns=['uf', 'gastos_totais'])

    # plt.figure(figsize=(10, 6))
    fig, (partido_gf, uf_gf) = plt.subplots(1, 2, figsize=(20,4))
    partido_gf = sns.barplot(x='partido', y='gastos_totais', data=df, ax=partido_gf)
    uf_gf = sns.barplot(x='uf', y='gastos_totais', data=df_uf, ax=uf_gf)
    partido_gf.tick_params(axis='x', rotation=45)
    uf_gf.tick_params(axis='x', rotation=45)
    #exibir o gráfico
    plt.tight_layout()
    plt.show()

apresentar_dados()