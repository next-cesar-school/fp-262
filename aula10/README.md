# NExT 26.2 | Fundamentos de Python Aplicado a Dados

![CESAR School](/cesar_school.png)

## Aula 10 - Fundamentos de NumPy

### Na aula de hoje

* O que é o NumPy;
* NumPy em análise de dados;
* Diferenças entre listas Python e arrays NumPy;
* Operações vetorizadas;
* Criando arrays com `array`, `arange`, `zeros`, `ones` e `linspace`;
* Atributos principais: `ndim`, `shape`, `size` e `dtype`;
* Indexação e fatiamento em arrays 1D e 2D;
* Agregações com `sum`, `mean`, `min`, `max` e `std`;
* Boas práticas no uso de NumPy.

> A continuação deste conteúdo (`axis`, máscaras booleanas, broadcasting e leitura de arquivos) está na [Aula 11](/aula11/README.md).

---

## 🎲 NumPy

**NumPy** significa **Numerical Python**.

Ele é uma biblioteca do Python criada para trabalhar com dados numéricos de forma eficiente, especialmente quando precisamos lidar com muitos valores ao mesmo tempo.

O NumPy permite criar e manipular estruturas parecidas com listas, mas muito mais adequadas para cálculos matemáticos, estatísticos e científicos.

Na prática, NumPy costuma aparecer principalmente nas etapas de transformação e exploração dos dados. Depois que os dados são extraídos de uma fonte, podemos usar arrays para calcular médias, somas, filtros, distribuições e outros resumos numéricos.

A estrutura principal do NumPy se chama **array**, ou mais especificamente `ndarray`, que significa **N-dimensional array**.

Um array pode ter:

* Uma dimensão: parecido com uma lista simples;
* Duas dimensões: parecido com uma tabela ou matriz;
* Três ou mais dimensões: usado em imagens, vídeos, tensores e dados mais complexos.

Exemplo:

```txt
Array 1D:
[10, 20, 30, 40]

Array 2D:
[
    [10, 20, 30],
    [40, 50, 60]
]

Array 3D:
[
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
]
```

### Por que usamos o NumPy?

O NumPy é um projeto [open source](https://github.com/numpy/numpy) e é uma das bases do ecossistema de dados em Python. Muitas bibliotecas importantes usam NumPy direta ou indiretamente, como:

* Pandas;
* Matplotlib;
* Scikit-learn;
* SciPy;
* OpenCV;
* TensorFlow;
* PyTorch.

Ou seja: aprender NumPy ajuda a entender melhor várias ferramentas modernas de dados, visualização, inteligência artificial e computação científica.

## O limite das listas

Até agora, usamos listas para armazenar coleções de valores:

```python
notas = [7.5, 8.0, 6.5, 9.0]
```

Listas são muito úteis, flexíveis e fáceis de usar. Elas podem guardar diferentes tipos de dados:

```python
mistura = ['Ana', 28, True, 9.5]
```

Essa flexibilidade é ótima para muitos problemas, mas pode ser ruim quando queremos fazer cálculos numéricos em grande escala.

Imagine que temos uma lista de notas e queremos adicionar 1 ponto em cada nota:

```python
notas = [7.5, 8.0, 6.5, 9.0]
notas_corrigidas = []

for nota in notas:
    notas_corrigidas.append(nota + 1)

print(notas_corrigidas)
```

Saída:

```python
[8.5, 9.0, 7.5, 10.0]
```

Funciona. Mas perceba que precisamos escrever um `for` para aplicar a operação em cada item.

Com NumPy, essa ideia fica mais direta.

---

## Instalando e importando NumPy

Em muitos ambientes de análise de dados, como Google Colab, Anaconda e alguns notebooks online, o NumPy já vem instalado.

Caso seja necessário instalar, usamos o terminal:

```bash
python -m pip install numpy
```

> ℹ️ Ou, usando um **ambiente virtual**, como explicado [aqui](/venv_pip.md).

Depois, importamos no nosso código Python:

```python
import numpy as np
```

Esse apelido `np` é uma convenção muito comum na comunidade Python. Ele deixa o código mais curto e ainda é fácil de reconhecer.

Exemplo:

```python
import numpy as np

notas = np.array([7.5, 8.0, 6.5, 9.0])
print(notas)
```

Saída:

```python
[7.5 8.  6.5 9. ]
```

> 💡 Observe que a saída não aparece exatamente igual a uma lista Python. Arrays NumPy têm sua própria representação.

---

## Primeira diferença importante: lista x array

Vamos comparar uma lista Python com um array NumPy.

```python
lista = [10, 20, 30]
array = np.array([10, 20, 30])
```

Agora vamos tentar somar 5.

```python
print(lista + [5])
# saída: [10, 20, 30, 5]
```

Em listas, o operador `+` concatena listas.

Agora com NumPy:

```python
print(array + 5)
# saída: [15 25 35]
```

No NumPy, a operação foi aplicada em cada elemento do array.

Essa é uma diferença fundamental: **arrays NumPy foram pensados para operações matemáticas com muitos valores ao mesmo tempo**.

---

## Vetorização

**Vetorização** é a capacidade de aplicar uma operação a vários valores de uma vez, sem escrever manualmente um `for`.

Com lista:

```python
precos = [100, 200, 300]
precos_com_desconto = []

for preco in precos:
    precos_com_desconto.append(preco * 0.9)

print(precos_com_desconto)
```

Com NumPy:

```python
import numpy as np

precos = np.array([100, 200, 300])
precos_com_desconto = precos * 0.9

print(precos_com_desconto)
```

Saída:

```python
[ 90. 180. 270.]
```

O NumPy não elimina a repetição internamente. O que ele faz é executar essa repetição de maneira muito mais otimizada, usando implementações eficientes por baixo da linguagem Python.

Para quem está aprendendo, a ideia principal é:

> Em vez de pensar “vou percorrer cada elemento”, começamos a pensar “vou aplicar uma operação ao conjunto inteiro”.

---

## Criando arrays

### Criando um array a partir de uma lista

```python
import numpy as np

idades = np.array([18, 21, 25, 30])
print(idades)
```

### Criando um array com números sequenciais

```python
numeros = np.arange(0, 10)
print(numeros)
#[0 1 2 3 4 5 6 7 8 9]
```

Também podemos definir um intervalo com passo:

```python
pares = np.arange(0, 11, 2)
print(pares)
#[ 0  2  4  6  8 10]
```

### Criando arrays preenchidos com zero ou um

```python
zeros = np.zeros(5)
print(zeros)
#[0. 0. 0. 0. 0.]

uns = np.ones(4)
print(uns)
#[1. 1. 1. 1.]
```

### Criando uma matriz de zeros

```python
matriz = np.zeros((3, 4))
print(matriz)
#[[0. 0. 0. 0.]
# [0. 0. 0. 0.]
# [0. 0. 0. 0.]]
```

Aqui criamos uma matriz com 3 linhas e 4 colunas.

### Criando valores igualmente espaçados

```python
valores = np.linspace(0, 1, 5)
print(valores)
#[0.   0.25 0.5  0.75 1.  ]
```

`linspace` é útil quando queremos dividir um intervalo em uma quantidade específica de partes.

---

## Principais atributos de um array

Um array NumPy carrega informações importantes sobre sua estrutura.

```python
notas = np.array([
    [8.0, 7.5, 9.0],
    [6.5, 8.0, 7.0]
])
```

### `ndim` - número de dimensões

```python
print(notas.ndim)
#2
```

Esse array tem duas dimensões: linhas e colunas.

### `shape` - formato do array

```python
print(notas.shape)
#(2, 3)
```

Isso significa que o array tem 2 linhas e 3 colunas.

### `size` - quantidade total de elementos

```python
print(notas.size)
#6
```

### `dtype` - tipo dos dados

```python
print(notas.dtype)
#float64
```

O `dtype` indica o tipo de dado armazenado no array.

Diferente de uma lista, um array NumPy normalmente trabalha melhor quando todos os valores são do mesmo tipo.

---

## Indexação e fatiamento

Arrays NumPy podem ser acessados de forma parecida com listas.

### Array 1D

```python
notas = np.array([7.5, 8.0, 6.5, 9.0])

print(notas[0])
print(notas[1])
print(notas[-1])
```

### Fatiamento em array 1D

```python
print(notas[1:3])
#[8.  6.5]
```

### Array 2D

```python
notas = np.array([
    [8.0, 7.5, 9.0],
    [6.5, 8.0, 7.0],
    [9.5, 8.5, 10.0]
])
```

Podemos acessar uma posição informando linha e coluna:

```python
print(notas[0, 0])
print(notas[2, 1])
#8.0
#8.5
```

### Pegando uma linha inteira

```python
print(notas[0])
#[8.  7.5 9. ]
```

### Pegando uma coluna inteira

```python
print(notas[:, 1])
#[7.5 8.  8.5]
```

O `:` significa “todas as linhas”.

Então:

```python
notas[:, 1]
```

Significa:

> Pegue todas as linhas da coluna 1.

---

## Operações matemáticas com arrays

```python
notas = np.array([7.0, 8.0, 6.0, 9.0])
```

### Soma

```python
print(notas + 1)
#[ 8.  9.  7. 10.]
```

### Subtração

```python
print(notas - 0.5)
```

### Multiplicação

```python
print(notas * 2)
```

### Divisão

```python
print(notas / 2)
```

### Operações entre arrays

```python
notas_unidade_1 = np.array([7.0, 8.0, 6.0])
notas_unidade_2 = np.array([8.0, 7.5, 9.0])

media = (notas_unidade_1 + notas_unidade_2) / 2
print(media)
#[7.5  7.75 7.5 ]
```

Nesse caso, o NumPy soma posição com posição:

```txt
[7.0, 8.0, 6.0]
+
[8.0, 7.5, 9.0]
=
[15.0, 15.5, 15.0]
```

Depois divide tudo por 2.

---

## Funções de agregação

Funções de agregação resumem muitos valores em um resultado.

```python
notas = np.array([7.5, 8.0, 6.5, 9.0, 10.0])
```

### Soma

```python
print(notas.sum())
```

### Média

```python
print(notas.mean())
```

### Menor valor

```python
print(notas.min())
```

### Maior valor

```python
print(notas.max())
```

### Desvio padrão

```python
print(notas.std())
```

O desvio padrão indica o quanto os valores estão espalhados em relação à média.

* Desvio padrão baixo: valores mais próximos da média;
* Desvio padrão alto: valores mais espalhados.

Exemplo:

```python
turma_a = np.array([7.0, 7.1, 7.2, 7.0, 7.1])
turma_b = np.array([3.0, 5.0, 7.0, 9.5, 10.0])

print(turma_a.mean(), turma_a.std())
print(turma_b.mean(), turma_b.std())
```

Mesmo que duas turmas tenham médias parecidas, elas podem ter distribuições bem diferentes.

---

## Boas práticas com NumPy

1. **Use `import numpy as np`**

   Essa é a convenção mais comum.

2. **Prefira operações vetorizadas quando fizer sentido**

   Em vez de criar muitos `for`, procure pensar em operações sobre o array inteiro.

3. **Observe o formato dos dados com `shape`**

   Muitos erros acontecem porque o array não está no formato esperado.

4. **Verifique o tipo dos dados com `dtype`**

   Dados importados de arquivos podem vir como texto, inteiro ou decimal.

5. **Use nomes claros**

   Prefira `notas`, `medias`, `precos`, `vendas` em vez de `x`, `a`, `b`, quando estiver aprendendo.

6. **Não use NumPy para tudo**

   Se você só tem poucos valores simples ou dados muito heterogêneos, listas e dicionários podem ser suficientes.

> ➡️ Na [Aula 11](/aula11/README.md) vamos usar esses fundamentos para analisar tabelas de dados: agregações por linha e coluna (`axis`), filtros com máscaras booleanas, broadcasting e leitura de arquivos.

---

## Resumo dos principais recursos

| Recurso          | Para que serve                     | Exemplo                |
| ---------------- | ---------------------------------- | ---------------------- |
| `np.array()`     | Criar array a partir de lista      | `np.array([1, 2, 3])`  |
| `np.arange()`    | Criar sequência numérica           | `np.arange(0, 10, 2)`  |
| `np.linspace()`  | Criar valores igualmente espaçados | `np.linspace(0, 1, 5)` |
| `np.zeros()`     | Criar array preenchido com zero    | `np.zeros((3, 4))`     |
| `np.ones()`      | Criar array preenchido com um      | `np.ones(5)`           |
| `.ndim`          | Ver número de dimensões            | `array.ndim`           |
| `.shape`         | Ver formato do array               | `array.shape`          |
| `.size`          | Ver total de elementos             | `array.size`           |
| `.dtype`         | Ver tipo dos dados                 | `array.dtype`          |
| `[i]`, `[i:j]`   | Acessar e fatiar elementos         | `notas[1:3]`           |
| `[l, c]`, `[:, c]` | Acessar posição ou coluna em 2D  | `notas[:, 1]`          |
| `+ - * /`        | Operar elemento a elemento         | `precos * 0.9`         |
| `.sum()`         | Somar valores                      | `notas.sum()`          |
| `.mean()`        | Calcular média                     | `notas.mean()`         |
| `.min()`         | Menor valor                        | `notas.min()`          |
| `.max()`         | Maior valor                        | `notas.max()`          |
| `.std()`         | Desvio padrão                      | `notas.std()`          |

---

## 🧱 Exercícios fundamentais

### [Exercício 01] Criando arrays

Crie um array NumPy com os seguintes valores:

```python
[10, 20, 30, 40, 50]
```

Depois exiba:

* O array completo;
* O primeiro valor;
* O último valor;
* A quantidade total de elementos;
* O tipo dos dados.

---

### [Exercício 02] Corrigindo notas

Dado o array:

```python
notas = np.array([6.0, 7.5, 8.0, 5.5, 9.0])
```

Crie um novo array adicionando `0.5` ponto a cada nota.

Depois exiba:

* As notas originais;
* As notas corrigidas;
* A média antes da correção;
* A média depois da correção.

---

### [Exercício 03] Preços com desconto

Dado o array:

```python
precos = np.array([100, 250, 80, 300, 150])
```

Calcule um novo array com 10% de desconto.

Depois exiba:

* Os preços originais;
* Os preços com desconto;
* O maior preço original;
* O menor preço com desconto.

---

### [Exercício 04] Lista x array

Considere:

```python
lista = [1, 2, 3]
array = np.array([1, 2, 3])
```

**Antes de executar**, escreva no seu código (como comentário) o que você acha que cada linha abaixo vai exibir:

```python
print(lista * 2)
print(array * 2)
print(lista + lista)
print(array + array)
```

Depois execute e compare com a sua previsão.

Por fim, escreva um código que produza, usando **apenas listas** (com `for`), o mesmo resultado de `array * 2`.

---

### [Exercício 05] Explorando a estrutura

Crie os seguintes arrays:

* Uma sequência de 1 a 20 (incluindo o 20) com `np.arange`;
* Os múltiplos de 5 entre 0 e 50 com `np.arange`;
* Uma matriz de zeros com 4 linhas e 3 colunas;
* 6 valores igualmente espaçados entre 0 e 100 com `np.linspace`.

Para cada um, exiba o próprio array e seus atributos `ndim`, `shape`, `size` e `dtype`.

Depois pense:

* Por que `np.zeros` e `np.linspace` geram `float64`, enquanto `np.arange(1, 21)` gera inteiros?

---

### [Exercício 06] Fatiando temperaturas

Dado o array com as temperaturas máximas de uma semana (segunda a domingo):

```python
temperaturas = np.array([29.5, 30.2, 31.0, 28.7, 27.9, 32.4, 33.1])
```

Usando indexação e fatiamento, exiba:

* A temperatura de quarta-feira;
* As temperaturas dos três primeiros dias;
* As temperaturas do fim de semana (os dois últimos dias);
* As temperaturas dos dias úteis;
* As temperaturas de dias alternados, começando na segunda (`[::2]`).

Agora considere a matriz abaixo, em que cada linha é uma cidade e cada coluna é um turno (manhã, tarde, noite):

```python
turnos = np.array([
    [26.0, 31.5, 27.0],
    [24.5, 29.0, 25.5],
    [28.0, 34.0, 29.5]
])
```

Exiba:

* Todas as temperaturas da segunda cidade;
* Todas as temperaturas da tarde;
* A temperatura da noite na terceira cidade.

---

### [Exercício 07] Comparando turmas

Duas turmas fizeram a mesma prova:

```python
turma_a = np.array([6.5, 7.0, 7.5, 7.0, 6.8, 7.2])
turma_b = np.array([3.0, 10.0, 9.5, 4.0, 8.0, 7.5])
```

Para cada turma, calcule e exiba:

* A média;
* A maior e a menor nota;
* A amplitude (maior nota − menor nota);
* O desvio padrão.

Depois responda (em um comentário no código):

* As médias são parecidas? E os desvios padrão?
* Qual turma é mais "homogênea"? Como os números mostram isso?

---

## 🚀 Mini Projeto 7: Termômetro Semanal

### Contexto

Uma estação meteorológica registrou a temperatura máxima, em graus Celsius, de cada dia desta semana e da semana passada. Os dados vão ser enviados para um parceiro internacional, que precisa deles em Fahrenheit.

### Dados iniciais

Use os dados abaixo diretamente no código:

```python
import numpy as np

dias = np.array(['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo'])

semana_atual = np.array([28.5, 30.1, 31.4, 29.8, 27.6, 26.9, 30.0])
semana_passada = np.array([27.0, 28.5, 29.0, 30.2, 28.1, 27.5, 29.4])
```

### O desafio

Crie um programa que calcule e exiba:

1. As temperaturas da semana atual convertidas para Fahrenheit (`F = C * 9 / 5 + 32`);
2. A média, a máxima, a mínima e a amplitude térmica da semana atual (em Celsius);
3. O desvio padrão das duas semanas: qual foi mais estável?
4. A variação de cada dia em relação ao mesmo dia da semana passada (`semana_atual - semana_passada`);
5. A variação média entre as duas semanas: a semana atual foi mais quente ou mais fria?
6. A média dos dias úteis e a média do fim de semana da semana atual (use fatiamento);
7. Quanto cada dia da semana atual ficou acima ou abaixo da média da semana.

### Regras

* Use NumPy;
* Use operações vetorizadas para as conversões e comparações (sem `for` para calcular);
* Use fatiamento para separar dias úteis e fim de semana;
* O `for` pode ser usado **apenas** para exibir os resultados;
* Mostre os valores com duas casas decimais.

### Exemplo de saída esperada (parcial)

```txt
Temperaturas em Fahrenheit:
Segunda: 83.30 °F
Terça: 86.18 °F
Quarta: 88.52 °F
Quinta: 85.64 °F
Sexta: 81.68 °F
Sábado: 80.42 °F
Domingo: 86.00 °F

Média: 29.19 °C
Máxima: 31.40 °C
Mínima: 26.90 °C
Amplitude: 4.50 °C

Variação média em relação à semana passada: +0.66 °C
A semana atual foi mais quente.
```

### ✨ Extra

Use o módulo `random` (visto na [Aula 09](/aula09/README.md)) para gerar as temperaturas de 30 dias, entre 22 °C e 35 °C, e transforme-as em um array NumPy. Depois responda:

* Qual a média do mês?
* Qual a temperatura dos 7 primeiros e dos 7 últimos dias?
* A média da última semana foi maior que a da primeira?
