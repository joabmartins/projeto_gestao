import api_dados_abertos as api
import mysql_queries

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def cadastrar_parlamentares():
     data = api.get_parlamentares()
     #data = data[:10]
     count = 1
     size = len(data)

     for parlamentar in data:
          print(f"salvando {count} de {size}")
          total_gastos = get_total_despesas(parlamentar['id'])
          print(f"total de gastos: {total_gastos}")
          mysql_queries.inserir_parlamentar(parlamentar, total_gastos)
          count+=1

def get_total_despesas(matricula):
     despesas_list = api.get_despesas(matricula)
     if despesas_list is None:
          print(f"Erro ao retornar dados do parlamentar {matricula}")
          return
     total_gastos = 0
     for despesa in despesas_list:
          total_gastos += despesa.get("valorLiquido", 0)
     return total_gastos

def apresentacao_dados():
     gasto_partidos = mysql_queries.get_all_gastos_by_partido()
     gasto_uf = mysql_queries.get_all_gastos_by_uf()
     print(gasto_partidos)
     print(gasto_uf)

     # Converte a lista em um DataFrame do Pandas
     df = pd.DataFrame(gasto_partidos, columns=['partido', 'gastos_totais'])

     # Cria o gráfico de barras (histograma)
     plt.figure(figsize=(10, 6)) # Opcional: define o tamanho da figura para melhor visualização
     sns.barplot(x='partido', y='gastos_totais', data=df)

     # Adiciona títulos e rótulos
     plt.title('Gastos Totais por Partido')
     plt.xlabel('Partido')
     plt.ylabel('Gastos Totais (R$)')

     # Rotaciona os rótulos do eixo X para evitar sobreposição
     plt.xticks(rotation=45, ha='right')

     # Exibe o gráfico
     plt.tight_layout() # Ajusta o layout para evitar que os rótulos se cortem
     plt.show()

# executar apenas uma vez
# mysql_queries.criar_tabela_parlamentar()
# cadastrar_parlamentares()

apresentacao_dados()