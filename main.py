#o 'r' é de read, ler, leitura. o "a" → append é pra adicionar sempre no final do arquivo
#"w" → write → escrever (subistitui conteudo)
import sqlite3
import database

def view_contacts():
    conexao = sqlite3.connect('Lista_contatos.db')
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM usuarios ')
    usuarios = cursor.fetchall()

    print('Lista de usuários cadastrados: ')
    for usuarios in usuarios:
        print(f'ID: {usuarios[0]} | Name: {usuarios[1]} | Telefone: {usuarios[2]}')

    conexao.commit()
    conexao.close()


def add_contact():
    conexao = sqlite3.connect('Lista_contatos.db')
    cursor = conexao.cursor()

    nome = input('Digite o seu nome: ')
    telefone = input('Digite o seu telefone: ')

    comando_sql = "INSERT INTO usuarios (name, telefone) VALUES (?, ?)"

    try:
        cursor.execute(comando_sql, (nome, telefone))
        conexao.commit()

        print(f'O Usuário {nome}, foi inserido com sucesso!')
    except sqlite3.IntegrityError:
        print('Erro: Dados já foram cadastrados. Tente novamente.')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')

    conexao.close()


def excluir_usuario():
    conexao = sqlite3.connect('Lista_contatos.db')
    cursor = conexao.cursor()

    id_para_deletar = int(input('Digite o ID a ser excluido: '))
    comando_delete = 'DELETE FROM usuarios WHERE id = ?'
    cursor.execute(comando_delete, (id_para_deletar,))

    conexao.commit()
    conexao.close()

    if cursor.rowcount > 0:
        print(f'Usuário de ID: {id_para_deletar} deletado do Banco de dados com sucesso.')
    else:
        print('Nenhum usuário encontrado com o ID fornecido.')


def buscar_usuario():
    conexao = sqlite3.connect('Lista_contatos.db')
    cursor = conexao.cursor()

    buscar_id = int(input('Digite o ID: '))

    comando_sql = 'SELECT id, name, telefone FROM usuarios WHERE id = ?'
    cursor.execute(comando_sql, (buscar_id,))
    usuario = cursor.fetchone()

    if usuario:
        print(f'Usuário encontrado. ID: {usuario[0]}, seu nome é: {usuario[1]}, | seu telefone é: {usuario[2]}')
    else:
        print('Usuário não encontrado no banco de dados.')


def atualizar_usuario():
    conexao = sqlite3.connect('Lista_contatos.db')
    cursor = conexao.cursor()

    novo_nome = input('Digite o seu novo nome de usuário: ')
    id_usuario = input('Digite o ID do usuário que você quer atualizar: ')

    comando_update = 'UPDATE usuarios SET name = ? WHERE id = ?'

    cursor.execute(comando_update, (novo_nome, id_usuario))

    conexao.commit()
    conexao.close()

    print('Nome atualizado com sucesso!')

    if cursor.rowcount > 0:
        print(f'Nome de Usuário, com ID: {id_usuario} Atualizado com sucesso!')
    else:
        print('Nenhum usuário encontrado com o ID fornecido.')


while True:
    print(
    '1 - Adicionar usuário\n'
    '2 - Ver Usuários\n'
    '3 - Buscar Usuário\n'
    '4 - Atualizar Usuário\n'
    '5 - Excluir Usuário\n'
    '6 - Sair do Programa'
    )

    menu_option = input('Escolha uma opção: ')

    if menu_option == '1':
        add_contact()
    elif menu_option == '2':
        view_contacts()
        print('Usuários listados acima.')
    elif menu_option == '3':
        buscar_usuario()
    elif menu_option == '4':
        atualizar_usuario()
    elif menu_option == '5':
        excluir_usuario()
    elif menu_option == '6':
        print('Saindo...')
        quit()
        
    else:
        print('Opção incorreta. Tente novamente.')
