import sqlite3

# 1 - fazendo conexão com o banco de dados
conexao = sqlite3.connect("Lista_contatos.db")

# cursor vai enviar informações para o banco de dados, qual banco de dados? o conexao, ele ta fazendo a intermediação, ele é o carteiro
cursor = conexao.cursor()

# Escrevendo um comando SQL pra criar tabela(a)s.
Comando_sql = """
CREATE TABLE IF NOT EXISTS usuarios(
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 name TEXT NOT NULL,
 telefone INTEGER UNIQUE NOT NULL

)
"""
#Fazendo execução do comando SQL
cursor.execute(Comando_sql)
#Aqui vai salvar as alterações todas no banco de dados.
conexao.commit()
#fechar a conexão com o banco de dados
conexao.close()

#Mostrando se foi criado com sucesso (pode printar e não ter criado com sucesso, é apenas visual.)
print('Banco de dados, e tabelas foram criados com sucesso.')