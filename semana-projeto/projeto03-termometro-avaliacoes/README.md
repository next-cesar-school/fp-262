# 🌡️ Projeto 3: Termômetro de Avaliações

> **Área:** Ciência de Dados / Processamento de Linguagem Natural (NLP) · **Nível:** ⭐⭐⭐ · **Tempo estimado:** 7 a 10 horas
> **Conteúdos usados:** strings e `for` (Aula 04), funções (Aula 05), arquivos (Aula 06), exceções (Aula 07), `set`/`dict`/`tuple` (Aula 08). É a evolução direta do ⌨️ **Teclado Dominante**.

## 📖 Contexto

A **Loja NExT** recebe centenas de comentários de clientes por mês. O time de produto quer saber, **sem ler um por um**:

- quais produtos estão agradando e quais estão gerando reclamação;
- quais palavras aparecem mais quando o cliente está feliz ou irritado;
- e se dá para **classificar automaticamente** um comentário novo como positivo, negativo ou neutro.

Isso se chama **análise de sentimento**, uma das aplicações mais comuns de NLP. Hoje existem modelos de *machine learning* enormes para isso, mas a técnica clássica, e ótima para começar, é a **análise por léxico**: uma lista de palavras positivas e outra de negativas, e uma contagem de pontos.

> 💬 O mais importante deste projeto não é só classificar: é **medir o quanto o seu classificador acerta**. Todo modelo de ciência de dados precisa ser avaliado, e você vai fazer isso com **acurácia** e **matriz de confusão**, os mesmos conceitos usados em machine learning.

## 🎯 Objetivo

1. Ler e limpar 900 comentários de clientes;
2. Classificar cada comentário pelo **texto**, usando um léxico;
3. Comparar com o sentimento "verdadeiro", que vem da **nota** dada pelo cliente;
4. Gerar um relatório com desempenho, ranking de produtos e palavras mais frequentes;
5. Oferecer um **modo interativo** para classificar comentários digitados pelo usuário.

## 📦 Dados de entrada

Na pasta [`dados/`](dados/):

| Arquivo | Conteúdo |
| ------- | -------- |
| `avaliacoes.csv` | 900 avaliações: `id,produto,nota,comentario` |
| `lexico_positivo.txt` | Uma palavra positiva por linha (ex.: `adorei`, `excelente`) |
| `lexico_negativo.txt` | Uma palavra negativa por linha (ex.: `péssimo`, `quebrou`) |
| `stopwords.txt` | Palavras muito comuns, sem significado próprio (ex.: `de`, `o`, `com`) |

```txt
id,produto,nota,comentario
1,Mochila Esportiva,1,A QUALIDADE É HORRÍVEL E QUEBROU NA PRIMEIRA SEMANA. DECEPCIONADO COM O SOM, FRACO DEMAIS...
2,Fone Bluetooth,3,O atendimento é normal, como esperado!!
3,Mochila Esportiva,5,Adorei o produto, ficou excelente
```

### ⚠️ A primeira armadilha: vírgulas dentro do comentário

Olhe a linha 1: o **comentário tem vírgulas**. Se você fizer `linha.split(',')`, ele vai ser quebrado em vários pedaços. Como o comentário é a **última** coluna, a solução é limitar o número de divisões:

```python
linha = '1,Mochila Esportiva,1,Horrível, quebrou, fraco demais'
print(linha.split(','))      # ['1', 'Mochila Esportiva', '1', 'Horrível', ' quebrou', ' fraco demais']  ❌
print(linha.split(',', 3))   # ['1', 'Mochila Esportiva', '1', 'Horrível, quebrou, fraco demais']    ✅
```

O segundo argumento do `split` é o **número máximo de cortes**. Com 3 cortes, saem 4 pedaços.

### Notas inválidas

Algumas avaliações têm a nota vazia ou escrita por extenso (`cinco`). Elas devem ser **descartadas** e **contadas**. Nota válida é um **inteiro de 1 a 5**.

## 🧭 Passo a passo

### Etapa 1: Carregar o léxico em `set`s

```python
def carregar_palavras(caminho):
    """Lê um arquivo com uma palavra por linha e devolve um set."""
```

Por que `set` e não `list`? Porque você vai perguntar `palavra in positivas` **milhares de vezes**, e em um `set` essa busca é praticamente instantânea. É o mesmo raciocínio do Teclado Dominante.

### Etapa 2: Limpar o texto

```python
def limpar_texto(texto):
    """Converte para minúsculas, troca tudo que não é letra por espaço e devolve a lista de palavras."""

limpar_texto('PÉSSIMO, veio com defeito!!')   # ['péssimo', 'veio', 'com', 'defeito']
```

💡 `caractere.isalpha()` devolve `True` para letras, **inclusive as acentuadas** (`'é'.isalpha()` é `True`).

### Etapa 3: Pontuar e classificar

Regra básica: **+1** para cada palavra do léxico positivo e **-1** para cada palavra do léxico negativo.

```python
def pontuar(palavras, positivas, negativas):
    ...

def classificar(pontos):
    # pontos > 0  -> 'positivo'
    # pontos < 0  -> 'negativo'
    # pontos == 0 -> 'neutro'
```

| Comentário | Palavras no léxico | Pontos | Classe |
| ---------- | ------------------ | :----: | ------ |
| `Adorei o produto, ficou excelente` | adorei (+1), excelente (+1) | +2 | positivo |
| `Péssimo, a entrega veio com defeito` | péssimo (-1), defeito (-1) | -2 | negativo |
| `Produto mediano, nada demais` | nenhuma | 0 | neutro |

### Etapa 4: O "gabarito" vem da nota

Para saber se o classificador acertou, precisamos do sentimento **real**. Vamos considerar que a nota dada pelo cliente representa isso:

| Nota | Sentimento real |
| :--: | --------------- |
| 4 ou 5 | positivo |
| 3 | neutro |
| 1 ou 2 | negativo |

### Etapa 5: Avaliar o classificador

**Acurácia** é a fração de acertos: `acertos ÷ total`.

A **matriz de confusão** mostra **onde** o modelo erra. Cada linha é o sentimento **real** e cada coluna, o **previsto**. A diagonal são os acertos.

```txt
                 previsto: positivo   neutro   negativo
real: positivo            ✅ acerto    erro      erro
real: neutro                 erro    ✅ acerto   erro
real: negativo               erro      erro    ✅ acerto
```

💡 Um **dicionário de dicionários** é perfeito para isso:

```python
CLASSES = ('positivo', 'neutro', 'negativo')
matriz = {}
for real in CLASSES:
    matriz[real] = {}
    for previsto in CLASSES:
        matriz[real][previsto] = 0

# para cada avaliação:
matriz[sentimento_real][sentimento_previsto] += 1
```

### Etapa 6: Melhorar o modelo com o tratamento de negação

Rode o classificador e olhe os erros. Você vai encontrar casos como:

- `Não gostei, nada bom` → `gostei` (+1) e `bom` (+1) dão **+2 (positivo)**, mas a nota é 1! 😱

Melhore a função `pontuar`: **se a palavra anterior for `não`, `nem`, `nada` ou `nunca`, inverta o sinal** da palavra atual.

```python
pontuar(palavras, positivas, negativas, tratar_negacao=True)
```

Agora `não gostei` vale **-1** e `nada bom` vale **-1**, totalizando **-2 (negativo)**. ✅

Mostre no relatório a acurácia **antes e depois** dessa melhoria. É assim que se trabalha em ciência de dados: hipótese → mudança → **medição**.

> 📌 A partir daqui, todas as outras seções do relatório usam a versão **com** negação.

### Etapa 7: Ranking de produtos e palavras frequentes

- **Ranking de produtos:** para cada produto, o % de comentários classificados como positivos e como negativos, a nota média e a quantidade de avaliações. Ordene pelo % de positivos.
  - O **termômetro** usa um 🟩 para cada 10% de positivos e um 🟥 para cada 10% de negativos (`round(pct / 10)`).
- **Palavras mais frequentes:** conte as palavras das avaliações **realmente** positivas (pela nota) e **realmente** negativas, **ignorando** stopwords e palavras com 2 letras ou menos. Mostre as 8 mais frequentes, marcando `(+)` ou `(-)` quando a palavra estiver no léxico.

### Etapa 8: Saídas

1. Relatório no terminal **e** em `saida/relatorio_sentimento.txt`;
2. `saida/avaliacoes_classificadas.csv`, separado por **`;`** (pense: por que não vírgula?):

```txt
id;produto;nota;sentimento_real;pontuacao;sentimento_previsto;acertou;comentario
1;Mochila Esportiva;1;negativo;-4;negativo;sim;A QUALIDADE É HORRÍVEL E QUEBROU NA PRIMEIRA SEMANA. DECEPCIONADO COM O SOM, FRACO DEMAIS...
2;Fone Bluetooth;3;neutro;0;neutro;sim;O atendimento é normal, como esperado!!
3;Mochila Esportiva;5;positivo;2;positivo;sim;Adorei o produto, ficou excelente
```

3. **Modo interativo** ao final: o usuário digita comentários até escrever `sair`. Use `try/except` para `EOFError` e `KeyboardInterrupt` (o **Ctrl+C**), assim o programa termina de forma elegante, como no exercício 1068 da Aula 07.

## 🖥️ Exemplo de saída esperada

```txt
==========================================================
TERMÔMETRO DE AVALIAÇÕES - LOJA NExT
==========================================================

Avaliações analisadas: 876  |  descartadas (nota inválida): 24
Léxico: 24 palavras positivas, 23 negativas, 53 stopwords

>> DESEMPENHO DO CLASSIFICADOR (comparado com a nota)
  Acurácia sem tratar negação: 82.1%
  Acurácia COM negação:        84.9%

  Matriz de confusão (linhas = real pela nota | colunas = previsto pelo texto)
                positivo    neutro  negativo
  positivo           383        37        30
  neutro              19       109        14
  negativo             0        32       252

>> RANKING DE PRODUTOS (% de comentários positivos)
  Produto                Positivos  Negativos  Nota média    N  Termômetro
  Cafeteira                  66.4%      16.0%        3.94  119  🟩🟩🟩🟩🟩🟩🟩🟥🟥
  Luminária LED              66.1%      16.5%        4.03  115  🟩🟩🟩🟩🟩🟩🟩🟥🟥
  Fone Bluetooth             55.4%      22.8%        3.59  101  🟩🟩🟩🟩🟩🟩🟥🟥
  Caderno Inteligente        50.0%      34.8%        3.46  112  🟩🟩🟩🟩🟩🟥🟥🟥
  Mochila Esportiva          42.2%      34.3%        3.09  102  🟩🟩🟩🟩🟥🟥🟥
  Tênis de Corrida           37.5%      35.6%        3.33  104  🟩🟩🟩🟩🟥🟥🟥🟥
  Smartwatch                 23.9%      58.1%        2.52  117  🟩🟩🟥🟥🟥🟥🟥🟥
  Caixa de Som               23.6%      52.8%        2.55  106  🟩🟩🟥🟥🟥🟥🟥

>> PALAVRAS MAIS FREQUENTES (sem stopwords)
  Em avaliações positivas: bom (+) 122, compra     89, recomendo (+) 87, excelente (+) 76, funciona (+) 73, qualidade     66, gostei (+) 56, produto     52
  Em avaliações negativas: não     73, fraco (-) 56, ruim (-) 52, defeito (-) 45, produto     42, pior (-) 37, compra     37, quebrou (-) 36

>> EXEMPLOS DE ERROS DO CLASSIFICADOR (para investigar)
  [nota 1 | previsto neutro] Bonito, mas parou de funcionar
  [nota 1 | previsto neutro] Bonito, mas parou de funcionar...
  [nota 5 | previsto neutro] Não é ruim, gostei!!
  [nota 5 | previsto negativo] Achei que seria fraco, mas não é...

Modo interativo - digite um comentário (ou "sair"):
> O produto chegou rápido e é excelente
  Pontuação: +2 -> POSITIVO
> Não gostei, veio com defeito
  Pontuação: -2 -> NEGATIVO
> sair
Até mais!
```

> 💡 Para mostrar o sinal na pontuação (`+2`, `-2`), use `f'{pontos:+d}'`.
> 💡 Para os erros, basta filtrar as avaliações em que `previsto != real` e mostrar as 4 primeiras.

## ✅ Checklist de entrega

- [ ] O CSV é lido corretamente, sem quebrar os comentários que têm vírgula
- [ ] Notas inválidas são descartadas e contadas
- [ ] O léxico e as stopwords são carregados em `set`s
- [ ] A acurácia é mostrada **sem** e **com** tratamento de negação
- [ ] A matriz de confusão foi montada com dicionário
- [ ] Ranking de produtos e palavras frequentes aparecem no relatório
- [ ] `saida/relatorio_sentimento.txt` e `saida/avaliacoes_classificadas.csv` são gerados
- [ ] O modo interativo termina com `sair` **e** com Ctrl+C, sem *traceback*
- [ ] README com a análise dos erros (veja abaixo)

## 🔬 Análise crítica (responda no README)

1. Olhe a matriz de confusão: qual é o **erro mais comum** do classificador? Por que você acha que isso acontece?
2. Leia os comentários em que o modelo errou (filtre `acertou = não` no CSV). Encontre **3 tipos diferentes** de erro. *Dicas: ironia, "mas", palavras que não estão no léxico...*
3. A palavra `não` é a mais frequente nas avaliações negativas, mas ela **não está** no léxico negativo. Seria uma boa ideia colocá-la? Teste e meça!
4. A nota é um gabarito perfeito? Pense em um cliente que dá nota 5 e escreve "chegou atrasado, mas o produto é ótimo".
5. Se a acurácia fosse 99%, você desconfiaria? Por quê?

## 🏆 Desafios bônus

1. **Melhore o léxico:** adicione palavras aos arquivos `.txt` e **meça** se a acurácia subiu. Documente no README o que funcionou e o que não funcionou (o que não funcionou também é resultado!).
2. **Intensificadores:** faça `muito`, `super` e `demais` dobrarem o peso da palavra seguinte ("muito bom" = +2).
3. **Precisão e recall:** para a classe `negativo`, calcule **precisão** (dos que o modelo chamou de negativos, quantos eram mesmo?) e **recall** (dos negativos de verdade, quantos o modelo encontrou?). Pesquise esses conceitos: eles vão aparecer muito em machine learning.
4. **"Mas" muda tudo:** em "Bonito, mas parou de funcionar", o que vem **depois** do "mas" costuma importar mais. Implemente uma regra para isso e meça.
5. **Nuvem de palavras em texto:** mostre as 15 palavras mais frequentes com barras proporcionais, como no histograma do Projeto 2.

## 💼 Para o seu portfólio

> *"Desenvolvi do zero, em Python puro, um classificador de sentimento baseado em léxico para 900 avaliações de clientes, com limpeza de texto, tratamento de negação (+2,8 p.p. de acurácia), avaliação por matriz de confusão e ranking de satisfação por produto."*

Recrutadores adoram ver que você **mediu** e **iterou**. Na seção de resultados do README, mostre a tabela "versão do modelo × acurácia" com cada melhoria que você testou.
