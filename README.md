# 📱 CRUD Python SQLite

Sistema simples de gerenciamento de contatos desenvolvido em Python com SQLite.

## 🎯 Sobre o Projeto

Este é um projeto de estudo que desenvolvi para aprender na prática como integrar Python com banco de dados. O sistema permite gerenciar contatos com operações básicas de CRUD (Create, Read, Update, Delete).

## ✨ Funcionalidades

- Adicionar contatos
- Listar todos os contatos
- Buscar contato por ID
- Atualizar nome do contato
- Excluir contato
- Menu interativo no terminal

## 🛠️ Tecnologias

- Python 3
- SQLite3

## 📁 Estrutura
crud-python-sqlite/
├── app.py # Aplicação principal (CRUD)
├── database.py # Criação do banco e tabela
└── Lista_contatos.db # Banco de dados

text

## 🚀 Como Executar

```bash
# 1. Clone o repositório
git clone https://github.com/seuusuario/crud-python-sqlite.git

# 2. Acesse a pasta
cd crud-python-sqlite

# 3. Crie o banco de dados
python database.py

# 4. Execute a aplicação
python app.py
📋 Menu
text
1 - Adicionar usuário
2 - Ver usuários
3 - Buscar usuário
4 - Atualizar usuário
5 - Excluir usuário
6 - Sair
💻 Exemplos
Adicionar contato:

text
Digite seu nome: João Silva
Digite seu telefone: 11999999999
✅ Usuário João Silva inserido com sucesso!
Listar contatos:

text
ID: 1 | Name: João Silva | Telefone: 11999999999
ID: 2 | Name: Maria Santos | Telefone: 11888888888
Buscar contato:

text
Digite o ID: 1
Usuário encontrado. ID: 1, nome: João Silva, telefone: 11999999999
📚 Conceitos em aprendizado:
Conexão com SQLite

Operações CRUD

SQL básico (SELECT, INSERT, UPDATE, DELETE)

Tratamento de erros com try/except

Organização de código em funções

Importação de módulos
