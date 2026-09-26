"""Tarefas do projeto executadas com o invoke.

Liste as tarefas disponíveis com `uv run invoke --list`.
"""

from invoke import task


@task
def lab(c):
    """Abre o JupyterLab."""
    c.run("jupyter lab")


@task
def app(c):
    """Executa a aplicação Streamlit definida em src/deployment/app.py."""
    c.run("streamlit run src/deployment/app.py")


@task
def docs(c):
    """Serve a documentação localmente em http://127.0.0.1:8000."""
    c.run("mkdocs serve")


@task
def build(c):
    """Gera o site estático da documentação no diretório site/."""
    c.run("mkdocs build")


@task
def lint(c):
    """Verifica o código com o ruff (lint e formatação)."""
    c.run("ruff check src tasks.py")
    c.run("ruff format --check src tasks.py")


@task
def fmt(c):
    """Formata o código e aplica correções automáticas do ruff."""
    c.run("ruff format src tasks.py")
    c.run("ruff check --fix src tasks.py")


@task
def test(c):
    """Executa a suíte de testes com o pytest."""
    c.run("pytest")
