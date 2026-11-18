# NExT 26.2 | Fundamentos de Python Aplicado a Dados

![CESAR School](/cesar_school.png)

## Aula 11 - NumPy na Análise de Dados

### Na aula de hoje

* Revisão rápida da aula anterior;
* Agregações em matrizes com `axis`;
* Máscaras booleanas e combinação de condições (`&`, `|` e `~`);
* Encontrando posições com `argmax` e `argmin`;
* Broadcasting;
* Exemplo completo: análise de notas;
* Lendo e salvando dados com `np.loadtxt` e `np.savetxt`;
* Boas práticas no uso de NumPy.

---

## 🔁 Revisão rápida

Na [Aula 10](/aula10/README.md) vimos que:

* Um array NumPy (`ndarray`) guarda valores do mesmo tipo e permite **operações vetorizadas**;
* Podemos inspecionar a estrutura com `ndim`, `shape`, `size` e `dtype`;
* Acessamos elementos com índices e fatias, inclusive em 2D: `notas[linha, coluna]`, `notas[:, 1]`;
* Funções de agregação como `sum`, `mean`, `min`, `max` e `std` resumem muitos valores em um só.

```python
import numpy as np

notas = np.array([7.5, 8.0, 6.5, 9.0, 10.0])

print(notas + 0.5)   # vetorização
print(notas[1:3])    # fatiamento
print(notas.mean())  # agregação
```

Hoje vamos usar essas ferramentas para **responder perguntas sobre os dados**: qual a média de cada estudante? Quem foi aprovado? Qual o dia com mais vendas?

---

## Entendendo `axis`

O parâmetro `axis` é um dos pontos que mais confunde no começo.

Vamos usar uma tabela de notas:

```python
notas = np.array([
    [8.0, 7.5, 9.0],
    [6.5, 8.0, 7.0],
    [9.5, 8.5, 10.0],
    [8.5, 5.6, 7.8],
    [7.5, 9.0, 9.0]
])
```

Imagine que:

* Cada linha representa um estudante;
* Cada coluna representa uma avaliação.

```txt
             Avaliação 1   Avaliação 2   Avaliação 3
Estudante 1      8.0           7.5           9.0
Estudante 2      6.5           8.0           7.0
Estudante 3      9.5           8.5          10.0
Estudante 4      8.5           5.6           7.8
Estudante 5      7.5           9.0           9.0
```

### Média geral

```python
print(notas.mean())
```

Aqui o NumPy calcula a média de todos os valores.

### Média por coluna

```python
print(notas.mean(axis=0))
```

Saída:

```python
[8.   7.72 8.56]
```

`axis=0` percorre as linhas e calcula o resultado por coluna.

Pergunta-guia:

> Qual foi a média da turma em cada avaliação?

### Média por linha

```python
print(notas.mean(axis=1))
```

Saída:

```python
[8.16666667 7.16666667 9.33333333 7.3        8.5       ]
```

`axis=1` percorre as colunas e calcula o resultado por linha.

Logo...

> `axis=0` → calcula ao longo das linhas e retorna um resultado por coluna\
> `axis=1` → calcula ao longo das colunas e retorna um resultado por linha

---

## Máscaras booleanas

Máscaras booleanas são uma forma muito útil de filtrar dados.

```python
notas = np.array([4.5, 7.0, 8.5, 5.0, 9.0])
```

Vamos descobrir quais notas são maiores ou iguais a 7:

```python
aprovadas = notas >= 7
print(aprovadas)
#[False  True  True False  True]
```

Agora podemos usar essa máscara para filtrar o array:

```python
print(notas[aprovadas])
#[7.  8.5 9. ]
```

Podemos fazer direto:

```python
print(notas[notas >= 7])
```

Também podemos contar quantos valores atendem à condição:

```python
print((notas >= 7).sum())
```

Como `True` vale 1 e `False` vale 0 em operações numéricas, a soma indica quantos itens passaram no teste.

### Combinando condições

Para combinar condições em NumPy, usamos operadores próprios:

| Operador | Significado | Equivalente em Python puro |
| -------- | ----------- | -------------------------- |
| `&`      | E           | `and`                      |
| `\|`     | OU          | `or`                       |
| `~`      | NÃO         | `not`                      |

```python
notas = np.array([4.5, 7.0, 8.5, 5.0, 9.0])

# notas entre 5 e 8 (inclusive)
print(notas[(notas >= 5) & (notas <= 8)])
#[7. 5.]

# notas muito baixas ou muito altas
print(notas[(notas < 5) | (notas > 8)])
#[4.5 8.5 9. ]

# notas que NÃO são de aprovação
aprovadas = notas >= 7
print(notas[~aprovadas])
#[4.5 5. ]
```

> ⚠️ Cada condição deve ficar entre parênteses. Sem eles, o Python tenta resolver `5 & notas` antes da comparação e o resultado sai errado (ou gera erro).

### Filtrando um array a partir de outro

Uma máscara criada a partir de um array pode ser usada em outro array **do mesmo tamanho**. Isso é muito útil quando temos dados relacionados:

```python
nomes = np.array(['Ana', 'Bruno', 'Carlos', 'Duda', 'Eva'])
notas = np.array([4.5, 7.0, 8.5, 5.0, 9.0])

print(nomes[notas >= 7])
#['Bruno' 'Carlos' 'Eva']
```

A máscara `notas >= 7` diz *quais posições* passaram no teste; aplicada em `nomes`, ela devolve os nomes dessas posições.

---

## Encontrando posições: `argmax` e `argmin`

`max()` responde **qual é** o maior valor. Muitas vezes, porém, queremos saber **onde** ele está, para descobrir a quem ele pertence.

```python
nomes = np.array(['Ana', 'Bruno', 'Carlos', 'Duda'])
medias = np.array([8.2, 6.2, 9.0, 5.0])

print(medias.max())        # 9.0
print(np.argmax(medias))   # 2

indice = np.argmax(medias)
print(nomes[indice], medias[indice])
#Carlos 9.0
```

Da mesma forma, `np.argmin` retorna a posição do menor valor.

Em matrizes, também podemos usar `axis`:

```python
vendas = np.array([
    [1200, 1500, 1100],
    [900,  1000, 1300]
])

print(np.argmax(vendas, axis=1))
#[1 2]
```

Para cada linha (vendedor), o NumPy informa em qual coluna (dia) está a maior venda.

> ⚠️ Se houver empate, `argmax` e `argmin` retornam a **primeira** posição encontrada.

---

## Broadcasting

**Broadcasting** é o mecanismo que permite ao NumPy realizar operações entre arrays de formatos diferentes, desde que eles sejam compatíveis.

O exemplo mais simples é somar um número a um array:

```python
valores = np.array([10, 20, 30])
print(valores + 5)
#[15 25 35]
```

O número `5` foi aplicado a todos os elementos.

Agora veja um exemplo com matriz:

```python
notas = np.array([
    [8.0, 7.5, 9.0],
    [6.5, 8.0, 7.0],
    [9.5, 8.5, 10.0]
])

pesos = np.array([2, 3, 5])

notas_ponderadas = notas * pesos
print(notas_ponderadas)
#[[16.  22.5 45. ]
# [13.  24.  35. ]
# [19.  25.5 50. ]]
```

O array `pesos` tem 3 valores. A matriz `notas` tem 3 colunas. O NumPy consegue aplicar os pesos em cada linha.

Depois podemos calcular uma média ponderada:

```python
media_ponderada = notas_ponderadas.sum(axis=1) / pesos.sum()
print(media_ponderada)
#[8.35 7.2  9.45]
```

---

## Exemplo: Análise de Notas

Agora vamos juntar os conceitos.

### Dados iniciais

```python
import numpy as np

nomes = np.array(['Ana', 'Bruno', 'Carlos', 'Duda'])

notas = np.array([
    [8.0, 7.5, 9.0],
    [6.0, 5.5, 7.0],
    [9.0, 8.5, 9.5],
    [4.0, 6.0, 5.0]
])
```

Cada linha representa um estudante.
Cada coluna representa uma avaliação.

### Média de cada estudante

```python
medias = notas.mean(axis=1)
print(medias)
```

### Situação de aprovação

```python
aprovados = medias >= 7
print(aprovados)
```

### Mostrar apenas estudantes aprovados

```python
print(nomes[aprovados])
print(medias[aprovados])
```

### Mostrar estudantes em recuperação

```python
recuperacao = (medias >= 5) & (medias < 7)

print(nomes[recuperacao])
print(medias[recuperacao])
```

> ⚠️ Em NumPy, para combinar condições, usamos `&` em vez de `and`, e cada condição deve ficar entre parênteses.

### Mostrar estudantes reprovados

```python
reprovados = medias < 5

print(nomes[reprovados])
print(medias[reprovados])
```

---

## Carregando dados simples com NumPy

Em aulas anteriores, vocês trabalharam com arquivos CSV usando o módulo `csv`.

O NumPy também possui recursos para carregar dados numéricos de arquivos.

Vamos começar com um exemplo simples.

Imagine um arquivo `notas.csv` com o seguinte conteúdo:

```csv
8.0,7.5,9.0
6.0,5.5,7.0
9.0,8.5,9.5
4.0,6.0,5.0
```

Podemos carregar esse arquivo assim:

```python
import numpy as np

notas = np.loadtxt('notas.csv', delimiter=',')
print(notas)
```

Depois podemos calcular:

```python
print(notas.mean())
print(notas.mean(axis=0))
print(notas.mean(axis=1))
```

> ⚠️ `np.loadtxt` funciona melhor quando os dados são bem organizados e numéricos. Para arquivos CSV com cabeçalho, texto, valores ausentes ou dados mistos, normalmente usamos outras estratégias, como `csv`, `pandas` ou limpeza prévia dos dados.


### Salvando resultados com `np.savetxt`

Depois de calcular um resultado, podemos gravá-lo em um arquivo:

```python
medias = notas.mean(axis=1)

np.savetxt('medias.csv', medias, delimiter=',', fmt='%.2f')
```

O parâmetro `fmt` define o formato de cada número. Aqui, `'%.2f'` grava os valores com duas casas decimais.

Também é possível adicionar um cabeçalho:

```python
np.savetxt('medias.csv', medias, delimiter=',', fmt='%.2f', header='media', comments='')
```

> 💡 O parâmetro `comments=''` evita que o NumPy coloque um `#` antes do cabeçalho.

---

## Boas práticas com NumPy

1. **Observe o formato dos dados com `shape` antes de usar `axis` ou broadcasting**

   Muitos erros acontecem porque o array não está no formato esperado.

2. **Coloque cada condição entre parênteses**

   `(medias >= 5) & (medias < 7)` funciona; `medias >= 5 & medias < 7` não faz o que você espera.

3. **Dê nomes às máscaras**

   `aprovados = medias >= 7` deixa o código mais legível do que repetir a condição em vários lugares.

4. **Mantenha arrays relacionados alinhados**

   Se `nomes[i]` é o estudante da linha `i` de `notas`, qualquer filtro aplicado em um deve ser aplicado no outro com a mesma máscara.

5. **Cuidado com cópias e alterações**

   Algumas operações podem gerar cópias; outras podem gerar visualizações dos mesmos dados. Uma fatia como `notas[0]` é uma *visualização*: alterá-la altera `notas`. Se quiser um array independente, use `.copy()`.

   ```python
   primeira_linha = notas[0].copy()
   ```

6. **Não use NumPy para tudo**

   Para arquivos com cabeçalho, texto e valores ausentes, o `pandas` costuma ser uma escolha melhor. NumPy brilha com dados numéricos bem organizados.

---

## Resumo dos principais recursos

| Recurso          | Para que serve                         | Exemplo                                  |
| ---------------- | -------------------------------------- | ---------------------------------------- |
| `axis=0`         | Agregar por coluna                     | `notas.mean(axis=0)`                     |
| `axis=1`         | Agregar por linha                      | `notas.mean(axis=1)`                     |
| Máscara booleana | Filtrar dados por condição             | `notas[notas >= 7]`                      |
| `&`              | E lógico entre condições               | `(x >= 5) & (x < 7)`                     |
| `\|`             | OU lógico entre condições              | `(x < 5) \| (x > 9)`                     |
| `~`              | Negar uma máscara                      | `x[~aprovados]`                          |
| `.sum()` em máscara | Contar quantos valores são `True`   | `(notas >= 7).sum()`                     |
| `np.argmax()`    | Posição do maior valor                 | `np.argmax(medias)`                      |
| `np.argmin()`    | Posição do menor valor                 | `np.argmin(medias)`                      |
| Broadcasting     | Operar arrays de formatos compatíveis  | `notas * pesos`                          |
| `np.loadtxt()`   | Ler arquivo numérico simples           | `np.loadtxt('notas.csv', delimiter=',')` |
| `np.savetxt()`   | Salvar array em arquivo                | `np.savetxt('saida.csv', x, fmt='%.2f')` |

---

## 🧱 Exercícios fundamentais

### [Exercício 01] Aprovados e recuperação

Dado o array:

```python
notas = np.array([4.5, 7.0, 8.5, 5.0, 9.0, 6.5])
```

Crie filtros para exibir:

* Notas maiores ou iguais a 7;
* Notas entre 5 e 6.9;
* Notas menores que 5;
* Quantidade de estudantes aprovados.

---

### [Exercício 02] Matriz de notas

Dado o array:

```python
notas = np.array([
    [8.0, 7.5, 9.0],
    [6.5, 8.0, 7.0],
    [9.5, 8.5, 10.0],
    [5.0, 6.0, 6.5]
])
```

Calcule:

* A média geral;
* A média de cada estudante;
* A média de cada avaliação;
* A maior nota da matriz;
* A menor nota da matriz.

---

### [Exercício 03] Pesos das avaliações

Considere que as três avaliações possuem os seguintes pesos:

```python
pesos = np.array([2, 3, 5])
```

Usando a matriz de notas do exercício anterior, calcule a média ponderada de cada estudante.

Dica:

```python
notas_ponderadas = notas * pesos
```

Depois pense:

* Por que essa multiplicação funciona?
* O que aconteceria se `pesos` tivesse apenas 2 valores?

---

### [Exercício 04] Controle de estoque

Uma loja de informática tem os seguintes dados:

```python
produtos = np.array(['Teclado', 'Mouse', 'Monitor', 'Cadeira', 'Webcam', 'Headset'])
precos = np.array([150, 80, 1200, 900, 250, 350])
estoque = np.array([25, 5, 8, 12, 3, 40])
```

Usando máscaras booleanas, exiba:

* Os produtos que precisam de reposição (estoque menor que 10);
* Os produtos caros (preço maior que 500) **e** com estoque menor que 10 — esses têm prioridade;
* Os produtos baratos (preço menor que 100) **ou** com estoque maior que 30 — candidatos a promoção;
* Os produtos que **não** precisam de reposição (use `~`);
* O valor total em estoque da loja (preço × quantidade de cada produto, somados).

---

### [Exercício 05] Onde está o máximo?

Dados:

```python
cidades = np.array(['Recife', 'Olinda', 'Caruaru', 'Petrolina', 'Garanhuns'])
dias = np.array(['Seg', 'Ter', 'Qua', 'Qui', 'Sex'])

temperaturas = np.array([
    [30.5, 31.0, 29.8, 32.1, 31.4],
    [30.0, 30.8, 29.5, 31.6, 31.0],
    [27.2, 28.0, 26.9, 29.0, 28.4],
    [33.8, 34.5, 35.2, 34.0, 33.1],
    [24.0, 25.1, 23.8, 26.4, 25.0]
])
```

Cada linha representa uma cidade e cada coluna, um dia da semana.

Exiba:

* A temperatura média de cada cidade;
* A cidade mais quente e a mais fria (pela média), usando `np.argmax` e `np.argmin`;
* O dia mais quente da semana considerando a média de todas as cidades;
* Para cada cidade, o dia em que ela registrou a maior temperatura.

> 💡 `np.argmax` também aceita `axis`. Experimente `np.argmax(temperaturas, axis=1)`.

---

### [Exercício 06] Consumo de energia

O arquivo [`consumo_energia.csv`](/aula11/exercicios/consumo_energia.csv) contém o consumo mensal, em kWh, de 4 casas ao longo de 6 meses. Cada linha é uma casa e cada coluna é um mês.

```csv
150,160,155,170,180,175
220,210,230,240,235,250
90,95,100,85,80,92
300,310,295,320,330,315
```

Usando `np.loadtxt`:

* Carregue os dados e exiba o `shape`;
* Calcule o consumo total de cada casa;
* Calcule o consumo médio de cada mês;
* Descubra qual mês teve o maior consumo total (`argmax`);
* Exiba quais casas (Casa 1, Casa 2, ...) têm consumo médio acima de 200 kWh;
* Salve o consumo total de cada casa em um arquivo `resumo_consumo.csv` usando `np.savetxt`.

---

## 🚀 Mini Projeto 8: PyNotas NumPy

### Contexto

A coordenação de um curso recebeu uma tabela simples de notas de uma turma. Cada linha representa um estudante e cada coluna representa uma avaliação.

A equipe precisa de um pequeno programa que ajude a gerar um resumo da situação da turma.

### Dados iniciais

Use os dados abaixo diretamente no código:

```python
import numpy as np

nomes = np.array([
    'Ana',
    'Bruno',
    'Carlos',
    'Duda',
    'Eduardo',
    'Fernanda'
])

notas = np.array([
    [8.0, 7.5, 9.0],
    [6.0, 5.5, 7.0],
    [9.0, 8.5, 9.5],
    [4.0, 6.0, 5.0],
    [7.0, 7.0, 7.0],
    [5.0, 4.5, 6.0]
])
```

### O desafio

Crie um programa que calcule e exiba:

1. A média de cada estudante (com nome);
2. A média da turma em cada avaliação;
3. A média geral da turma;
4. O nome dos estudantes aprovados (média maior ou igual a 7);
5. O nome dos estudantes em recuperação (média maior ou igual a 5 e menor que 7);
6. O nome dos estudantes reprovados (média menor que 5);
7. A maior média da turma (com nome);
8. A menor média da turma (com nome).

### Regras

* Use NumPy;
* Use máscaras booleanas;
* Use `axis` para calcular médias por linha e por coluna;
* Evite resolver tudo com `for`;
* Organize o código com variáveis claras;
* Mostre as informações com mensagens compreensíveis.

### Exemplo de saída esperada

```txt
Médias dos estudantes:
Ana: 8.17
Bruno: 6.17
Carlos: 9.00
Duda: 5.00
Eduardo: 7.00
Fernanda: 5.17

Média por avaliação:
Avaliação 1: 6.50
Avaliação 2: 6.50
Avaliação 3: 7.25

Média geral da turma: 6.75

Aprovados: Ana, Carlos, Eduardo
Recuperação: Bruno, Duda, Fernanda
Reprovados: nenhum estudante

Maior média: Carlos (9.00)
Menor média: Duda (5.00)
```

### ✨ Extra

Depois de implementar este desafio, crie um módulo que gere um arquivo com dados sintéticos de 500 estudantes e adapte o programa atual para ler os dados desse arquivo.\
O início do arquivo deve ter os mesmos dados deste exercício. Os demais dados devem ser gerados de forma aleatória, respeitando a lógica do sistema, incluindo nomes e notas.

---

## 🚀 Mini Projeto 9: Análise de Vendas

### Contexto

Uma loja registrou o total de vendas de 4 vendedores ao longo de 5 dias.

```python
vendedores = np.array(['Ana', 'Bruno', 'Carlos', 'Duda'])

dias = np.array(['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta'])

vendas = np.array([
    [1200, 1500, 1100, 1800, 2000],
    [900,  1000, 950,  1200, 1300],
    [2000, 2100, 1900, 2200, 2500],
    [700,  850,  800,  950,  1000]
])
```

### O desafio

Calcule:

1. Total vendido por vendedor;
2. Total vendido por dia;
3. Média de vendas por vendedor;
4. Vendedor com maior total de vendas;
5. Dia com maior venda total;
6. Vendedores que venderam mais de 7000 no total.

### Dicas

* Use `sum(axis=1)` para total por vendedor;
* Use `sum(axis=0)` para total por dia;
* Use máscaras booleanas para filtrar vendedores;
* Use `np.argmax()` para encontrar a posição do maior valor.

### ✨ Extra

Depois de implementar este desafio, crie um módulo que gere um arquivo com dados sintéticos de 50 vendedores e adapte o programa atual para ler os dados desse arquivo.\
O início do arquivo deve ter os mesmos dados deste exercício. Os demais dados devem ser gerados de forma aleatória, respeitando a lógica do sistema, incluindo nomes e vendas.\
No final o programa deve salvar o relatório em um arquivo de resultados.
