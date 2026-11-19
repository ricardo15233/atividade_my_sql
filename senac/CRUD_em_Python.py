import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    database='banco_109',
)
cursor = conexao.cursor()

# CRUD
# nome_produto = "todynho"
# comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# conexao.commit() # edita o banco de dados   


#CREATE
'''nome_produto = "Fanta Laranaja"

valor = 12
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
conexao.commit() # edita o banco de dados'''


# READ
comando = f'SELECT * FROM pessoas'
cursor.execute(comando)
resultado = cursor.fetchall() # ler o banco de dados
print(resultado)


# UPDATE
# nome_produto = "todynho"
# valor = 6
# comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# conexao.commit() # edita o banco de dados

# DELETE
# nome_produto = "todynho"
# comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# conexao.commit() # edita o banco de dados

cursor.close()
conexao.close()