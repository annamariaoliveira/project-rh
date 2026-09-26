# Análise exploratória

Esta página resume **o desenho** da análise exploratória: quais notebooks existem, o que cada
um responde e as decisões metodológicas que valem para todos. Os resultados em si ficam nas
figuras de `reports/figures/` e nas tabelas de `data/processed/`.

!!! tip "Como preencher esta página"
    Preencha depois de [Entendimento dos dados](entendimento-dados.md): a EDA parte dos
    achados de qualidade registrados lá.

    Regras práticas:

    - um notebook por **objetivo de negócio**, não por técnica — assim dá para rastrear cada
      entrega até o critério de aceite que ela atende;
    - a página descreve o **desenho**, não os resultados; achado que interessa ao negócio vai
      para a página do objetivo correspondente;
    - toda decisão que muda a leitura de um gráfico (percentual × volume, média × mediana,
      como tratar ausência) fica registrada em **Escolhas metodológicas** — é o que impede a
      discussão de recomeçar do zero a cada revisão;
    - se os notebooks são commitados sem saída (`nbstripout`), então **toda figura e tabela
      relevante precisa ser persistida em disco**, ou o resultado se perde.

## Mapa dos notebooks

| Notebook | Objetivo | Recorte | Saída principal |
|:---|:-:|:---|:---|
| `NN-objN-nome.ipynb` | &lt;n&gt; | &lt;recorte de dados&gt; | &lt;o que o notebook produz&gt; |
| `NN-objN-nome.ipynb` | &lt;n&gt; | &lt;recorte de dados&gt; | &lt;o que o notebook produz&gt; |
| `NN-objN-nome.ipynb` | &lt;n&gt; | &lt;recorte de dados&gt; | &lt;o que o notebook produz&gt; |

A coluna **Objetivo** referencia a numeração dos [critérios de sucesso](criterios-sucesso.md).

## Desenho da EDA

<span style="color:red">**Descreva o roteiro do notebook de análise exploratória e sobre
quais variáveis ele é aplicado.**</span>

| Seção | Técnica | O que responde |
|:---|:---|:---|
| Valores ausentes | &lt;como a ausência é medida&gt; | a ausência é aleatória ou estrutural? |
| Univariada | &lt;técnica&gt; | como cada variável se distribui? |
| Outliers | &lt;critério de corte&gt; | há valor implausível? |
| Bivariada | &lt;medida de associação&gt; | quais variáveis andam juntas? |
| Multivariada | &lt;técnica de redução ou associação&gt; | que estrutura existe no conjunto? |
| Temporal | &lt;como a evolução é medida&gt; | o comportamento mudou ao longo do tempo? |

![](imagens/eda-steps.png)

### Escolhas metodológicas

Cada item declara **a decisão** e **o motivo** — o motivo é o que evita que a decisão seja
revertida por engano depois.

??? note "Decisões que costumam entrar aqui"
    - **percentual × volume** ao comparar grupos de tamanhos muito diferentes: valor
      absoluto mede tamanho, não comportamento;
    - **como tratar a ausência**: calcular sobre a base com informação e reportar o
      percentual ausente, em vez de descartar linhas ou tratar a sentinela como categoria;
    - **associação em vez de contagem cruzada**: a tabela de contingência bruta é dominada
      pelas categorias grandes;
    - **média × mediana** quando existe cauda longa legítima;
    - **amostragem** em cálculos de custo quadrático, quando a leitura comparativa não muda.

- <span style="color:red">**Decisão — e por quê.**</span>
- <span style="color:red">**Decisão — e por quê.**</span>
- <span style="color:red">**Decisão — e por quê.**</span>

## Reprodução

```bash
# comando que executa os notebooks na ordem
uv run invoke notebooks
```

<span style="color:red">**Registre se os notebooks são versionados sem saída e onde as
figuras e tabelas ficam persistidas.**</span>

## Dados por trás de cada gráfico

Boa prática: exportar a tabela-fonte de cada figura no mesmo momento em que a figura é
gravada, de modo que o dado não tenha como divergir do gráfico.

<span style="color:red">**Indique o diretório de exportação, o formato do CSV (separador e
decimal) e a função responsável por gravar figura e dado juntos.**</span>
