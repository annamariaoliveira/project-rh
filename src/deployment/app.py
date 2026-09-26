"""Aplicação Streamlit de exemplo.

Execute com `uv run invoke app` ou `uv run streamlit run src/deployment/app.py`.
"""

import streamlit as st


def main() -> None:
    """Ponto de entrada da aplicação."""
    st.set_page_config(page_title="Nome do projeto", layout="wide")
    st.title("Nome do projeto")
    st.write("Substitua este conteúdo pela interface do seu projeto.")


if __name__ == "__main__":
    main()
