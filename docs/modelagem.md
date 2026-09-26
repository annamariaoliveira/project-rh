# Modelagem dos dados

Esta página descreve **o desenho do experimento de modelagem**: qual problema o modelo
resolve, sobre que unidade de análise ele opera, quais variáveis entram, qual técnica foi
escolhida e como o resultado é avaliado.

!!! tip "Como preencher esta página"
    Nem todo objetivo exige modelo — objetivos descritivos são resolvidos na
    [análise exploratória](analise-exploratoria.md). Declare logo no início **quais**
    objetivos exigem modelagem e por quê.

    Regras práticas:

    - a **unidade de análise** vem da pergunta de negócio, não do formato da tabela; se a
      pergunta é sobre o cliente, um registro por transação faria os clientes recorrentes
      dominarem o resultado;
    - amarre cada variável ao **critério de aceite** que a pediu, e marque as que você
      acrescentou por conta própria;
    - justifique a **técnica** pelo tipo de dado (categórico, contínuo, misto, textual,
      temporal) — não pela familiaridade com a biblioteca;
    - toda métrica de avaliação vem com a **direção de leitura** (maior é melhor / menor é
      melhor) e com a ressalva de quando ela engana;
    - liste as **saídas** com caminho: modelo serializado, tabelas de resultado e figuras.

## Problema

<span style="color:red">**Enuncie o problema em uma frase, no vocabulário do negócio, e
indique a que objetivo dos [critérios de sucesso](criterios-sucesso.md) ele corresponde.**</span>

<span style="color:red">**Aponte o notebook e o módulo onde a modelagem está
implementada.**</span>

## Unidade de análise

Um registro por **&lt;unidade de análise&gt;** (`arquivo_de_entrada`).

<span style="color:red">**Justifique a escolha: por que esta unidade e não outra, e o que
daria errado com a alternativa.**</span>

## Variáveis

| Critério pede | Variável usada | Observação |
|:---|:---|:---|
| &lt;dimensão pedida no critério&gt; | `nome_da_coluna` | &lt;o que ela representa&gt; |
| &lt;dimensão pedida no critério&gt; | `nome_da_coluna` | &lt;o que ela representa&gt; |
| — | `nome_da_coluna` | &lt;variável acrescentada e o que ela captura&gt; |

<span style="color:red">**Descreva as variáveis derivadas, se houver, e o que elas separam
que as variáveis originais não separavam.**</span>

### Pré-processamento

<span style="color:red">**Registre cada transformação e o motivo.**</span>

??? note "Transformações que costumam entrar aqui"
    - agrupamento de categorias raras em `Outros`, para que o modelo não gaste capacidade
      descrevendo ruído;
    - decisão sobre ausência: virar categoria própria, ser imputada ou excluir a linha;
    - transformação de escala em contagens com cauda longa (`log1p`, padronização);
    - codificação de categóricas, coerente com a técnica escolhida;
    - balanceamento, quando a classe de interesse é rara.

## Técnica

<span style="color:red">**Explique por que esta técnica se aplica ao tipo de dado do
problema.**</span>

```mermaid
flowchart LR
    A["entrada<br/>variáveis"] --> B["etapa 1<br/>transformação"]
    B --> C["etapa 2<br/>modelo"]
    C --> D["etapa 3<br/>caracterização do resultado"]
```

<span style="color:red">**Detalhe cada etapa do pipeline e onde ela é ajustada — em amostra
ou na base completa.**</span>

## Avaliação do modelo

| Métrica | Leitura |
|:---|:---|
| &lt;métrica&gt; | &lt;maior ou menor é melhor, e o que ela mede&gt; |
| &lt;métrica&gt; | &lt;maior ou menor é melhor, e o que ela mede&gt; |

<span style="color:red">**Descreva o desenho do experimento: divisão treino/teste, validação
cruzada, faixa de hiperparâmetros testada e critério de escolha do modelo final.**</span>

!!! warning "Ressalva de métrica"
    Use um bloco como este para registrar quando uma métrica engana no seu contexto — por
    exemplo, acurácia com classes desbalanceadas, ou índices de separação em espaços
    derivados de variáveis categóricas. Diga qual é o critério de desempate.

## Interpretação do resultado

<span style="color:red">**Explique como o resultado é traduzido para o negócio: importância
de variáveis, caracterização de grupos, regras extraídas. Se houver nomeação automática de
grupos ou classes, descreva o critério.**</span>

## Saídas

| Arquivo | Conteúdo |
|:---|:---|
| `data/processed/nome.parquet` | &lt;o que contém&gt; |
| `models/nome.joblib` | &lt;modelo serializado, para que serve&gt; |
| `reports/figures/nome/*.png` | &lt;quais figuras&gt; |
