# TRUNCATE TABLE projeto_db.parlamentar;
# SELECT id, mat_parlamentar, nome, partido, UF, total_gastos
# FROM projeto_db.parlamentar;

# SELECT uf, SUM(total_gastos) AS gastos_totais
# FROM projeto_db.parlamentar
# GROUP BY uf;

import mysql.connector
import mysql_connection as db_conn

def executar_query(sql, dados=None):

     conn = db_conn.conectar()
     if conn is None:
          print("conexão vazia.")
          return
     
     cur = None
     try:
          cur = conn.cursor()
          print("Executando o comando SQL...")
          cur.execute(sql, dados)
          conn.commit() # <<< ESSA LINHA É CRUCIAL! Confirma as alterações no banco de dados.
          print("Comando SQL executado com sucesso e transação confirmada.")
     except mysql.connector.Error as error:
          print(f"Erro ao executar comando: {error}")
          # Se ocorrer um erro, é uma boa prática fazer um rollback
          if conn:
               conn.rollback()
     finally:
          # Garante que o cursor e a conexão sejam fechados
          if cur:
               cur.close()
          if conn and conn.is_connected():
               conn.close()

def consultar(sql):
     conn = db_conn.conectar()
     if conn is None:
          print("conexão vazia.")
          return
     
     cur = None
     resultados = None
     try:
          cur = conn.cursor()
          cur.execute(sql)
          resultados = cur.fetchall()
     except mysql.connector.Error as error:
          print(f"Erro ao executar comando: {error}")
          # Se ocorrer um erro, é uma boa prática fazer um rollback
          if conn:
               conn.rollback()
     finally:
          # Garante que o cursor e a conexão sejam fechados
          if cur:
               cur.close()
          if conn and conn.is_connected():
               conn.close()
     return resultados

def criar_tabela_parlamentar():
     """Define o SQL para criar a tabela parlamentar e chama create_table."""
     sql = """
     CREATE TABLE IF NOT EXISTS parlamentar (
          id INT PRIMARY KEY AUTO_INCREMENT,
          mat_parlamentar INT UNIQUE NOT NULL,
          nome VARCHAR(100) NOT NULL,
          partido VARCHAR(100) NOT NULL,
          UF VARCHAR(4) NOT NULL,
          total_gastos NUMERIC(10, 2)
     );"""
     executar_query(sql)

def inserir_parlamentar(parlamentar, total_gastos):

     matricula = parlamentar['id']
     nome = parlamentar['nome']
     partido = parlamentar['siglaPartido']
     uf = parlamentar['siglaUf']

     sql = """
          INSERT IGNORE INTO parlamentar (
          mat_parlamentar,
          nome,
          partido,
          uf,
          total_gastos
          ) VALUES (%s, %s, %s, %s, %s)
     """

     print(f"cadastrando parlamentar {nome} com gasto {total_gastos}")

     # Cria uma tupla com os dados na ordem correta
     dados = (matricula, nome, partido, uf, total_gastos)

     # Chama a função de execução, passando o SQL e os dados
     executar_query(sql, dados)

def get_all_gastos_by_partido():
     sql = """
          SELECT partido, SUM(total_gastos) AS gastos_totais
          FROM parlamentar
          GROUP BY partido;
     """
     return consultar(sql)

def get_all_gastos_by_uf():
     sql = """
          SELECT uf, SUM(total_gastos) AS gastos_totais
          FROM parlamentar
          GROUP BY uf;
     """
     return consultar(sql)