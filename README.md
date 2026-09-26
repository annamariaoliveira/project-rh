# <Título do projeto>

Insira aqui uma introdução para que o leitor entenda o contexto e os problemas identificados. Tente apresentar uma justificativa para o projeto. É desejável que também se insira um [graphical abstract](https://www.elsevier.com/authors/tools-and-resources/visual-abstract).

## Objetivos e resultados chave

Em termos simples, os "Objetivos" se relacionam com a meta do projeto, e os "Resultados-Chave" expressam como essa meta será alcançada. Os Objetivos e resultados chave devem ser definidos no início de um projeto. A ideia é escolher uma métrica associada a um projeto e defini-la como o objetivo. Isso mostra a meta que você deseja alcançar. Em seguida, os resultados-chave são definidos para mostrar como atingir o objetivo. Os resultados principais são mensuráveis ​​e geralmente limitados a três a cinco por objetivo.

Em síntese, os objetivos estão ligados as entregas e os resultados chave aos passos que precisam se seguir para conseguir alcançar os resultados.
Exemplo de objetivos e resultados chave aplicados a projetos de ciência de dados.

 - Realizar uma análise exploratória de dados de <conjunto de dados>
    - Indentificar variáveis, descrevê-las e definir os tipos de dados
    - Realizar transformação de variáveis (codificação)
    - Tratar de valores faltantes e valores discrepantes
    - ...
 - Criar modelo de detecção de fakenews
    - Realizar transformação de dados textuais utilizando o tf-idf
    - ...
 - ...

## Conteúdo

Utilize esta seção para descrever o que cada notebook faz. Se tiver gerado algum relatório, também utilize essa seção para descrevêlo. Isso facilitará a leitura.

## Utilização

Descreva aqui quais os passos necessários (dependências externas, comandos, etc.) para replicar o seu projeto. Instalação de dependências necessárias, criação de ambientes virtuais, etc. Este modelo é baseado em um projeto utilizando o [uv](https://docs.astral.sh/uv/) como gerenciador de dependências e ambientes virtuais. Você pode utilizar o `conda`, ambientes virtuais genéricos do Python ou até mesmo containers do docker. Mas tente fazer algo que seja facilmente reprodutível.

Passos básicos com o `uv`:

```bash
# Instalar o uv (caso ainda não tenha)
# https://docs.astral.sh/uv/getting-started/installation/

# Criar o ambiente virtual e instalar todas as dependências (usa o uv.lock)
uv sync

# Instalar os hooks de pre-commit (ruff + nbstripout)
uv run pre-commit install

# Listar as tarefas disponíveis do projeto
uv run invoke --list

# Exemplos de tarefas
uv run invoke lab     # Abre o JupyterLab
uv run invoke app     # Executa a aplicação Streamlit
uv run invoke docs    # Serve a documentação localmente
uv run invoke lint    # Verifica o código com o ruff
uv run invoke test    # Executa os testes com o pytest

# Adicionar uma nova dependência
uv add <pacote>

# Adicionar uma dependência de desenvolvimento ou de documentação
uv add --group dev <pacote>
uv add --group docs <pacote>
```

A versão do Python utilizada está fixada em [`.python-version`](.python-version); o `uv` instala e usa essa versão automaticamente.

## Desenvolvedores
 - [Contribuidor 1](http://github.com/contribuidor_1)
 - [Contribuidor 2](http://github.com/contribuidor_2)

## Organização de diretórios

> **Nota**: essa seção é somente para entendimento do usuário do template. Por favor removê-la quando for atualizar este `README.md`

```
.
├── .github/                # Templates de issues/PRs e CODEOWNERS
├── data/                   # Diretório contendo todos os arquivos de dados (Geralmente está no git ignore ou git LFS)
│   ├── external/           # Arquivos de dados de fontes externas
│   ├── processed/          # Arquivos de dados processados
│   └── raw/                # Arquivos de dados originais, imutáveis
├── docs/                   # Documentação do projeto publicada com o MkDocs
├── models/                 # Modelos treinados e serializados, predições ou resumos de modelos
├── notebooks/              # Diretório contendo todos os notebooks utilizados nos passos
├── references/             # Dicionários de dados, manuais e todo o material exploratório
├── reports/                # Análises geradas como html, latex, etc
│   └── figures/            # Imagens utilizadas nas análises
├── src/                    # Código fonte utilizado nesse projeto
│   ├── data/               # Classes e funções utilizadas para download e processamento de dados
│   ├── deployment/         # Classes e funções utilizadas para implantação do modelo
│   └── model/              # Classes e funções utilizadas para modelagem
├── tests/                  # Testes automatizados executados com o pytest
├── .pre-commit-config.yaml # Hooks de qualidade executados antes de cada commit (ruff, nbstripout)
├── .python-version         # Versão do Python utilizada pelo uv para criar o ambiente
├── LICENSE                 # Licença do projeto
├── mkdocs.yml              # Configuração do site de documentação
├── pyproject.toml          # Arquivo de dependências para reprodução do projeto
├── uv.lock                 # Arquivo com subdependências do projeto principal (lockfile do uv)
├── README.md               # Informações gerais do projeto
└── tasks.py                # Arquivo com funções para criação de tarefas utilizadas pelo invoke

```
