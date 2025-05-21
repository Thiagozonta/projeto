import sqlite3

#menu principal do sistema 

def main_menu():
    print("n/ Sistema de Cadastro De Alunos")
    print("1. Cadastrar Aluno")
    print("2. Listar Alunos")
    print("3. Atualizar Aluno")
    print("4. Excluir Aluno")
    print("5. Sair")

    opcao = input("Escolha uma opcao:")
    return opcao

##################################################################
#   Objetivo: Conectar no Banco de Dados e Criar Tabela
##################################################################
def create_table():
    conexao = sqlite3.connect("Escola.db")
    cursor = conexao.cursor ()

    cursor.execute("""
             CREATE TABLE IF NOT EXISTS aluno(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   email TEXT NOT NULL UNIQUE,
                   Idade INTEGER
                   )      
                   """ )

    conexao.commit() #garantir 
    conexao.close()#

#funcao para cadastrar o aluno no DB
def register(nome,email,idade):

    conexao = sqlite3.connect("escola.db")
    cursor = conexao.cursor ()

    try:
        cursor.execute("INSERT INTO aluno(nome,email,idade)VALUES (?,?,?)",
                       (nome,email,idade))
    except sqlite3.IntegrityError:
        print("email ja cadastrado")
    finally:
        conexao.close()
def display():
    conexao = sqlite3.connect("escola01.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM aluno")
    alunos = cursor.fetchall()

    conexao.close.fetchall()#fecho a conexao com o banco

    print("Lista de Alunos Cadastrados")



if __name__ == "__main__":
    create_table()
    main_menu()

    while True:
        opcao = main_menu()
        
        if opcao == "1":
            nome = input("Nome:")
            email = imput("E-mail:")
            idade = imput("Idade:")
            register(nome,email,idade)
        elif opcao == "2":
            display()
        elif opcao == "5":
            break
        else:
            print("Funcao ainda nao implementada.")
