# Laboratório DIO: Azure SQL Managed Instance + GitHub Automation

Este projeto faz parte do desafio da **Digital Innovation One (DIO)** para consolidar conhecimentos na criação e documentação de ambientes Azure SQL Managed Instance, e na utilização do GitHub como plataforma para versionamento e compartilhamento.

O notebook em **Python (Google Colab)** tem como objetivo **automatizar** parte do processo do desafio:
- Criar um repositório no GitHub de forma automática via API.
- Gerar um arquivo `README.md` inicial com instruções e links úteis.
- Fazer commit e push do conteúdo direto para o GitHub.
- (Opcional) Instalar `pyodbc` para preparar testes de conexão a um banco **Azure SQL Database** ou **Managed Instance**.

---

## 🎯 Objetivos do projeto

- **Praticar conceitos aprendidos** no curso/laboratório.
- **Documentar** o processo de criação de um ambiente de banco de dados no Microsoft Azure.
- **Automatizar** a criação de repositórios no GitHub via API.
- Criar documentação detalhada usando Markdown (`README.md`).
- Servir como **base de estudos futuros** e repositório de anotações e dicas.

---

## 📂 Estrutura do Projeto

.
├── README.md -> Guia rápido e documentação
├── notebook_colab.ipynb -> Código Python para rodar no Google Colab
└── images/ -> Pasta para armazenar prints do ambiente/configuração

text

---

## 🚀 Como usar o notebook no Google Colab

1. Abra o [Google Colab](https://colab.research.google.com/).
2. Crie um novo notebook e copie o código presente neste repositório (`notebook_colab.ipynb`).
3. No Colab, execute célula por célula:
   - **Configuração do GitHub**: inserir seu usuário, nome do repositório e token com escopo `repo`.
   - **Criação do repositório** usando a API do GitHub.
   - **Geração do README.md** automático com base nas instruções do desafio.
   - **Configuração do Git no Colab** e **envio (push)** para o GitHub.
   - (Opcional) Instalar `pyodbc` para testes com Azure SQL.

---

## 📌 Requisitos

- **Conta do GitHub** e **Personal Access Token (PAT)** com permissão `repo`.
- **Conta no Microsoft Azure** para provisionar Azure SQL Managed Instance ou Azure SQL Database.
- No caso de testes de conexão a bancos Azure SQL:
  - **pyodbc** instalado
  - **ODBC Driver 18 for SQL Server**
  - Rede permitindo conexão ao banco (liberação de firewall ou conexão via VNet/VPN no caso da MI).

---

## 📜 Exemplo de conexão Python → Azure SQL

import pyodbc

server = "SEU_SERVIDOR.database.windows.net" # ou endpoint público da MI
database = "SEU_BANCO"
username = "SEU_USUARIO"
password = "SUA_SENHA"
driver = "{ODBC Driver 18 for SQL Server}"

conn_str = (
f"DRIVER={driver};"
f"SERVER={server};"
f"DATABASE={database};"
f"UID={username};"
f"PWD={password};"
"Encrypt=yes;"
"TrustServerCertificate=no;"
)

with pyodbc.connect(conn_str) as conn:
with conn.cursor() as cursor:
cursor.execute("SELECT TOP 3 name, create_date FROM sys.databases ORDER BY create_date DESC;")
for r in cursor.fetchall():
print(r)

text

---

## 📷 Sugestão de documentação adicional

- **Passo a passo** da criação da instância no **Azure Portal** (ou via CLI/PowerShell).
- **Capturas de tela** salvas na pasta `/images`.
- Testes de conectividade (Azure Data Studio, SSMS e Python).
- Links úteis para referência:
  - [Quickstart: Criar Azure SQL Managed Instance](https://learn.microsoft.com/pt-br/azure/azure-sql/managed-instance/instance-create-quickstart?view=azuresql&tabs=azure-portal)
  - [GitHub Docs](https://docs.github.com/pt)

---

## 📅 Atualizado em 13/08/25
