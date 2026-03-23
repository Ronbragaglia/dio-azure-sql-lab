"""
DIO Azure SQL Lab - Automação de GitHub e Azure SQL

Este pacote fornece ferramentas para:
- Criação automática de repositórios no GitHub
- Configuração de Azure SQL Managed Instance e Database
- Testes de conectividade com Azure SQL
"""

from .github_client import GitHubClient
from .azure_client import AzureSQLClient
from .repo_creator import create_repository, generate_readme

__version__ = "1.0.0"
__all__ = [
    "GitHubClient",
    "AzureSQLClient",
    "create_repository",
    "generate_readme",
]
