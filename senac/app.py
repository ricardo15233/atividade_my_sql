import mysql.connector
from alunos import Aluno


conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="senac",
    database="cadastro",
    port = 3307
)


aluno = Aluno(conexao)


while True:

    print("\n===== MENU PRINCIPAL =====")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Atualizar curso do aluno")
    print("4 - Excluir aluno")
    print("5 - Listar cursos")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        aluno.cadastrar()

    elif opcao == "2":
        aluno.listar()

    elif opcao == "3":
        aluno.atualizar()

    elif opcao == "4":
        aluno.excluir()

    elif opcao == "5":
        aluno.listar_cursos()

    elif opcao == "6":
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")


aluno.cursor.close()
conexao.close()