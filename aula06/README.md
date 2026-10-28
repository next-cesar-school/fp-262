# NExT 26.2 | Fundamentos de Python Aplicado a Dados

![CESAR School](/cesar_school.png)

## Aula 06 - Arquivos

### Na aula de hoje

- Manipulação de Arquivos

---

## 📄 Arquivos

Uma das formas mais populares e eficientes de manter informações salvas é armazenando os dados em **arquivos**.

Arquivos também são fontes de entradas de dados para os sistemas, onde esses dados podem ter sido coletados e processados inicialmente por um programa, e lidos e manipulados por outro.

Em Python temos uma série de recursos nativos para escrita e leitura de arquivos.

De forma geral, podemos dizer que existem dois tipos de arquivo:

- Arquivos de texto (`.txt`, `.py`, `.html`, `.md`)
- Arquivos binários (`.docx`, `.pdf`, `.jpeg`, `.mp3`)

> 💡 Habilite no seu sistema a exibição das **extensões de nomes de arquivos**. Isso ajuda a visualizar qual o formato do arquivo.

### 📚 Modos de abertura de arquivo

Por padrão, os arquivos são abertos no modo de leitura, mas existem vários outros modos possíveis:

| Modo | Sintaxe | Cursor | Descrição |
| ---- | ------- | ------ | --------- |
| **Read** | **`'r'`** | Início | **Padrão**. Abre o arquivo apenas para leitura. Se o arquivo não existir, lança um erro `FileNotFoundError` |
| Read and Write | `'r+'` | Início | Abre o arquivo para leitura e escrita. Se o arquivo não existir, lança um erro `FileNotFoundError` |
| Write | `'w'` | Início | Abre o arquivo para escrita, sobrescrevendo o conteúdo original. Se o arquivo não existir, será criado |
| Append | `'a'` | Final | Abre o arquivo para escrita. Se o arquivo não existir, será criado. |

### 🗒️ Leitura

O primeiro passo para ler um arquivo é abri-lo. Para isso, usamos a função `open()`:

```python
arquivo = open('nomedoarquivo.txt')
```

Se for necessário mudar o modo de abertura, esse parâmetro é passado depois do nome do arquivo:

```python
arquivo = open('nomedoarquivo.txt', 'a')
```

A função `open()` retorna uma referência a um arquivo que pode ser manipulado com funções próprias.

> 💡 Documentação da função `open` [aqui](https://docs.python.org/3/library/functions.html#open)

#### 🪧 Métodos de leitura

Os dados extraídos do arquivo geralmente são representados como strings.

- #### `arq.read()`

Retorna um `str` com todo o conteúdo do arquivo.

```python
conteudo = arq.read()
```

- #### `arq.readline()`

Retorna um `str` com o conteúdo de uma linha do arquivo. Para cada vez que esse comando é executado, uma nova linha é retornada.

```python
conteudo = arq.readline()
```

- #### `arq.readlines()`

Retorna um `list` onde cada elemento da lista é uma linha do arquivo em `str`.

```python
conteudo = arq.readlines()
```

- #### `arq.seek()`

Move o cursor para a posição de um caracter específico.

```python
arquivo.seek(0)
```

Esses métodos podem ser usados em conjunto com o `for`:

```python
arquivo = open('nomedoarquivo.txt', 'r')
for linha in arquivo:
  print(linha)
```

### 📝 Escrita

Para escrever em um arquivo, é necessário usar um modo que habilite isso, como `w`, `r+` ou `a`:

```python
arquivo = open('nomearquivo.txt', 'w')
arquivo.write('cachorro,terrestre\n')
arquivo.write('leão,terrestre\n')
arquivo.write('pato,aéreo\n')
```

Sempre que um arquivo é lido, é boa prática fechá-lo. Caso o conteúdo dele tenha sido manipulado, as modificações só serão gravadas em permanentemente quando o método `.close()` for alcançado.

```python
arquivo.close()
```

#### 🪧 Métodos de escrita

Para escrever em um arquivo, podemos usar dois métodos:

- #### `arq.write(conteúdo)`

  Escreve o conteúdo em `str` passado como argumento para o arquivo.
  
  ```python
  arquivo = open('nomearquivo.txt', 'a')
  arquivo.write('chimpanzé,terrestre\n')
  arquivo.write('elefante,terrestre\n')
  arquivo.close()
  ```

- #### `arq.writelines(lista)`

  Escreve um `list` de `str` passado como argumento para o arquivo.
  
  ```python
  arquivo = open('nomearquivo.txt', 'a')
  lista = ['ovos\n', 'bacon\n', 'Spam\n']
  arquivo.writelines(lista)
  arquivo.close()
  ```

### 📋 Comando `with`

O comando `with` é usado para facilitar a manipulação de qualquer estrutura que precise ser finalizada. Geralmente é usado associado a leitura e escrita de arquivos.

Principais vantagens:

- Sintaxe mais limpa para a leitura de arquivos;
- Abre e fecha o arquivo automaticamente;
- Permite trabalhar com vários arquivos simultaneamente.

```python
with open('arquivo.txt') as arquivo:
  print(arquivo.readline())
  print(arquivo.readline())
```

## 🧱 Exercícios Fundamentais

### [Exercício 01]

Crie um arquivo que contenha, em cada linha, o nome de um animal e seu habitat, separado por vírgula, como no exemplo:

  ```txt
  baleia,aquático
  tucano,aéreo
  tubarão,aquático
  coelho,terrestre
  leão,terrestre
  golfinho,aquático
  camaleão,arbóreo
  cobra,terrestre
  urso-polar,gelado
  coruja,aéreo
  canguru,terrestre
  tartaruga,aquático
  ```

  Em seguida, faça um programa que leia o arquivo e exiba apenas o nome dos animais terrestres.

  > 🎖️ *Bônus: peça ao usuário que informe o habitat.*

### [Exercício 02]

Implemente um programa que leia o arquivo da questão anterior e gere um novo arquivo apenas com os animais terrestres.

### [Exercício 03]

Crie um programa que registra as 4 notas de uma pessoa na escola (como o boletim) em um arquivo. Em seguida, leia todos os valores para imprimir o **menor** valor, o **maior** e a **média**.

> 💡 Dica: Se você usar listas, pode usar as funções `min()` e `max()`.

ℹ️ Esses projetos a seguir são baseados em entrevistas de avaliação técnica de emprego. Ao escrever o código, recomendamos que foquem na legibilidade, uso de boas práticas de programação e recursos adequados à situação. Criem repositórios individuais para cada projeto.

## 🚀 Mini Projeto 1: 💸 PyFinanceiro

- Neste desafio, você tem a tarefa de criar um script Python para analisar os registros financeiros de sua empresa. Você fornecerá um conjunto de dados financeiros chamado [dados_financeiros.csv](https://drive.google.com/file/d/1g4A0DkMdGxwv9JSGO32DYqvPby45pIHG/view?usp=sharing). O conjunto de dados é composto por duas colunas: `Data` e `Lucros/Perdas`, separados por virgula. Felizmente, sua empresa tem padrões bastante flexíveis para a contabilidade, então os registros são simples.
- Sua tarefa é criar um script Python que analise os registros para calcular cada um das seguintes informações:
  - O número total de meses incluídos no conjunto de dados
  - O valor total líquido de "Lucros / Perdas" durante todo o período
  - A média dos "Lucros / Perdas" durante todo o período
  - A média das mudanças em "Lucros / Perdas" durante todo o período
  - O maior aumento nos lucros (data e valor) durante todo o período
  - A maior redução nos lucros (data e valor) ao longo de todo o período
- Por exemplo, sua análise deve ser semelhante a esta abaixo:

  ```txt
  Analise Financeira
  ----------------------------
  Total de meses: 86
  Total: $ 38382578
  Média: $ 446309.05
  Variação da média: $ -2315.12
  Maior aumento nos lucros: Feb-2012 ($ 1926159)
  Maior redução nos lucros: Sep-2013 ($ -2196167)
  ```

- Além disso, seu script final deve imprimir a análise no terminal e exportar um arquivo de texto `relatorio.txt` com os resultados.

## 🚀 Mini Projeto 2: 🗳️ PyVotação

- Neste desafio, você tem a tarefa de ajudar uma pequena cidade rural a modernizar seu processo de contagem de votos. (Até agora, o tio Cleiton vinha contando-os um por um com confiança, mas, infelizmente, sua concentração não é o que costumava ser.)
- Você receberá um conjunto de dados de enquete chamado [dados_eleicao.csv](https://drive.google.com/file/d/13tarkZMlfvMcHnS8K49pdF-GMYOwgggg/view?usp=sharing). O conjunto de dados é composto por três colunas: `ID do eleitor`, `Município` e `Candidato`. Sua tarefa é criar um script Python que analise os votos e calcule cada uma das seguintes informações:
  - O número total de votos expressos
  - Uma lista completa de candidatos que receberam votos
  - A porcentagem de votos que cada candidato ganhou
  - O número total de votos que cada candidato ganhou
  - O vencedor da eleição com base no voto popular.
- Por exemplo, sua análise deve ser semelhante a esta abaixo:

  ```txt
  Resultados Eleitorais
  -------------------------
  Total de votos: 3521001
  -------------------------
  Khan: 63.0% (2218231)
  Correy: 20.0% (704200)
  Li: 14.0% (492940)
  O'Tooley: 3.0% (105630)
  -------------------------
  Vencedor: Khan
  -------------------------
  ```

- Além disso, seu script final deve imprimir a análise no terminal e exportar um arquivo de texto `resultado.txt` com os resultados.

### 🏃💨 Conteúdo de Apoio

Para tratar alguns dados, pode ser interessantes adotar o uso de dicionários (conteúdo que será abordado nas próximas aulas). Se você puder, sugerimos a leitura dos seguintes artigos:

- [Sort a dictionary by value](https://careerkarma.com/blog/python-sort-a-dictionary-by-value/)
- [Python Sort](https://careerkarma.com/blog/python-sort/)

Obs.: A função `sorted()`, por padrão, organiza uma lista por ordem alfabética, mas isso pode ser personalizado usando o parâmetro `key`. No caso, você pode usar também funções `lambda`.

Para o caso do sorted, especificamente, seria possível fazer da seguinte forma:

```python
# usando funções tradicionais
def ordena_dict(dicionario):
  return dicionario[1]

cand_voto = sorted(cand_voto.items(), key=ordena_dict, reverse=True)

# usando lambda
cand_voto = sorted(cand_voto.items(), key=lambda d: d[1], reverse=True)
```

Para entender mais sobre `funções lambda`, recomendo a leitura desses materiais:

- [Funções Lambda em Python](https://www.hashtagtreinamentos.com/funcoes-lambda-python)
- [Lambda Function](https://www.guru99.com/python-lambda-function.html)

## 🏋️‍♂️ Mais desafios de programação

Quer fazer mais desafios de programação? [Neste repositório](https://github.com/CollabCodeTech/backend-challenges) existe um compilado de desafios de backend de várias empresas ao redor do mundo.
