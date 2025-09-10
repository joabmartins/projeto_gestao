import database_connection as db_conn
import mysql.connector
 
def executar_query( sql, dados ):
    conn = db_conn.conectar()
    if conn is None:
        print( "conexão vazia" )
        return
    resultados = None #alteração 2
    try:
        cur = conn.cursor()
        cur.execute( sql, dados )
        resultados = cur.fetchall() #alteração 1
        print("Comando SQL executado com sucesso!")
    except mysql.connector.Error as error:
        print(f"Erro ao executar comando: { error }")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def consultar_query( sql, dados ):
    conn = db_conn.conectar()
    if conn is None:
        print( "conexão vazia" )
        return resultados #alteração 3
    
    try:
        cur = conn.cursor()
        cur.execute( sql, dados )
        conn.commit()
        print("Comando SQL executado com sucesso!")
    except mysql.connector.Error as error:
        print(f"Erro ao executar comando: { error }")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def criar_tabela_deputados():
    sql = """
    CREATE TABLE IF NOT EXISTS deputado(
        id INT PRIMARY KEY AUTO_INCREMENT,
        mat_deputado INT UNIQUE NOT NULL,
        nome VARCHAR(100) NOT NULL,
        partido VARCHAR(100) NOT NULL,
        uf VARCHAR(4) NOT NULL,
        total_gastos NUMERIC(10, 2)
    );"""
    executar_query(sql)

def inserir_deputado(deputado, total_gastos):
    matricula = deputado[ 'id' ]
    nome = deputado[ 'nome' ]
    partido = deputado[ 'siglaPartido' ]
    uf = deputado[ 'siglaUf' ]

    sql = """
        INSERT IGNORE INTO deputados (
        mat_deputado,
        nome,
        partido,
        uf,
        total_gastos
        ) VALUES ( %s, %s, %s, %s, %s )
    """
    dados = ( matricula, nome, partido, uf, total_gastos )
    executar_query( sql, dados )

def get_all_gastos_by_partido():
    sql = '''
    SELECT partido, SUM( total_gastos) AS gastos_totais
    FROM deputado
    GROUP BY partido;
'''
    consultar_query(sql)