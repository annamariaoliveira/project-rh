# Entendimento dos dados

Esta página responde a três perguntas sobre o conjunto de dados: **o que existe**, **em que
qualidade** e **o que isso impede ou permite** dentro dos objetivos do projeto.

!!! tip "Como preencher esta página"
    Preencha depois de [Fonte dos dados](fonte-dados.md) e antes de
    [Preparação dos dados](preparacao.md): aqui você descreve o que encontrou, lá você
    descreve o que fez a respeito.

    Regras práticas:

    - descreva o **grão** antes de qualquer outra coisa — quase todo erro de análise nasce
      de somar coisas em grãos diferentes;
    - agrupe as colunas por **dimensão de negócio**, não em ordem alfabética: é assim que
      quem conhece o negócio procura;
    - confronte os dados com os [critérios de sucesso](criterios-sucesso.md) e diga, para
      cada requisito, se ele está **atendido, parcial ou inviável**;
    - registre cada achado de qualidade com a **consequência para a análise**, não apenas a
      constatação ("a coluna X tem 30% de nulo" → "por isso a distribuição de X é calculada
      sobre a base com informação");
    - o que não puder ser resolvido com dado disponível vira **limitação declarada**, não
      um objetivo silenciosamente reduzido.

## Dados iniciais

<span style="color:red">**Indique de onde vieram os dados analisados aqui e em qual
notebook está a apuração desta página.**</span>

## Descrição dos dados

### Grão

Cada linha é um(a) **&lt;grão do registro&gt;** (`coluna_identificadora`).

<span style="color:red">**Diga se a tabela é normalizada ou achatada e, se for achatada,
quantas dimensões estão embutidas nela.**</span>

### Grupos de colunas

| Dimensão | Exemplos de colunas |
|:---|:---|
| &lt;Dimensão de negócio&gt; | `coluna_a`, `coluna_b`, `coluna_c` |
| &lt;Dimensão de negócio&gt; | `coluna_d`, `coluna_e` |
| Métricas | `metrica_a`, `metrica_b` |

### Cobertura frente aos critérios de sucesso

| Requisito | Situação |
|:---|:---|
| &lt;Requisito vindo dos critérios de sucesso&gt; | **atendida** — &lt;com que dado&gt; |
| &lt;Requisito vindo dos critérios de sucesso&gt; | **parcial** — &lt;o que falta&gt; |
| &lt;Requisito vindo dos critérios de sucesso&gt; | **inviável** — &lt;por quê&gt; |

## Qualidade dos dados

### Valores sentinela

Muitos sistemas de origem não gravam nulo: a ausência de informação vira uma categoria de
texto ou um código negativo. Sem tratamento, essas sentinelas aparecem nas distribuições
como se fossem valores reais.

| Sentinela | Significado |
|:---|:---|
| `<valor sentinela>` | &lt;o que representa na origem&gt; |
| `<valor sentinela>` | &lt;o que representa na origem&gt; |

<span style="color:red">**Diga onde essas regras estão implementadas e se há exceção
deliberada — alguma coluna em que a sentinela é categoria legítima e deve ser preservada.**</span>

### Achados que mudam a análise

Registre aqui o que foi descoberto na exploração e que **altera alguma decisão** adiante.

??? note "O que costuma aparecer nesta seção"
    - **coluna quase certa**: existem duas colunas parecidas e a informação útil está na
      menos óbvia;
    - **sujeira de formatação**: espaços de preenchimento, caixa inconsistente ou acentuação
      que fragmentam a mesma categoria em várias;
    - **preenchimento descontínuo**: a coluna deixa de ser alimentada em parte da série;
    - **ausência estrutural, não aleatória**: o campo falta justamente em um subconjunto
      (um canal, um período, um tipo de cliente) — descartar essas linhas enviesa o retrato;
    - **valores extremos legítimos**: outliers que são reais e não podem ser removidos de
      somas, mas distorcem médias.

1. <span style="color:red">**Achado — e o que ele muda na análise.**</span>
2. <span style="color:red">**Achado — e o que ele muda na análise.**</span>
3. <span style="color:red">**Achado — e o que ele muda na análise.**</span>

## Dimensões-chave

Use esta seção para detalhar uma dimensão que exigiu tratamento próprio — porque não existia
na origem, porque foi derivada, ou porque sustenta sozinha um critério de aceite.

<span style="color:red">**Descreva a dimensão: de onde ela vem, como é derivada e por que a
derivação foi feita assim.**</span>

| Valor | Descrição | Regra de derivação |
|:---|:---|:---|
| `<valor>` | &lt;o que significa&gt; | &lt;condição que o produz&gt; |
| `<valor>` | &lt;o que significa&gt; | &lt;condição que o produz&gt; |

## Limitações

O que os dados **não** permitem responder, com o impacto em cada objetivo afetado.

<span style="color:red">**Declare cada limitação e qual objetivo ela afeta. Se depender de
dado a ser fornecido por terceiro, registre também nas pendências dos
[critérios de sucesso](criterios-sucesso.md).**</span>
