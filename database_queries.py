import database_connection as db_conn
import mysql.connector

def executar_query(sql):
    conn = db_conn.conectar()
    if conn is None:
        print("conexão vazia")
        return
    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("Comando SQL executado com sucesso!")
    except mysql.connector.Error as error:
        print(f"Erro ao executar comando: {error}")
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