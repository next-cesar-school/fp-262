# NExT 26.1 | Fundamento de Python Aplicado a Dados

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

## 🐝 Exercícios Beecrowd

-- 💡 Refaça todos os exercícios da aula passada usando `for` --

[1067 - Números Ímpares](https://judge.beecrowd.com/pt/problems/view/1067)

[1075 - Resto 2](https://judge.beecrowd.com/pt/problems/view/1075)

[1172 - Substituição em Vetor I](https://judge.beecrowd.com/pt/problems/view/1172)

[1095 - Sequencia IJ 1](https://judge.beecrowd.com/pt/problems/view/1095)

[1116 - Dividindo X por Y](https://judge.beecrowd.com/pt/problems/view/1116)

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
