# NExT 26.2 | Fundamento de Python Aplicado a Dados

![CESAR School](/cesar_school.png)

## Aula 04 - Estruturas de Repetição (parte 02)

### Na aula de hoje

- Estruturas de Repetição
  - for
  - controle de fluxo

---

## 🔃 `For`

O comando `for` em Python é usado para iterar (percorrer) elementos de uma sequência, como listas, strings, tuplas, dicionários ou qualquer objeto iterável. É muito útil para automatizar tarefas repetitivas, permitindo que você execute um bloco de código para cada elemento de uma sequência.

```python
for item in iteravel:
  # código que vai repetir
```

- `item`: é o nome que você dará ao item atual da sequência a cada iteração;
- `iteravel`: é o objeto que será percorrido.

```python
# percorrer uma lista

frutas = ['maçã', 'banana', 'laranja', 'uva', 'ração', 'desodorante']

# com while
i = 0
while i < len(frutas):
    print(frutas[i])
    i += 1

# com for
for fruta in frutas:
    print(f'Item da lista: {fruta}')
```

### Exemplos

```python
# Percorrer uma lista + Condicional
# exibir apenas as idades maiores que 35
idades = [19, 45, 30, 35, 33, 13, 67, 22]

```

```python
# Iteração sobre uma string
nome_completo = input('Insira o seu nome completo: ')

# cada letra será um elemento

# Cada palavra como elemento

```

```python
# Uso do range
# repetir num número x de vezes

# receber 4 notas de um estudante e adicionar a uma lista

# exibir todos os números pares contidos de 1 a 100

```

```python
# Iterando sobre matriz
# listas dentro de listas

matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

```

```python
# Filtrando de elementos de uma lista
# criar uma nova lista apenas com os itens com 5 caracteres ou menos

nomes_original = ['Miguel', 'Arthur', 'Heitor', 'Helena', 'Alice', 'Laura', 'Gabriel', 'Davi', 'Maria Clara', 'Pedro', 'Yoda', 'Caio']
nomes_selecionados = []

```

> ⚠️ **Evite modificar listas durante a iteração**:\
> Ao alterar uma lista dentro de um loop `for`, use cópias para evitar comportamentos inesperados.

## Resumo

### Estruturas de Repetição

| **Característica** | **`while`** | **`for`** |
| ------------------ | ----------- | --------- |
| **Uso principal** | Usado quando não se sabe quantas iterações serão necessárias | Usado quando se sabe o número de iterações ou ao iterar sobre uma sequência |
| **Condição de parada** | Continua enquanto a condição especificada for verdadeira | Itera sobre uma sequência (como lista, tupla, string) ou usa `range` |
| **Controla a iteração?** | Sim, diretamente com uma condição booleana | Não diretamente, o número de iterações é controlado pela sequência |
| **Ideal para** | Loops indeterminados (quando o número de repetições depende de uma condição) | Loops determinados (quando se sabe o número exato de iterações) |
| **Flexibilidade** | Mais flexível, pode ser usado para uma variedade de situações baseadas em condições | Menos flexível, pois depende de um iterável ou de uma sequência |
| **Eficiência** | Pode ser menos eficiente se a condição não for controlada corretamente | Geralmente mais eficiente e fácil de usar em iterações simples |

# 🐝 Exercícios Beecrowd

-- 💡 Refaça todos os exercícios da aula passada usando `for` --

## [1067 - Números Ímpares](https://judge.beecrowd.com/pt/problems/view/1067)

Leia um inteiro X (1 ≤ X ≤ 1000) e mostre os números ímpares de 1 até X, um por linha. Se X for ímpar, ele também aparece.

### Entrada

Um valor inteiro qualquer.

### Saída

Todos os ímpares de 1 até X, incluindo X se for o caso.

### Exemplos

| Entrada | Saída |
|---|---|
| `8` | `1`<br>`3`<br>`5`<br>`7` |

## [1075 - Resto 2](https://judge.beecrowd.com/pt/problems/view/1075)

Leia um inteiro N e mostre todos os números de 1 a 10000 cujo resto da divisão por N é 2.

### Entrada

Um valor inteiro N (N < 10000).

### Saída

Os valores cujo resto da divisão por N é 2, um por linha.

### Exemplos

| Entrada | Saída |
|---|---|
| `13` | `2`<br>`15`<br>`28`<br>`41`<br>`...` |

## [1172 - Substituição em Vetor I](https://judge.beecrowd.com/pt/problems/view/1172)

Leia um vetor `X[10]`. Troque por 1 todos os valores iguais a zero ou negativos e depois mostre o vetor.

### Entrada

10 valores inteiros, positivos ou negativos.

### Saída

Para cada posição do vetor, mostre `X[i] = x`, em que `i` é a posição e `x` é o valor guardado nela.

### Exemplos

| Entrada | Saída |
|---|---|
| `0`<br>`-5`<br>`63`<br>`0`<br>`...` | `X[0] = 1`<br>`X[1] = 1`<br>`X[2] = 63`<br>`X[3] = 1`<br>`...` |

## [1095 - Sequencia IJ 1](https://judge.beecrowd.com/pt/problems/view/1095)

Mostre a sequência do exemplo abaixo: `I` começa em 1 e aumenta de 3 em 3, `J` começa em 60 e diminui de 5 em 5, até `J` chegar a 0.

### Entrada

Não há entrada.

### Saída

A sequência no formato do exemplo.

### Exemplos

| Entrada | Saída |
|---|---|
| *(sem entrada)* | `I=1 J=60`<br>`I=4 J=55`<br>`I=7 J=50`<br>`...`<br>`I=? J=0` |

## [1116 - Dividindo X por Y](https://judge.beecrowd.com/pt/problems/view/1116)

Leia pares de números e mostre o resultado da divisão do primeiro pelo segundo. Se a divisão não puder ser feita (divisor igual a zero), mostre `divisao impossivel`.

Observação: em linguagens como C e C++, dividir dois inteiros dá um inteiro. Faça a conversão (*cast*) para obter o resultado com casa decimal.

### Entrada

Um inteiro N, que é a quantidade de pares de inteiros (X e Y) que vêm a seguir.

### Saída

Para cada par, o resultado da divisão com um dígito depois do ponto, ou `divisao impossivel` se o cálculo não for possível.

### Exemplos

| Entrada | Saída |
|---|---|
| `3`<br>`3 -2`<br>`-8 0`<br>`0 8` | `-1.5`<br>`divisao impossivel`<br>`0.0` |

## 🧱 Exercícios Fundamentais

⚠️ Esses são os mesmos exercícios da aula passada, mas agora você deve fazer usando `for`.

### [Exercício 01]

Faça um programa que leia 5 números e informe o maior número.

### [Exercício 02]

Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

### [Exercício 03]

Faça um programa que recebe um número de 1 a 10 do usuário e imprime a tabuada de multiplicação desse número

### [Exercício 04]

Faça um programa que recebe do usuário 10 valores de números inteiros, armazena em um vetor e apos percorre-lo exibe qual é o maior valor e a sua posição.

## 🤿 Exercícios de Aprofundamento

⚠️ Alguns desses exercícios exigem conhecimentos ainda não apresentados no curso!

### [Exercício 05]

Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

### [Exercício 06]

Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

### [Exercício 07]

Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.
