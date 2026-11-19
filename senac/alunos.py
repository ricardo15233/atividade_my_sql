
class Aluno:

    def __init__(self, conexao):
        self.conexao = conexao
        self.cursor = conexao.cursor()

    def coletar_dados(self):

        nome = input("Digite o nome: ")
        profissao = input("Digite a profissão: ")
        nascimento = input("Data de nascimento (AAAA-MM-DD): ")
        sexo = input("Sexo (M/F): ").upper()

        peso = float(input("Digite o peso: ").replace(",", "."))
        altura = float(input("Digite a altura: ").replace(",", "."))

        nacionalidade = input("Digite a nacionalidade: ")
        curso = int(input("Digite o ID do curso preferido: "))

        return (
            nome, profissao, nascimento, sexo,
            peso, altura, nacionalidade, curso
        )

    def cadastrar(self):

        valores = self.coletar_dados()

        sql = """
        INSERT INTO alunos
        (nome, profissao, nascimento, sexo, peso,
        altura, nacionalidade, cursopreferido)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        self.cursor.execute(sql, valores)
        self.conexao.commit()

        print("Aluno cadastrado com sucesso!")


    def listar(self):

        sql = """
        SELECT
            alunos.id,
            alunos.nome,
            alunos.profissao,
            alunos.nascimento,
            alunos.sexo,
            alunos.peso,
            alunos.altura,
            alunos.nacionalidade,
            cursos.nome
        FROM alunos
        INNER JOIN cursos
        ON alunos.cursopreferido = cursos.idcurso
        """

        self.cursor.execute(sql)

        resultado = self.cursor.fetchall()

        if resultado:
            for aluno in resultado:
                print("------------------------")
                print("ID:", aluno[0])
                print("Nome:", aluno[1])
                print("Profissão:", aluno[2])
                print("Nascimento:", aluno[3])
                print("Sexo:", aluno[4])
                print("Peso:", aluno[5])
                print("Altura:", aluno[6])
                print("Nacionalidade:", aluno[7])
                print("Curso preferido:", aluno[8])
        else:
            print("Nenhum aluno encontrado!")


    def atualizar(self):

        identificador = int(input("Digite o ID do aluno: "))

        valores = self.coletar_dados()

        sql = """
        UPDATE alunos
        SET nome = %s,
            profissao = %s,
            nascimento = %s,
            sexo = %s,
            peso = %s,
            altura = %s,
            nacionalidade = %s,
            cursopreferido = %s
        WHERE id = %s
        """

        self.cursor.execute(sql, valores + (identificador,))
        self.conexao.commit()

        if self.cursor.rowcount > 0:
            print("Aluno atualizado com sucesso!")
        else:
            print("Aluno não encontrado!")

    def excluir(self):

        identificador = int(input("Digite o ID do aluno: "))

        sql = "DELETE FROM alunos WHERE id = %s"

        self.cursor.execute(sql, (identificador,))
        self.conexao.commit()

        if self.cursor.rowcount > 0:
            print("Aluno excluído com sucesso!")
        else:
            print("Aluno não encontrado!")

    def listar_cursos(self):

        sql = "SELECT idcurso, nome FROM cursos"

        self.cursor.execute(sql)

        resultado = self.cursor.fetchall()

        if resultado:
            print("\n===== LISTA DE CURSOS =====")

            for curso in resultado:
                print("ID:", curso[0])
                print("Nome:", curso[1])

        else:
            print("Nenhum curso encontrado!")
