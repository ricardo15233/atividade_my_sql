
import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    port=3307,
    user="root",
    password="senac",
    database="cadastro"
)

if conexao.is_connected():
    print("Conectado ao banco de dados!")




