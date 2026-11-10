# 📊 Projeto 2: Raio-X Salarial da Área de Dados

> **Área:** Análise e Ciência de Dados (EDA) · **Nível:** ⭐⭐⭐ · **Tempo estimado:** 7 a 9 horas
> **Conteúdos usados:** funções (Aula 05), arquivos (Aula 06), exceções (Aula 07), `dict`/`tuple`/`set` (Aula 08), `sorted` com `key` (PyVotação)

## 📖 Contexto

Você está entrando na área de dados e, cedo ou tarde, vai se perguntar: *"quanto ganha quem trabalha com isso? Vale mais ser Engenheiro(a) de Dados ou Cientista? Trabalhar remoto paga melhor? E Pernambuco, como fica?"*

Uma comunidade de profissionais fez uma **pesquisa salarial** com 640 pessoas da área. Os dados são **fictícios**, mas foram construídos para ter comportamento realista. Sua missão é fazer a **Análise Exploratória de Dados (EDA)**, a etapa que, como vimos na Aula 07, vem depois do ETL: entender a distribuição dos dados, comparar grupos, achar padrões e outliers e **transformar números em respostas**.

> 💬 O detalhe que torna este projeto especial: você **não** vai usar bibliotecas de estatística. Você vai **implementar média, mediana, desvio padrão e correlação** com as próprias mãos. Quando chegar o NumPy, você vai saber exatamente o que `np.median()` faz por dentro.

## 🎯 Objetivo

Construir um programa que leia a pesquisa, calcule estatísticas descritivas por grupos, desenhe gráficos no terminal e gere um relatório com **insights**, além de um CSV-resumo que poderia alimentar um dashboard.

## 📦 Dados de entrada

Arquivo: [`dados/pesquisa_salarial.csv`](dados/pesquisa_salarial.csv), separado por **vírgula**.

```txt
id,cargo,nivel,anos_experiencia,uf,modelo_trabalho,salario_mensal
1,Analista de Dados,Sênior,6,BA,Remoto,9200
2,Cientista de Dados,Pleno,2,PR,Híbrido,9300
3,Analista de Dados,Júnior,0,SP,Híbrido,6000
4,Cientista de Dados,Especialista,8,SP,Remoto,22200
```

### Dicionário de dados

| Coluna | Tipo | Valores possíveis |
| ------ | ---- | ----------------- |
| `id` | inteiro | Identificador da resposta |
| `cargo` | texto | Analista de Dados, Analista de BI, Cientista de Dados, Engenheiro(a) de Dados, Engenheiro(a) de Machine Learning |
| `nivel` | texto | Júnior, Pleno, Sênior, Especialista |
| `anos_experiencia` | inteiro | Anos de experiência na área. **Pode estar vazio** |
| `uf` | texto | Sigla do estado (10 estados) |
| `modelo_trabalho` | texto | Remoto, Híbrido, Presencial |
| `salario_mensal` | decimal | Salário bruto mensal em R$. **Pode estar vazio ou com texto** |

## 📏 Regras de tratamento

Toda pesquisa real tem respostas problemáticas. Siga estas regras:

| Situação | O que fazer |
| -------- | ----------- |
| `salario_mensal` vazio ou com texto (ex.: `prefiro não informar`) | **Descartar** a resposta e contar como "sem salário informado" |
| `salario_mensal` **acima de R$ 60.000** | É um **outlier**: provavelmente a pessoa informou o salário **anual**. **Remover** da análise e listar os `id`s no relatório |
| `anos_experiencia` vazio | **Manter** a resposta em todas as análises, **exceto** no cálculo da correlação |

> 🧠 **Por que remover outliers?** Faça o teste: calcule a média geral **com** e **sem** os dois outliers. A média é muito sensível a valores extremos; a mediana, quase nada. É por isso que análises salariais costumam usar a **mediana**.

## 🧮 Parte 1: sua mini biblioteca de estatística

Implemente estas funções **sem** usar `statistics`, `numpy` ou similares. `sum()`, `len()`, `min()`, `max()` e `sorted()` podem ser usados.

| Função | O que calcula | Como calcular |
| ------ | ------------- | ------------- |
| `media(valores)` | Valor médio | soma ÷ quantidade |
| `mediana(valores)` | Valor do meio | Ordene a lista. Se o tamanho for **ímpar**, pegue o elemento do meio; se for **par**, a média dos dois do meio |
| `desvio_padrao(valores)` | O quanto os valores se espalham em torno da média | Fórmula abaixo |
| `resumo(valores)` | Tudo junto | Devolve um **dicionário** `{'n', 'media', 'mediana', 'min', 'max', 'dp'}` |

**Desvio padrão (amostral):**

$$ s = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n - 1}} $$

Em português: para cada valor, calcule a distância até a média e eleve ao quadrado; some tudo; divida por `n - 1`; tire a raiz quadrada. Para a raiz quadrada, lembre-se de que `x ** 0.5` é a raiz de `x`.

✅ **Teste suas funções antes de usar nos dados reais:**

```python
print(media([2, 4, 4, 4, 5, 5, 7, 9]))          # 5.0
print(mediana([7, 1, 3]))                       # 3
print(mediana([7, 1, 3, 10]))                   # 5.0
print(round(desvio_padrao([2, 4, 4, 4, 5, 5, 7, 9]), 4))   # 2.1381
```

## 🧭 Parte 2: passo a passo da análise

### 1. Carregar os dados

Crie `carregar(caminho)`, que devolve **três** coisas: a lista de respostas válidas (cada uma como **dicionário**), a lista de ids sem salário e a lista de outliers removidos.

```python
{'id': '1', 'cargo': 'Analista de Dados', 'nivel': 'Sênior', 'anos': 6,
 'uf': 'BA', 'modelo': 'Remoto', 'salario': 9200.0}
```

💡 Use `try/except ValueError` na conversão do salário e dos anos. Para anos vazios, guarde `None`.

### 2. Agrupar

A função mais útil do projeto. Ela recebe as respostas e o nome de um campo e devolve um dicionário **grupo → lista de salários**:

```python
agrupar(respostas, 'nivel')
# {'Sênior': [9200.0, 15400.0, ...], 'Pleno': [9300.0, ...], 'Júnior': [...], 'Especialista': [...]}
```

Com ela e com `resumo()`, você consegue montar **qualquer** tabela do relatório.

### 3. Tabelas, gráficos e rankings

- **Tabelas por cargo, nível e modelo de trabalho** (n, média, mediana, mín., máx.).
  - Cargos: ordenar pela **mediana**, do maior para o menor;
  - Níveis: ordem **lógica** (Júnior → Pleno → Sênior → Especialista). Dica: guarde essa ordem em uma `tuple`!
- **Gráfico de barras** da mediana por cargo: a maior barra tem 40 caracteres.
- **Top 5 estados** pela mediana e a **posição de PE** no ranking.
- **Histograma** em faixas de R$ 3.000. Para descobrir a faixa de um salário: `inicio = int(salario // 3000) * 3000`.

### 4. Correlação (experiência × salário)

A **correlação de Pearson** mede o quanto duas variáveis "andam juntas". Vai de **-1** (uma sobe e a outra desce) a **+1** (sobem juntas); perto de **0** significa que não há relação linear.

$$ r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2} \cdot \sqrt{\sum (y_i - \bar{y})^2}} $$

Aqui, `x` é `anos_experiencia` e `y` é o salário, **considerando só as respostas que têm anos informados**. Classifique: `r ≥ 0.7` é **forte**, `0.4 ≤ r < 0.7` é **moderada** e `r < 0.4` é **fraca**.

✅ Teste: `correlacao([1, 2, 3, 4], [10, 20, 30, 40])` deve dar `1.0`, ou `0.9999999999999999`. Esse "quase 1" é normal: computadores guardam números decimais com uma precisão limitada (pesquise *ponto flutuante*). Por isso, use `round(r, 2)` na hora de exibir.

### 5. Saídas

- Imprimir o relatório no terminal **e** salvar em `saida/relatorio_salarial.txt`;
- Salvar `saida/resumo_por_cargo.csv` (um cargo por linha, em ordem alfabética, valores com 2 casas):

```txt
cargo,n,media,mediana,minimo,maximo,desvio_padrao
Analista de BI,95,8157.37,7200.00,2850.00,20050.00,4233.91
Analista de Dados,221,8807.92,8000.00,3150.00,22000.00,4123.50
Cientista de Dados,118,11471.61,10375.00,4200.00,29900.00,5658.25
Engenheiro(a) de Dados,139,12637.77,11450.00,4700.00,28600.00,5837.55
Engenheiro(a) de Machine Learning,52,14813.46,12325.00,5650.00,34800.00,8321.92
```

## 🖥️ Exemplo de saída esperada

Confira os seus números com estes:

```txt
============================================================
RAIO-X SALARIAL DA ÁREA DE DADOS - PESQUISA 2025
============================================================

>> SOBRE OS DADOS
  Respostas válidas:              625
  Sem salário informado:          13
  Outliers removidos (> R$ 60.000): 2 -> ids 57, 402
  Cargos distintos:               5
  Estados (UF) representados:     10

>> PANORAMA GERAL
  Média:          R$ 10.563
  Mediana:        R$ 8.900
  Desvio padrão:  R$ 5.700
  Menor salário:  R$ 2.850
  Maior salário:  R$ 34.800

>> SALÁRIO POR CARGO (ordenado pela mediana)
  Grupo                                  N       Média     Mediana         Mín         Máx
  --------------------------------------------------------------------------------------
  Engenheiro(a) de Machine Learning     52   R$ 14.813   R$ 12.325    R$ 5.650   R$ 34.800
  Engenheiro(a) de Dados               139   R$ 12.638   R$ 11.450    R$ 4.700   R$ 28.600
  Cientista de Dados                   118   R$ 11.472   R$ 10.375    R$ 4.200   R$ 29.900
  Analista de Dados                    221    R$ 8.808    R$ 8.000    R$ 3.150   R$ 22.000
  Analista de BI                        95    R$ 8.157    R$ 7.200    R$ 2.850   R$ 20.050

>> SALÁRIO POR NÍVEL
  Grupo                                  N       Média     Mediana         Mín         Máx
  --------------------------------------------------------------------------------------
  Júnior                               213    R$ 5.554    R$ 5.300    R$ 2.850    R$ 9.300
  Pleno                                202    R$ 9.412    R$ 8.900    R$ 5.200   R$ 16.500
  Sênior                               146   R$ 15.107   R$ 14.475    R$ 9.000   R$ 27.250
  Especialista                          64   R$ 20.503   R$ 19.300   R$ 11.750   R$ 34.800

>> SALÁRIO POR MODELO DE TRABALHO
  Grupo                                  N       Média     Mediana         Mín         Máx
  --------------------------------------------------------------------------------------
  Remoto                               293   R$ 10.852    R$ 9.200    R$ 3.600   R$ 30.550
  Híbrido                              237   R$ 10.786    R$ 9.150    R$ 3.300   R$ 34.800
  Presencial                            95    R$ 9.117    R$ 7.800    R$ 2.850   R$ 30.250

>> MEDIANA POR CARGO
  Engenheiro(a) de Machine Learning   ████████████████████████████████████████ R$ 12.325
  Engenheiro(a) de Dados              █████████████████████████████████████ R$ 11.450
  Cientista de Dados                  ██████████████████████████████████ R$ 10.375
  Analista de Dados                   ██████████████████████████ R$ 8.000
  Analista de BI                      ███████████████████████ R$ 7.200

>> TOP 5 ESTADOS (mediana salarial)
  1º SP   R$ 10.150  (169 respostas)
  2º DF   R$ 10.100  (25 respostas)
  3º RJ    R$ 9.700  (47 respostas)
  4º PR    R$ 9.300  (44 respostas)
  5º BA    R$ 9.225  (44 respostas)
  ... PE aparece em 7º lugar, com mediana de R$ 8.550

>> DISTRIBUIÇÃO DOS SALÁRIOS (faixas de R$ 3.000)
  R$ 0 a R$ 2.999        1
  R$ 3.000 a R$ 5.999   ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 140
  R$ 6.000 a R$ 8.999   ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 173
  R$ 9.000 a R$ 11.999  ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 107
  R$ 12.000 a R$ 14.999 ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 78
  R$ 15.000 a R$ 17.999 ▇▇▇▇▇▇▇▇▇▇▇▇▇ 57
  R$ 18.000 a R$ 20.999 ▇▇▇▇▇▇▇▇ 33
  R$ 21.000 a R$ 23.999 ▇▇▇▇ 19
  R$ 24.000 a R$ 26.999 ▇ 6
  R$ 27.000 a R$ 29.999 ▇▇ 7
  R$ 30.000 a R$ 32.999  2
  R$ 33.000 a R$ 35.999  2

>> INSIGHTS AUTOMÁTICOS
  - Um(a) Sênior ganha, na mediana, 2.7x o salário de um(a) Júnior.
  - Correlação entre anos de experiência e salário: 0.80 (forte).
  - Remoto x Presencial (mediana): R$ 9.200 x R$ 7.800.
```

> 📌 Os valores em reais estão **sem centavos** no relatório (`f'{valor:,.0f}'` e depois a troca de `,` por `.`), mas **com 2 casas** no CSV.
> 📌 Pequenas diferenças de alinhamento são aceitáveis. **Os números, não.**

### 💡 Dica de alinhamento de tabelas

As f-strings aceitam largura e alinhamento: `<` à esquerda, `>` à direita.

```python
print(f"{'Cargo':<36}{'N':>4}{'Mediana':>12}")
print(f"{cargo:<36}{n:>4}{mediana_formatada:>12}")
```

## ✅ Checklist de entrega

- [ ] As funções `media`, `mediana`, `desvio_padrao` e `correlacao` foram implementadas à mão e passam nos testes da Parte 1
- [ ] Respostas inválidas e outliers são tratados conforme as regras
- [ ] O relatório é impresso e salvo em `saida/relatorio_salarial.txt`
- [ ] `saida/resumo_por_cargo.csv` foi gerado
- [ ] Os números batem com o exemplo
- [ ] README com as **respostas às perguntas de negócio** abaixo

## ❓ Perguntas de negócio (responda no README)

O código calcula; **quem interpreta é você**. Escreva de 1 a 3 frases para cada pergunta, sempre citando números:

1. Qual cargo tem a maior mediana salarial? A diferença para o menor é grande?
2. Por que a **média** geral (R$ 10.563) é maior que a **mediana** (R$ 8.900)? O que isso diz sobre a distribuição dos salários? *Dica: olhe o histograma.*
3. Trabalhar remoto paga mais? Os dados permitem afirmar que **o remoto causa** o salário maior, ou pode haver outra explicação? *Dica: pesquise "correlação não implica causalidade".*
4. Como Pernambuco se compara com os outros estados?
5. Se você fosse dar **um conselho** para alguém que está entrando na área, com base nesses dados, qual seria?

## 🏆 Desafios bônus

1. **Filtro interativo:** um menu que pergunta cargo e/ou UF e mostra o `resumo()` só daquele recorte (ex.: "Cientista de Dados em PE"). Trate entradas inválidas.
2. **Tabela cruzada:** a mediana para cada combinação **cargo × nível**, em formato de matriz.
3. **Quartis e outliers estatísticos:** calcule Q1 e Q3 e identifique outliers pela regra do IQR (abaixo de `Q1 − 1,5·IQR` ou acima de `Q3 + 1,5·IQR`). Os dois outliers removidos aparecem? Aparecem outros?
4. **Impacto dos outliers:** mostre lado a lado média, mediana e desvio padrão **com** e **sem** os outliers.
5. **Comparar com uma biblioteca:** depois da aula de Módulos, compare seus resultados com `statistics.median()` e `statistics.stdev()`. Bateu?

## 💼 Para o seu portfólio

> *"Realizei uma análise exploratória de uma pesquisa salarial com 640 profissionais de dados, implementando do zero as funções estatísticas (média, mediana, desvio padrão e correlação de Pearson), tratando dados ausentes e outliers e comunicando os resultados com tabelas e gráficos em texto."*

Esse projeto rende um ótimo **post no LinkedIn**: um print do relatório e 3 descobertas em tópicos. Só deixe claro que os dados são **fictícios**, criados para fins didáticos.
