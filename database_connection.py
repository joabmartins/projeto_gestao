import mysql.connector

DB_CONFIG = {
    'host': 'localhost',
    'port': 3307,
    'database': 'projeto_db',
    'user': 'root',
    'password': 'admin'
}

def conectar():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        print("Conexao estabelecida com sucesso!")
        conn.close()
    except mysql.connector.Error as error:
        print(f"Erro ao conectar ao banco de dados: {error}")
        
    
conectar()