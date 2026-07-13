# Programação para Internet

Repositório criado para a disciplina de programação para a internet com o professor Daniel Aguiar na turma de info3V do IFRN - Campus Parnamirim
---

## 📁 Organização

Todos os projetos Flask estão localizados na pasta `src/`.

---

## 📦 Projetos

- [x] Tutorial Flask
- [x] Banco de Problemas Matemáticos (Faltam apenas ajustes visuais)

## 📝 Objetivo

O primeiro projeto tem como objetivo fornecer um ambiente simples para registrar e compartilhar problemas matemáticos organizados por assunto e nível de dificuldade, seguindo a arquitetura apresentada no Tutorial Oficial do Flask e a lógica do sistema CRUD do SQL.

---
## ⚙️ Funcionalidades: 
- Cadastro e autenticação de usuários.
- Cadastro de problemas matemáticos.
- Listagem de problemas cadastrados.
- Edição de problemas criados pelo próprio usuário.
- Exclusão de problemas criados pelo próprio usuário.

---
## 📖Cada problema poderá conter informações como:

- Título
- Enunciado
- Assunto
- Dificuldade
- Resposta

---
## 🤖 Tecnologias
- Python
- Flask
- SQLite
- HTML
- CSS
- Jinja2
---

---
## 🖥️ Como executar
Crie um ambiente virtual e o ative.   
Abra em seu diretório a pasta raíz do projeto (project-flask)  
Digite:
- python -m venv .venv
- .venv\Scripts\activate  
Instale as bibliotecas
- pip install -r requirements.txt  
Escolha qual projeto você quer rodar, e substituia "projeto" nos comandos abaixos pelo nome do projeto: <br>
Flask --app src/projeto init-db   <br>
Flask --app src/projeto run 

---
O projeto segue a organização proposta pelo Tutorial Oficial do Flask, utilizando Application Factory, Blueprints e SQLite para persistência dos dados.
