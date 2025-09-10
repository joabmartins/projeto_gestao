import mysql.connector

DB_CONFIG = {
    "host": 'localhost',
    'port': 3307,
    'user' : 'root',
    'database': 'projeto_db',
    'password' : 'admin'
}

def conectar():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        print("conexão estabelecida com sucesso!!")
        return conn
    except mysql.connector.Error as error:
        print(f"Erro ao conectar ao banco de dados: {error}")
        return None
    
conectar()