# Fonte de dados

Esta página descreve **de onde vêm os dados** do projeto: a origem, como ela está
organizada, qual é o grão de cada registro e como a carga é reproduzida.

!!! tip "Como preencher esta página"
    Substitua os textos em destaque pelos do seu projeto. Preencha antes de começar a
    análise — quem chega depois no repositório lê esta página primeiro.

    Regras práticas:

    - descreva a origem de forma que **outra pessoa consiga acessá-la** (sistema, caminho,
      credencial necessária), sem expor segredos ou caminhos com dados pessoais;
    - registre o **grão** em uma frase: "cada linha é um(a) …";
    - anote **volumetria e período**, que são o que dimensiona todo o resto do projeto;
    - liste as **métricas aditivas** separadamente das dimensões — são elas que podem ser
      somadas com segurança;
    - deixe a seção de reprodução com os comandos reais, testados.

## Origem

<span style="color:red">**Descreva o sistema de origem, a área responsável e em que formato
os dados são publicados.**</span>

```
CAMINHO_DA_ORIGEM  (caminho de rede, URI do bucket ou string de conexão)
```

O caminho pode ser sobrescrito pela variável de ambiente `NOME_DA_VARIAVEL`.

!!! warning "Dados sensíveis"
    Não versione caminhos que contenham nome de usuário, token ou host interno
    identificável. Prefira um placeholder aqui e o valor real em um `.env` fora do git.

### Extração vigente

<span style="color:red">**Identifique a extração em uso (nome, data) e o que mudou em
relação à anterior. Se colunas foram acrescentadas ou removidas, liste-as.**</span>

| Coluna | Conteúdo |
|:---|:---|
| `nome_da_coluna` | &lt;o que ela representa&gt; |
| `nome_da_coluna` | &lt;o que ela representa&gt; |

## Organização da origem

<span style="color:red">**Explique o esquema de particionamento ou a estrutura de
diretórios/tabelas da origem.**</span>

```
raiz_da_origem/
├── particao_1=valor/
│   ├── particao_2=valor/arquivo.parquet
│   └── ...
└── particao_1=valor/
```

| Característica | Valor |
|:---|---:|
| Partições | &lt;n&gt; |
| Arquivos | &lt;n&gt; |
| Registros | &lt;n&gt; |
| Colunas | &lt;n&gt; |
| Volume na origem | &lt;n&gt; GB |
| Período | &lt;aaaa a aaaa&gt; |

## Grão e conteúdo

Cada linha é um(a) **&lt;grão do registro&gt;** (`coluna_identificadora`).

<span style="color:red">**Descreva as dimensões disponíveis e, se a tabela for
desnormalizada, quantas dimensões estão embutidas nela.**</span>

As métricas aditivas são:

| Métrica | Descrição |
|:---|:---|
| `nome_da_metrica` | &lt;o que é contabilizado e em que unidade&gt; |
| `nome_da_metrica` | &lt;o que é contabilizado e em que unidade&gt; |

## Fluxo de dados no projeto

```mermaid
flowchart LR
    A["Origem<br/>formato e volume"] --> B["data/raw<br/>o que é materializado"]
    B --> C["data/processed/base curada<br/>colunas curadas"]
    C --> D["data/processed/agregados<br/>um por objetivo"]
    D --> E["notebooks<br/>figuras, tabelas e relatórios"]
```

<span style="color:red">**Indique o notebook e o módulo responsáveis pela carga, e se ela é
idempotente (pode ser reexecutada sem duplicar dado).**</span>

## Fontes complementares

Dados que não vêm da origem principal, mas entram na análise.

| Arquivo | Conteúdo |
|:---|:---|
| `data/raw/arquivo.csv` | &lt;o que contém e para que serve&gt; |

## Reprodução

```bash
# comandos que refazem a carga do zero
uv run invoke ingestao
uv run invoke preparacao
```
