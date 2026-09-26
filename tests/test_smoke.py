"""Teste inicial que garante que o pacote do projeto pode ser importado."""

import src


def test_version_disponivel():
    assert src.__version__
