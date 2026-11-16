# NExT 26.2 | Fundamentos de Python Aplicado a Dados

![CESAR School](/cesar_school.png)

## Aula 09 - Módulos e Pacotes

### Na aula de hoje

- O que são módulos;
- Como utilizar alguns dos principais módulos nativos do Python;
- Boas práticas no uso de módulos.

---

## Módulos

À medida que nossos programas se tornam maiores e mais complexos, organizar o código é essencial. Em Python, usamos **módulos** e **pacotes** para dividir programas em partes menores e reutilizáveis. Além disso, Python oferece uma ampla gama de módulos nativos que já resolvem muitos problemas comuns, como manipulação de arquivos, cálculos matemáticos, operações com datas e tempo, entre outros.

## 🧰 Módulo

Por mais que a linguagem Python venha com uma série de recursos que otimizam bastante o tempo de desenvolvimento dos algoritmos, ela não é completa. Há uma série de cálculos, estruturas de dados e recursos para tratar com formatos de arquivos específicos que não está disponível nativamente na linguagem.

Para evitar o esforço de "reinventar a roda", podemos importar tais recursos desenvolvidos por outros programadores como **módulos**.

Um módulo é um arquivo Python que contém definições e implementações de funções, _classes_ e variáveis. O Python já vem com uma grande quantidade de módulos prontos para uso, conhecidos como **biblioteca padrão**.

### Importando módulos

Quando instalamos o Python, ele vem acompanhado de dezenas de módulos. A lista completa pode ser encontrada [aqui](https://docs.python.org/3/py-modindex.html).

Destacamos alguns:

- [calendar](https://docs.python.org/3/library/calendar.html#module-calendar)
- [copy](https://docs.python.org/3/library/copy.html#module-copy)
- [csv](https://docs.python.org/3/library/csv.html#module-csv)
- [datetime](https://docs.python.org/3/library/datetime.html#module-datetime)
- [json](https://docs.python.org/3/library/json.html#module-json)
- [statistics](https://docs.python.org/3/library/statistics.html#module-statistics)

Para adicionar um módulo, basta usar o comando `import` seguido no nome do módulo.

Existem três formas principais de importar módulos:

1. **Importar o módulo inteiro:**

    ```python
    import math


    print(math.sqrt(16))  # Saída: 4.0
    ```

2. **Importar elementos específicos do módulo:**

    ```python
    from math import sqrt, pi


    print(sqrt(25))  # Saída: 5.0
    print(pi)        # Saída: 3.141592653589793
    ```

3. **Importar com alias (apelido):**

    ```python
    import math as m


    print(m.sqrt(9))  # Saída: 3.0
    ```

## Principais Módulos Nativos do Python

### 🔢 `math`

Módulo matemático.

Fornece recursos matemáticos baseados na linguagem C, como cálculos trigonométricos, fatoriais e exponenciais. Mais detalhes [aqui](https://docs.python.org/3/library/math.html#module-math).

```python
import math


print(math.sqrt(16))      # Raiz quadrada: 4.0
print(math.factorial(5))  # Fatorial: 120
print(math.pi)            # Valor de pi: 3.141592653589793
print(math.pow(2, 3))     # Potenciação: 2³
print(math.ceil(1.1))     # Arredondamento para cima
print(math.floor(1.9))    # Arredondamento para baixo
```

> ℹ️ Para fazer o arredondamento automático, usamos `round(numero)` ou `round(numero, casas)`

### 🔀 `random`

O módulo `random` permite trabalhar com geração de números pseudo-aleatórios e escolha de elementos de coleções.

Mais detalhes [aqui](https://docs.python.org/3/library/random.html#module-random).

Exemplo de uso:

```python
import random


print(random.randint(1, 10))             # Número aleatório entre 1 e 10
print(random.choice(['a', 'b', 'c']))    # Escolhe aleatoriamente um elemento da lista
print(random.sample(range(100), 5))      # Escolhe 5 números aleatórios sem repetição

nums = [1, 2, 3, 4, 5]
random.shuffle(nums)                     # Embaralha toda a lista (não retorna nada)
```

### 📅 `datetime`

O módulo `datetime` é usado para trabalhar com datas e horas.

Exemplo de uso:

```python
from datetime import datetime, timedelta


agora = datetime.now()
print(agora)  # Data e hora atual

amanha = agora + timedelta(days=1)
print(amanha)  # Data e hora de amanhã

data_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")
print(data_formatada)  # Exibe data formatada
```

### 💻 `os`

O módulo `os` permite interagir com o sistema operacional, como navegar em diretórios, criar pastas e acessar variáveis de ambiente.

Mais detalhes [aqui](https://docs.python.org/3/library/os.html#module-os).

> **⚠️ CUIDADO!**\
> Como esse módulo manipula os arquivos e pastas no seu computador, cuidado para não deletar ou alterar algo por acidente!

```python
import os


print(os.getcwd())          # Diretório atual
os.mkdir("nova_pasta")      # Cria uma pasta chamada 'nova_pasta'
os.rmdir("nova_pasta")      # ⚠️ Remove a pasta chamada 'nova_pasta'
os.path.exists('teste.txt') # Verifica se um caminho existe
```

### 🎲 `csv`

O módulo csv facilita a leitura e escrita de arquivos no formato CSV (Comma-Separated Values), amplamente utilizado para troca de dados entre sistemas.

#### Leitura de arquivos CSV

Para ler um arquivo CSV, usamos `csv.reader`, que retorna as linhas como listas.

Exemplo de leitura:

```python
import csv


with open("dados.csv", "r") as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)
```

#### Escrita em arquivos CSV

Para escrever em um arquivo CSV, usamos `csv.writer`, que permite adicionar linhas de dados.

Exemplo de escrita:

```python
import csv


dados = [
    ["Nome", "Idade", "Cidade"],
    ["Frederico", 30, "Recife"],
    ["Ana", 25, "São Paulo"],
    ["Beto", 35, "Olinda"]
]

with open("saida.csv", "w", newline="") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(dados)
```

#### Usando `DictReader` e `DictWriter`

Podemos ler e escrever arquivos CSV como dicionários, onde cada linha é um dicionário com as colunas como chaves.

Exemplo com `DictReader`:

```python
import csv


with open("dados.csv", "r") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        print(linha)  # Cada linha é um dicionário
```

Exemplo com `DictWriter`:

```python
import csv


dados = [
    {"Nome": "Frederico", "Idade": 30, "Cidade": "Recife"},
    {"Nome": "Ana", "Idade": 25, "Cidade": "São Paulo"},
    {"Nome": "Beto", "Idade": 35, "Cidade": "Olinda"}
]

with open("saida.csv", "w", newline="") as arquivo:
    campos = ["Nome", "Idade", "Cidade"]
    escritor = csv.DictWriter(arquivo, fieldnames=campos)
    escritor.writeheader()  # Escreve o cabeçalho
    escritor.writerows(dados)
```

## Boas Práticas ao Usar Módulos

1. Importe apenas o necessário:

    Evite importar módulos ou funções que não serão usados.

2. Organize as importações:

    Coloque todas as importações no início do arquivo.

3. Use nomes descritivos:

    Evite usar alias que dificultem a leitura do código.

4. Aproveite a biblioteca padrão:

    Antes de criar suas próprias funções, verifique se já existe um módulo nativo que resolva o problema.

### Benefícios dos módulos

- Reutilização de código em diferentes projetos;
- Redução da duplicação de código;
- Facilitação na manutenção e organização.

## Criando um módulo

1. Crie um arquivo Python com o nome `meu_modulo.py`:

    ```python
    # Arquivo: meu_modulo.py
    def saudacao(nome):
        return f"Olá, {nome}! Bem-vindo ao NExT."
    ```

2. Use o módulo em outro arquivo:

    ```python
    # Arquivo: exemplo.py
    import meu_modulo


    print(meu_modulo.saudacao("Erick"))

## 📦 Pacotes

Em casos onde vários módulos fazem parte de uma mesma solução, pode ser interessante agrupá-los em pacotes (packages).

Um pacote é uma coleção de módulos organizados em um diretório. Ele contém um arquivo especial `__init__.py` que pode estar vazio ou conter código de inicialização. Quando fazemos um `import`, é possível importar todos os módulos de um pacote, ou apenas alguns específicos.

## Estrutura de um pacote

Um pacote chamado `calculadora` com dois módulos (`basico.py` e `cientifico.py`) poderia ter a seguinte estrutura:

```txt
calculadora/
    __init__.py
    basico.py
    cientifico.py
```

### Exemplo de Pacote

1. `basico.py`:

    ```python
    def somar(a, b):
        return a + b

    def subtrair(a, b):
        return a - b
    ```

2. `cientifico.py`:

    ```python
    def raiz_quadrada(x):
        return x ** 0.5

    def potencia(base, expoente):
        return base ** expoente
    ```

3. Uso do pacote em um programa:

    ```python
    from calculadora.basico import somar
    from calculadora.cientifico import raiz_quadrada

    print(somar(2, 3))           # Saída: 5
    print(raiz_quadrada(16))     # Saída: 4.0
    ```

## Benefícios da Modularidade

- **Organização**: Divide o código em partes menores e mais gerenciáveis.
- **Reutilização**: Permite usar o mesmo código em diferentes projetos.
- **Testabilidade**: Módulos menores são mais fáceis de testar e depurar.
- **Manutenção**: Atualizações são localizadas, reduzindo o impacto em outras partes do sistema.

## Boas Práticas na Criação de Módulos e Pacotes

1. Use nomes descritivos:
    - Nomeie módulos e pacotes de forma clara e concisa;
    - Evite abreviações confusas.

2. Evite importações circulares:
    - Não crie dependências entre módulos que se importam mutuamente.

3. Organize arquivos relacionados:
    - Agrupe módulos com funções semelhantes em pacotes.

4. Use o arquivo `__init__.py`:
    - Utilize-o para inicializar pacotes e expor apenas o necessário.

5. Documente seus módulos:
    - Inclua docstrings para descrever a finalidade de cada módulo e função.

## Bônus - Easter Eggs do Python

Existem alguns pequenos segredos escondidos na própria linguagem que revelam o bom-humor da comunidade e, de quebra, ajudam a fixar conceitos sobre módulos e importação.

1. `import this` – O Zen of Python

    Quando você digita `import this` no interpretador, o Python carrega um poema com 19 princípios de design que norteiam a linguagem.

    Não tem finalidade prática direta no código, mas é um lembrete elegante dos valores de legibilidade e simplicidade que buscamos ao programar. Ótimo para abrir discussões sobre boas práticas antes de aprofundar em PEP 8 (nas próximas aulas).

2. `from __future__ import braces` – {} Chaves em Python

    O módulo `__future__` é usado oficialmente para habilitar recursos que chegarão em versões futuras (ex.: `from __future__ import annotations`).

    Este módulo promete ativar suporte a {} como delimitadores de bloco (à moda de C/Java).

3. (Extra) `import antigravity`

## 🧱 Exercícios Fundamentais

### [Exercício 01]

A partir do valor do raio informado pelo usuário, calcule a área da circunferência utilizando funções e π (pi) do modulo `math`.

### [Exercício 02]

Use o módulo `math` para calcular e exibir:
    - A raiz quadrada de 144;
    - O valor do cosseno de 45° (em radianos);
    - O valor da constante `e` elevado a 2.

### [Exercício 03]

Crie uma função que atue como um simulador de dado 🎲 (valor entre 1 e 6). Se o valor for igual a 6, exiba a mensagem: "Dano Crítico!".

### [Exercício 04]

Use o módulo `random` para criar um jogo onde o programa escolhe um número aleatório entre 0 e 10 e o usuário deve tentar adivinhar o valor. Quando a pessoa acertar, deve ser apresentado uma pontuação (se acertar de primeira, 10 pontos, na segunda tentativa, 9 pontos...)

### [Exercício 05]

Use o módulo `datetime` para implementar uma função que retorne quanto tempo falta para o final deste módulo:
    - Exiba o tempo seguindo o formato: `Tempo restante para o fim do módulo: XX dias e YY horas`;

### [Exercício 06]

Use o módulo `csv` para refazer as questões do desafio `PyFinanceiro` e `PyVotação`, da aula de arquivos. Use os recursos relacionados ao `DictReader` para ler o código e adapte a saída para usar o `DictWriter`.

## 🚀 Mini Projeto 4: Pacote de Utilidades

### Contexto

No dia a dia de um Analista ou Engenheiro de Dados, é muito comum escrevermos pequenas funções que resolvem problemas repetitivos (como limpar um texto ou fazer um cálculo específico). Em vez de copiar e colar essas funções em todos os nossos códigos, nós criamos Pacotes! Neste projeto, você vai criar a sua própria biblioteca de utilidades e importá-la em um programa principal.

### O Desafio

Você deve criar um pacote chamado `utilidades` que conterá dois módulos distintos: um para manipular textos e outro para realizar cálculos matemáticos.

### Passo a Passo

1. Crie uma pasta principal para o seu projeto;
2. Dentro dela, crie uma pasta chamada utilidades (este será o seu pacote);
3. Dentro da pasta utilidades, crie um arquivo vazio chamado `__init__.py` para que o Python reconheça a pasta como um pacote válido;
4. Ainda dentro de utilidades, crie um arquivo chamado `strings.py` e programe duas funções:
   - `contar_vogais(texto)`: Recebe uma string e retorna a quantidade de vogais nela;
   - `inverter(texto)`: Recebe uma string e retorna o texto de trás para frente.
5. Crie outro arquivo chamado `numeros.py` (dentro de utilidades) com duas funções:
   - `eh_primo(n)`: Verifica se um número inteiro é primo (retorna `True` ou `False`);
   - `fatorial(n)`: Calcula e retorna o fatorial do número recebido.
6. Por fim, volte para a pasta principal do projeto (fora de utilidades) e crie um arquivo chamado `main.py`;
7. No seu `main.py`, importe o seu pacote e teste as quatro funções criadas, imprimindo os resultados na tela!

### Estrutura visual esperada do seu projeto

```txt
meu_projeto/
    main.py
    utilidades/
        __init__.py
        strings.py
        numeros.py
```

## 🚀 Mini Projeto 5: Template Automatizado

### Contexto

Sempre que iniciamos um novo projeto de Análise de Dados, precisamos criar a mesma estrutura de pastas repetidas vezes (uma pasta para dados, outra para documentação, arquivos em branco, etc.). Como bons programadores, nós não fazemos trabalho braçal duas vezes: vamos usar o Python para automatizar isso!

### O Desafio

Você deve criar um script que utilize o módulo nativo `os` para gerar automaticamente uma estrutura básica de pastas e arquivos para novos projetos.

### Passo a Passo

1. Importe o módulo `os` no seu script;
2. Use o comando `input()` para perguntar ao usuário qual será o nome do novo projeto;
3. Utilize a função `os.mkdir()` para criar a pasta raiz (principal) com o nome que o usuário digitou;
4. Dentro dessa nova pasta raiz, crie dois subdiretórios: `src` (onde ficariam os códigos) e `docs` (onde ficaria a documentação). Dica: Utilize a função `os.path.join(pasta_raiz, 'src')` para garantir que os caminhos sejam montados corretamente independentemente do sistema operacional;
5. Crie um arquivo de texto vazio chamado `README.md` dentro da pasta docs recém-criada. Lembre-se de usar o `with open(...)` no modo de escrita (`w`);
6. Crie um arquivo vazio chamado `main.py` diretamente na pasta raiz do projeto;
7. Imprima uma mensagem de sucesso avisando que a estrutura do projeto foi criada!

### Estrutura visual que o seu script deve gerar automaticamente

```txt
nome_digitado_pelo_usuario/
    main.py
    src/
    docs/
        README.md
```

## 🚀 Mini Projeto 6: 👀 Tipoglicemia

### 🧠 O que é a Tipoglicemia?

A tipoglicemia (um neologismo que mistura "tipografia" com "hipoglicemia") é um fenômeno cognitivo muito interessante sobre como o cérebro humano processa a leitura.

A teoria por trás desse fenômeno afirma que nós não lemos letra por letra, mas sim a palavra como um todo. Por causa disso, desde que a primeira e a última letra de uma palavra estejam na posição correta, as letras do meio podem estar totalmente embaralhadas e, ainda assim, conseguiremos ler e compreender o texto com certa fluidez.

### 📝 Exemplo de Texto Tipoglicêmico

"De aocdro com uma psqeiusa de uma uivnersdiade ignlsea, não ipmotra em qaul odrem as lteras de uma plavara etsão, a úncia ciosa ipmotratne é que a piremria e a útlima ltera etejasm no lguar crteo. O rseto pdoe ser uma bgaunça ttoal, que vcoê aìdna pdoe ler sem porbelma. Itso é poqrue nós não lemos cdaa ltera isloada, mas a plavara cmoo um tdoo."

### Contexto

Estudiosos de linguística e ciência cognitiva adoram o fenômeno da tipoglicemia. Para ajudar em uma pesquisa, eles pediram que você criasse um programa capaz de pegar qualquer texto comum e transformá-lo em um texto tipoglicêmico automaticamente.

### O Desafio

Você deve criar um programa que leia um arquivo de texto de entrada (`texto_normal.txt`), embaralhe as letras internas de cada palavra e salve o resultado em um novo arquivo de saída (`texto_embaralhado.txt`).

### Regras do Programa

1. Importe o módulo nativo `random`;
2. O programa deve abrir e ler o arquivo de entrada;
3. Para cada palavra lida, o programa deve verificar o tamanho dela. Palavras com 3 letras ou menos (como "um", "de", "nós") não devem ser alteradas;
4. Para palavras maiores que 3 letras, mantenha a primeira e a última letra no mesmo lugar, e embaralhe apenas as letras do meio (dica: a função random.`shuffle()` será muito útil aqui);
5. Grave o texto modificado no arquivo de saída.
