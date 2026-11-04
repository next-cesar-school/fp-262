# NExT 26.2 | Fundamentos de Python Aplicado a Dados

![CESAR School](/cesar_school.png)

## Aula 08 - Estruturas de Dados

### Na aula de hoje

- Tuple
- Set
- Dict

---

## Estruturas de Dados

Sempre que precisamos armazenar vários dados em uma única variável se faz necessário usar algum tipo de dado _container_. Em Python, os principais são:

- `list`;
- `tuple`;
- `set`;
- `dict`;

Cada container, ou tipos de coleção, tem uma característica específica e um uso diferente. Nesta aula vamos conhecer um pouco mais sobre eles.

### 🪨 `tuple`

Ao usar listas, há bastante liberdade para alterar seus itens. Em determinadas situações, essas listas não deveriam ser alteradas. Para criar coleções de dados que não podem ser alterados, podemos usar `tuple` (tupla), em casos como:

- Dias da semana;
- Coordenadas de um prédio;
- Letras de um alfabeto.

```python
t = ('domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado')
```

> #### Características `tuple`

- Imutáveis;
- Ordenados/indexável;
- Permite elementos duplicados;
- Desempenho superior a listas.

> 💡 Obs.: _O acesso aos elementos de uma tupla é feito da mesma forma que com listas_

```python
# tuple -> Tópicos a explorar:
# - Criação de uma Tupla
# - Acesso aos elementos de uma Tupla
# - len()
# - tupla.index(item)
# - tupla.count(item)
# - Imutabilidade
```

### 💎 `set`

Tanto em **listas**, quanto em **tuplas**, é possível ter elementos repetidos:

```python
t = (0, 1, 1, 2, 3, 5)
l = [0, 1, 1, 2, 3, 5]
```

Quanto houver uma situação onde você não deva armazenar itens repetidos em uma coleção de dados, é possível usar um `set` (conjunto):

```python
s1 = set()
s.add(1)
s.add(2)
s.add(1)

s2 = {'bacon', 'banana', 'spam', 'ovos', 'spam', 'salsicha', 'spam'}
```

> #### Características `set`

- Mutáveis (itens podem ser adicionados e removidos, mas os itens em si devem ser imutáveis. Você não pode ter uma lista dentro de um set, por exemplo, mas pode ter uma tupla);
- Não Ordenados/não indexável;
- **Não Permite elementos repetidos**.

```python
# Tópicos a explorar:
# - criar um set
# - print(ingredientes[0]) # erro
# - adicionar elementos
# - remover elementos
```

### 🔑 `dict`

Para criar estruturas de dados que são mapeados por valores (e não pelo índice, como nas listas) é possível usar um **dicionário**.

> **Chave** x **Valor**

Obs.: _O mapeamento é feito pela chave (e não pela ordem)_

Exemplos de uso prático:

- Dicionários;
- CEP;
- Tabela de valores;

```python
dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
```

> #### Características `dict

- Mutáveis;
- Ordenados/indexável;
- Permite valores duplicados (mas não a chave);
- Acesso aos valores rápido;
- Base para JSON e APIs.

```python
# Tópicos a explorar
# - Criando um dicionário
# - Acessando elementos de um dicionário
# - Adição de itens por atribuição
# - Adição de itens por update
# - Removendo itens
# - esvaziando um dicionário
```

### 🗝️ Alguns métodos úteis de dicionários

- `dict.keys()` - Apresenta todas as chaves do dicionário
- `dict.values()` - Apresenta todos os valores do dicionário
- `dict.items()` - `dict_keys()` + `dict_values()`
- `dict.get(chave, default)` - Retorna um elemento do dicionário. Se não encontrar, retorna o valor _default_.

```python
# Tópicos a explorar
# - adicionar valores + update()
# - get()
# - keys()
# - values()
# - items()
# - for
```

## 📋 Resumão

| Tipo  | Mutável | Ordenado | Indexável | Elementos Repetidos |
|-------| :-----: | :------: | :-------: | :-----------------: |
|`list` |   ✅    |    ✅    |    ✅     |          ✅         |
|`tuple`|   ❌    |    ✅    |    ✅     |          ✅         |
| `set` |   ✅    |    ❌    |    ❌     |          ❌         |
|`dict` |   ✅    |    ✅    |    ✅*    |          ✅         |

## 🐝 Exercícios Beecrowd

[1050 - DDD](https://judge.beecrowd.com/pt/problems/view/1050)

[1168 - LED](https://judge.beecrowd.com/pt/problems/view/1168)

[1049 - Animal](https://judge.beecrowd.com/pt/problems/view/1049)

[1179 - Preenchimento de Vetor IV*](https://judge.beecrowd.com/pt/problems/view/1179)

[2653 - Dijkstra](https://judge.beecrowd.com/pt/problems/view/2653)

\* Questão sobre vetor, mas é uma boa oportunidade de usar função\

## 🧱 Exercícios Fundamentais

### [Exercício 01]

Dada a lista a seguir, crie uma nova lista onde cada um desses elementos aparece apenas uma única vez.

```python
l = [1, 3, 2, 3, 4, 5, 1, 5, 7, 6, 8, 3, 4]
```

### [Exercício 02]

Crie um programa com duas funções. A primeira deve pedir um CEP e o endereço do usuário e armazena-lo em um dicionário. A segunda deve pesquisar um endereço, buscando pelo CEP informado.

🏆 Desafio: Armazene o dicionário em um arquivo.

## 🚀 Mini Projeto 3: Teclado Dominante

Você já parou para pensar de qual lado do teclado vêm as palavras que você digita?

A digitação padronizada (conhecida como _touch typing_) divide o teclado QWERTY em duas zonas principais, designando teclas específicas para os dedos da mão esquerda e da mão direita.

![Mapeamento Qwert](/aula08/mapeamento_qwert.jpeg)

De forma simplificada (considerando o padrão brasileiro ABNT2 e ignorando acentos para facilitar), a divisão funciona assim:

- Mão Esquerda: `q, w, e, r, t, a, s, d, f, g, z, x, c, v, b`
- Mão Direita: `y, u, i, o, p, h, j, k, l, ç, n, m`

### O projeto

Você deve criar um programa que leia um arquivo de texto longo (como um artigo ou um capítulo de livro). O programa deve analisar **palavra por palavra** e determinar se aquela palavra é "dominante da mão esquerda" (tem mais letras da esquerda), "dominante da mão direita", ou "balanceada" (empate).

No final, o programa deve usar um **dicionário** para contabilizar esses totais e imprimir qual é a porcentagem do texto escrita com cada mão!

### Regras

1. Crie dois Sets (`set()`), um com as letras da mão esquerda e outro com as da mão direita. Sets são ideais aqui porque a busca de elementos dentro deles é extremamente rápida!
2. Leia o arquivo `.txt` usando o `with open(...)`;
3. Limpe as palavras (remova pontuações e converta tudo para minúsculas);
4. Use funções;
5. Guarde o placar final em um **Dicionário** (`dict`).

## ✨ Bônus

Além dos tipos de coleção de dados clássicos apresentados na aula de hoje, Python possui alguns tipos utilitários presentes no módulo `collections`:

| Ferramenta | Para que serve | Quando usar |
| ---------- | --------------- | ----------- |
| **`namedtuple`** | Cria tuplas imutáveis com **campos nomeados**. Mantém o desempenho/memória de uma tupla, mas oferece acesso por atributo (`ponto.x`) e métodos úteis (`_replace`, `_asdict`). | Estruturas de dados leves que só agrupariam valores (ex.: coordenadas, result sets) sem precisar da “sobre-carga” de uma classe. |
| **`OrderedDict`** | Dicionário que preserva **ordem de inserção** _e_ expõe APIs extras como `move_to_end` e `popitem(last=False)`. | Quando a ordem faz parte da lógica (LRU cache, serialização com ordem definida). Obs.: desde Py 3.7 a ordem já é garantida em `dict`; o benefício hoje são os métodos adicionais. |
| **`ChainMap`** | “Empilha” vários dicionários e os expõe como **um único mapeamento de leitura/escrita** (procura na sequência). | Construir escopos aninhados (config local → global → default), sobrescrever variáveis sem copiar grandes estruturas. |
| **`Counter`** | Multiconjunto especializado em **contar ocorrências**. Suporta aritmética (`+`, `-`), `.most_common()` e atualização incremental. | Estatísticas rápidas (frequência de palavras, contagem de itens vendidos) ou operações de bag/mochila. |
| **`deque`** | **Fila/stack** baseada em lista duplamente encadeada. Inserções e remoções `O(1)` em ambas as pontas, métodos `appendleft`, `popleft`, `rotate`, `maxlen`. | Implementar filas de tarefas, janelas deslizantes, algor. BFS, LRU simples — sem penar com `pop(0)` em listas normais. |
| **`defaultdict`** | Subclasse de `dict` que chama uma **factory** para criar valores-padrão ao acessar chave ausente. | Contagens (`defaultdict(int)`), agrupamentos (`defaultdict(list/set)`), aninhamento fácil sem `if … in`. |
