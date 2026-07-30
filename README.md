# 📱 CRUD Python SQLite

> Um sistema simples de gerenciamento de contatos desenvolvido em Python com SQLite como parte do meu aprendizado em programação.

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3-green?logo=sqlite&logoColor=white)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)

## 📖 Sobre o Projeto

Este é um projeto de estudo que desenvolvi para aprender na prática como integrar Python com bancos de dados. 

Antes deste projeto, eu armazenava dados em arquivos de texto (.txt). Com o SQLite, pude entender conceitos importantes como:
- Conexão com banco de dados
- Estruturação de dados em tabelas
- Operações CRUD (Create, Read, Update, Delete)
- Segurança com placeholders para evitar SQL injection

O sistema permite gerenciar uma lista de contatos com nome e telefone, tudo através de um menu interativo no terminal.

## ✨ Funcionalidades

- ➕ **Adicionar contatos** - Insere novos contatos com nome e telefone
- 📋 **Listar contatos** - Exibe todos os contatos cadastrados
- 🔍 **Buscar contato** - Localiza um contato específico pelo ID
- ✏️ **Atualizar contato** - Altera o nome de um contato existente
- 🗑️ **Excluir contato** - Remove um contato do banco de dados
- 🎮 **Menu interativo** - Interface simples no terminal para navegação

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+** - Linguagem de programação
- **SQLite3** - Banco de dados embutido (nativo do Python)
- **Terminal/CLI** - Interface de usuário

## 📁 Estrutura do Projeto
crud-python-sqlite/
│
├── main.py # Arquivo principal com todas as funções CRUD
├── database.py # Criação e configuração do banco de dados
└── Lista_contatos.db # Arquivo do banco de dados SQLite (gerado automaticamente)

text

## 🚀 Como Executar

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/crud-python-sqlite.git

# 2. Entre na pasta do projeto
cd crud-python-sqlite

# 3. Execute o arquivo de configuração do banco (opcional, o sistema cria automaticamente)
python database.py

# 4. Execute a aplicação principal
python main.py
💻 Exemplos de Uso
Menu Principal
text
1 - Adicionar usuário
2 - Ver usuários
3 - Buscar usuário
4 - Atualizar usuário
5 - Excluir usuário
6 - Sair do Programa

Escolha uma opção: 
Adicionando um Contato
text
Escolha uma opção: 1
Digite seu nome: João Silva
Digite seu telefone: 11999999999

✅ Usuário João Silva inserido com sucesso!
Visualizando Contatos
text
Escolha uma opção: 2

Lista de usuários cadastrados:
ID: 1 | Name: João Silva | Telefone: 11999999999
ID: 2 | Name: Maria Santos | Telefone: 11888888888
ID: 3 | Name: Pedro Oliveira | Telefone: 11777777777
Buscando um Contato
text
Escolha uma opção: 3
Digite o ID: 2

✅ Usuário encontrado:
ID: 2
Nome: Maria Santos
Telefone: 11888888888
📚 Conceitos Aprendidos
Durante o desenvolvimento deste projeto, pude praticar:

🐍 Fundamentos do Python - Funções, loops, condicionais, entrada de dados

🗄️ SQLite3 - Conexão com banco, criação de tabelas, consultas SQL

📊 Operações CRUD - INSERT, SELECT, UPDATE, DELETE

🛡️ Segurança - Uso de placeholders (?) para prevenir SQL injection

🔄 Controle de Fluxo - Estrutura de menu interativo com while True

🧹 Organização - Separação de responsabilidades em funções

⚠️ Tratamento de Erros - Blocos try/except para capturar exceçõ
