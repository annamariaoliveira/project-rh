# Projeto RH — Segmentação de Colaboradores (IBM HR Analytics)

Este projeto aplica técnicas de **Machine Learning Não Supervisionado** para segmentar colaboradores de uma organização com base em características demográficas, profissionais e de satisfação, utilizando a base de dados pública *IBM HR Analytics Employee Attrition & Performance*. O fluxo segue as diretrizes metodológicas do **CRISP-DM**.

## Objetivos e Resultados-Chave

- **Objetivo 1**: Realizar a Análise Exploratória (EDA) e Curadoria da base de dados de Recursos Humanos.
    - Identificar variáveis, descrevê-las e definir os tipos de dados (Notebook 01).
    - Tratar a consistência e estruturar engenharia de recursos para RH (Notebook 02).
- **Objetivo 2**: Preparar e Modelar Dados para Agrupamento (Clusterización).
    - Aplicar normalização (`MinMaxScaler`) e codificação (`OneHotEncoder`) (Notebook 03).
    - Executar uma varredura comparativa com múltiplos algoritmos de clusterização (K-Means, K-Medoides, GMM, DBSCAN, etc.) avaliados pela métrica da silhueta (Notebook 04).

## Conteúdo / Notebooks

- **`00-dicionario-dados.ipynb`**: Mapeamento e dicionário das variáveis do dataset.
- **`01-analise-exploratoria.ipynb`**: Análise exploratória univariada, bivariada, multivariada e correlogramas.
- **`02-ajustes-dados.ipynb`**: Limpeza, tratamento e curadoria da base de RH (`base_rh_tratado.csv`).
- **`03-preparacao.ipynb`**: Pré-processamento, escalonamento e codificação para a modelagem (`base_rh_preprocessed.csv`).
- **`04-0-modelagem-cluster.ipynb`**: Varredura de modelos de agrupamento, seleção do algoritmo vencedor, salvamento do modelo em disco (`.joblib`) e análise de perfil dos segmentos.

## Utilização

Este projeto utiliza o [uv](https://docs.astral.sh/uv/) como gerenciador de dependências e ambientes virtuais.

Passos básicos para replicar o ambiente:

```bash
# Criar o ambiente virtual e instalar todas as dependências
uv sync

# Ativar o ambiente virtual (se necessário) ou executar via uv run
uv run invoke lab     # Abre o JupyterLab