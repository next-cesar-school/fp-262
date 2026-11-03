# NExT 26.2 | Fundamentos de Python Aplicado a Dados

![CESAR School](/cesar_school.png)

## Aula 07 - Tratamento de Exceções

### Na aula de hoje

- ETL
- Exceções
- `try`, `except`, `else`, `finally`
- Boas práticas no tratamento de exceções

---

## Pipeline ETL

No trabalho com dados, é comum implementarmos processos chamados de ETL (Extract, Transform, Load):

- **Extract (Extrair)**: Extrair dados do usuário, sistemas, APIs ou arquivos;
- **Transform (Transformar)**: Aplicação de regras de negócio e limpeza dos dados, convertendo os valores e tratando eventuais erros que atrapalhariam a análise;
- **Load (Carregar)**: Carregar (salvar) os dados transformados em um novo destino, como um arquivo ou banco de dados.

### Pipeline EDA (Exploratory Data Analysis)

Após o ETL, pode vir a etapa de EDA (Exploratory Data Analysis), usada para explorar os dados por meio de estatísticas descritivas, tendências, distribuições, padrões, valores ausentes, outliers e visualizações.

## Tratamento de Exceções

O tratamento de exceções é uma técnica fundamental para tornar os programas mais **robustos** e capazes de lidar com erros de maneira controlada. Em Python, as exceções são eventos que **interrompem o fluxo normal do programa**, mas que podem ser tratadas para evitar falhas inesperadas.

As exceções em Python **ocorrem durante a execução do programa** e podem interromper o fluxo normal do código. Alguns exemplos de situações comuns que geram exceções:

- Divisão por zero: `ZeroDivisionError`
- Índice fora do intervalo: `IndexError`
- Tipo inválido: `TypeError`
- Arquivo inexistente: `FileNotFoundError`

Exemplo:

```python
numeros = [1, 2, 3]
print(numeros[5])  # Lança IndexError
```

## Lidando com Exceções: `try` e `except`

O bloco `try` permite testar um trecho de código que pode gerar uma exceção. O bloco `except` define o que fazer quando a exceção ocorre.

Exemplo:

```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print('Erro: Divisão por zero não é permitida.')
```

## Capturando múltiplas exceções

É possível tratar várias exceções de diferentes formas:

```python
try:
    numero = int(input('Digite um número: '))
    resultado = 10 / numero
except ValueError:
    print('Erro: Você deve digitar um número.')
except ZeroDivisionError:
    print('Erro: Não é possível dividir por zero.')
```

Ou ainda, capturando várias exceções para um tratamento único:

```python
try:
    numero = int(input('Digite um número: '))
    resultado = 10 / numero
except (ValueError, ZeroDivisionError):
    print('Erro: informe um número válido e diferente de zero.')
```

## Blocos `else` e `finally`

- `else`: Executado se nenhuma exceção ocorrer;
- `finally`: Executado sempre, independentemente de exceções.

```python
arquivo = None

try:
    arquivo = open('dados.txt', 'r', encoding='utf-8')
    conteudo = arquivo.read()
except FileNotFoundError:
    print('Erro: Arquivo não encontrado.')
else:
    print('Arquivo lido com sucesso!')
finally:
    if arquivo is not None:
        arquivo.close()
    print('Encerrando operação.')
```

### As Exceções do Python

> ℹ️ Consulte todas as exceções do Python [aqui](https://docs.python.org/3/library/exceptions.html)

## Boas Práticas no Tratamento de Exceções

1. Trate apenas as exceções esperadas.

    Evite capturar exceções genéricas com `except Exception` quando você não souber exatamente o que fazer com o erro. Quando for necessário capturar uma exceção genérica, registre o erro, informe o problema adequadamente e evite esconder falhas importantes.

    ```python
    ...
    except Exception as e:
        print(f'Erro: {type(e).__name__} - {e}.')
    ```

2. Seja específico.

    Capture exceções específicas para um tratamento mais claro.

3. Use `finally` para liberar recursos.

    Feche arquivos ou conexões no bloco `finally`.

4. Não esconda erros.

    Sempre informe o que aconteceu e como o usuário pode corrigir.

## 🐝 Exercícios Beecrowd

[1068 - Balanço de Parênteses I](https://judge.beecrowd.com/pt/problems/view/1068)

[3038 - Carta de Natal Criptografada](https://judge.beecrowd.com/pt/problems/view/3038)

[1467 - Zerinho ou Um](https://judge.beecrowd.com/pt/problems/view/1467)

[1789 - A Corrida de Lesmas](https://judge.beecrowd.com/pt/problems/view/1789)

## 🧱 Exercícios Fundamentais

### [Exercício 01]

Escreva um programa que leia dois números do usuário e calcule a divisão entre eles. Use exceções para tratar:

- Erros de entrada (`ValueError`);
- Divisão por zero (`ZeroDivisionError`).

### [Exercício 02]

Implemente uma função que solicite ao usuário o nome de um arquivo, tente abri-lo para leitura e exiba seu conteúdo. Trate o erro de arquivo não encontrado (`FileNotFoundError`).

### [Exercício 03]

Crie uma função que receba um dicionário e uma chave, retornando o valor correspondente. Trate o erro de chave inexistente (`KeyError`).

### [Exercício 04]

Você recebeu um conjunto de dados extraído de um sistema legado. No entanto, o banco de dados está "sujo": alguns cadastros possuem textos informativos, valores nulos, campos vazios ou linhas incompletas no lugar dos números.

Dado o arquivo abaixo, escreva um programa que percorra todos os itens, tente converter os valores das colunas `idade` e `valor_compra` para `int` e `float`, respectivamente, e adicione as linhas válidas em um novo arquivo de saída.

Sempre que uma linha com dados inválidos for encontrada, imprima essa linha e informe o tipo de erro identificado.

```c
id_cliente,nome,idade,valor_compra
1,Ana,28,150.50
2,Bruno,N/A,200.00
3,Carlos,45,300.10
4,Daniela,Trinta,350.25
5,Eduardo,22,120.00
6,Fernanda,34,cem reais
7,Gustavo,29,89.90
8,Helena,18,50.00
9,Igor,50
10,Julia,31,450.75
11,Kleber,40,N/A
12,Laura,26,199.99
13,Marcos,NULL,NULL
14,Natalia,33,210.00
15,Oswaldo,,
```
