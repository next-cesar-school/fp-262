# NExT 26.2 | Fundamentos de Python Aplicado a Dados

![CESAR School](/cesar_school.png)

## Extra - Ambientes Virtuais com `venv` e Instalação de Bibliotecas com `pip`

### Neste material

* O que é um ambiente virtual;
* O que é `pip`;
* Como criar um ambiente virtual;
* Como instalar bibliotecas externas dentro do ambiente;

---

## Contexto

Nas aulas anteriores, nós vimos que Python possui vários recursos nativos que podem ser importados como módulos, como `math`, `random`, `datetime`, `os` e `csv`.

Também vimos que podemos organizar nossos próprios códigos em módulos e pacotes, reaproveitando funções em diferentes arquivos e projetos.

Agora vamos dar um passo importante para trabalhar de forma mais profissional com Python: aprender a criar um **ambiente virtual**.

Esse conteúdo é fundamental porque, a partir do momento em que começamos a instalar bibliotecas externas, como `numpy`, `pandas`, `matplotlib`, `requests` ou outras ferramentas, precisamos organizar melhor o ambiente de desenvolvimento.

Sem essa organização, um projeto pode acabar interferindo em outro.

---

## O problema de quando tudo fica instalado no mesmo lugar

Imagine que você está trabalhando em três projetos diferentes:

```txt
projeto_notas/
projeto_vendas/
projeto_api/
```

No `projeto_notas`, você usa uma versão do NumPy.

No `projeto_vendas`, você usa Pandas e Matplotlib.

No `projeto_api`, você usa uma biblioteca chamada `requests`.

Agora imagine que um desses projetos precisa de uma versão específica de uma biblioteca, mas outro projeto precisa de uma versão diferente.

Isso pode gerar conflitos.

Exemplo:

```txt
Projeto A precisa da biblioteca X na versão 1.0
Projeto B precisa da biblioteca X na versão 2.0
```

Se tudo estiver instalado no mesmo ambiente global do computador, os projetos podem começar a quebrar.

É como se todos os projetos dividissem a mesma gaveta bagunçada de ferramentas.

O ambiente virtual resolve esse problema criando uma “gaveta separada” para cada projeto.

---

## O que é um ambiente virtual?

Um **ambiente virtual** (`venv`) é um espaço isolado dentro do seu projeto Python.

Nesse espaço, ficam instaladas as bibliotecas que aquele projeto precisa.

Cada projeto pode ter seu próprio ambiente virtual, com suas próprias bibliotecas e versões.

Exemplo:

```txt
projeto_notas/
    .venv/
    main.py

projeto_vendas/
    .venv/
    main.py

projeto_api/
    .venv/
    main.py
```

Cada pasta `.venv` representa um ambiente separado.

Assim, o `projeto_notas` pode ter NumPy instalado sem obrigar o `projeto_api` a ter NumPy também.

### `venv` são como as lanchas, e os pedestres são os banhistas

Pense em cada projeto como uma bancada de trabalho.

Sem ambiente virtual:

```txt
Todos os projetos usam a mesma caixa de ferramentas.
```

Com ambiente virtual:

```txt
Cada projeto tem sua própria caixa de ferramentas.
```

Isso evita bagunça, conflito e confusão.

---

## O que é `venv`?

`venv` é um módulo nativo do Python usado para criar ambientes virtuais.

A palavra vem de **Virtual Environment**, ou seja, **ambiente virtual**.

Como o `venv` já vem com o Python, normalmente não precisamos instalar nada extra para usá-lo.

Criamos um ambiente virtual com o comando:

```bash
python -m venv .venv
```

Esse comando significa:

```txt
Use o Python para executar o módulo venv e criar um ambiente chamado .venv
```

Vamos entender por partes:

| Parte do comando | Significado                                     |
| ---------------- | ----------------------------------------------- |
| `python`         | Chama o interpretador Python                    |
| `-m`             | Executa um módulo como programa                 |
| `venv`           | Módulo que cria ambientes virtuais              |
| `.venv`          | Nome da pasta do ambiente virtual (pode mudar)  |

O nome `.venv` é uma convenção comum.

Também seria possível criar com outros nomes:

```bash
python -m venv ambiente
python -m venv env
python -m venv venv
```

Mas, para este curso, vamos usar sempre:

```bash
python -m venv .venv
```

---

## O que é `pip`?

`pip` é o gerenciador de pacotes do Python.

Usamos `pip` para instalar bibliotecas externas.

Exemplo:

```bash
python -m pip install numpy
```

Esse comando instala a biblioteca NumPy no ambiente Python que está sendo usado naquele momento.

### ⚠️ Por que usar `python -m pip` em vez de apenas `pip`?

Você pode encontrar tutoriais usando:

```bash
pip install numpy
```

Isso pode funcionar.

Mas, durante o aprendizado, é mais seguro usar:

```bash
python -m pip install numpy
```

Assim, deixamos mais claro qual Python está chamando o `pip`. Isso é especialmente útil quando você tem mais de uma versão do Python instalada no seu computador.

Quando estamos usando ambiente virtual, isso ajuda a reduzir confusões.

---

## Criando um projeto do zero no VS Code

Vamos criar um projeto simples.

### Passo 1 - Criar uma pasta

Crie uma pasta chamada:

```txt
aula_venv
```

### Passo 2 - Abrir a pasta no VS Code

No VS Code:

```txt
File > Open Folder...
```

Escolha a pasta `aula_venv`.

> ⚠️ Atenção: é importante abrir a pasta do projeto no VS Code, e não apenas abrir um arquivo solto.

---

## Criando o ambiente virtual pelo terminal do VS Code

No VS Code, abra o terminal integrado:

```txt
Terminal > New Terminal
```

Ou use o atalho:

```txt
Ctrl + Shift + '
```

No terminal, execute:

```bash
python -m venv .venv
```

Se estiver no Windows e o comando `python` não funcionar, tente:

```bash
py -m venv .venv
```

Se estiver no Linux ou macOS e o comando `python` não funcionar, tente:

```bash
python3 -m venv .venv
```

Depois disso, a estrutura do projeto deve ficar parecida com:

```txt
aula_venv/
    .venv/
```

A pasta `.venv` contém arquivos internos do ambiente virtual.

Não é necessário mexer manualmente nela.

---

## Ativando o ambiente virtual

Criar o ambiente virtual não é a mesma coisa que ativar.

Depois de criar, precisamos ativar o ambiente.

### 8.1 Ativação no Windows usando PowerShell

No terminal do VS Code, use:

```bash
.venv\Scripts\Activate.ps1
```

Se funcionar, o terminal deve mostrar algo parecido com:

```bash
(.venv) PS C:\caminho\do\projeto>
```

O `(.venv)` no começo da linha indica que o ambiente virtual está ativo.

### 8.2 Ativação no Windows usando Prompt de Comando

Se o terminal estiver usando `cmd`, o comando é:

```bash
.venv\Scripts\activate.bat
```

### 8.3 Ativação no Linux ou macOS

```bash
source .venv/bin/activate
```

### 8.4 Desativando o ambiente virtual

Para sair do ambiente virtual, use:

```bash
deactivate
```

Depois disso, o `(.venv)` desaparece do terminal.

---

## Problema comum no Windows: script bloqueado no PowerShell

Às vezes, ao tentar ativar o ambiente no PowerShell, aparece um erro parecido com:

```txt
running scripts is disabled on this system
```

Isso acontece por causa da política de execução de scripts do PowerShell.

Uma forma comum de resolver para o usuário atual é executar:

```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Depois, tente ativar novamente:

```bash
.venv\Scripts\Activate.ps1
```

> ⚠️ Em computadores institucionais, algumas permissões podem ser bloqueadas por política de segurança. Nesse caso, use o terminal `cmd`, o Git Bash, ou peça orientação ao monitor.

---

## Selecionando o interpretador Python no VS Code

Além de ativar o ambiente no terminal, precisamos garantir que o VS Code está usando o Python correto.

No VS Code:

1. Pressione:

    ```txt
    Ctrl + Shift + P
    ```

2. Digite:

    ```txt
    Python: Select Interpreter
    ```

3. Escolha o interpretador que aponta para a pasta `.venv`.

    Ele pode aparecer de forma parecida com:

    ```txt
    .venv\Scripts\python.exe
    ```

    No Windows, ou:

    ```txt
    .venv/bin/python
    ```

    No Linux/macOS.

### Como saber se escolhi o ambiente certo?

Veja se o caminho do interpretador selecionado contém `.venv`.

Exemplo esperado:

```txt
aula_venv/.venv/Scripts/python.exe
```

ou:

```txt
aula_venv/.venv/bin/python
```

Se aparecer um Python instalado globalmente no computador, como:

```txt
C:\Python312\python.exe
```

ou:

```txt
/usr/bin/python3
```

talvez você não esteja usando o ambiente virtual do projeto.

---

## Checando se o VS Code está usando o ambiente correto

Crie um arquivo chamado:

```txt
main.py
```

Dentro dele, escreva:

```python
import sys

print(sys.executable)
```

Execute o arquivo.

A saída deve mostrar um caminho contendo `.venv`.

Exemplo:

```txt
C:\Users\Aluno\aula_venv\.venv\Scripts\python.exe
```

ou:

```txt
/home/aluno/aula_venv/.venv/bin/python
```

Se aparecer `.venv`, o VS Code está usando o ambiente correto.

---

## Instalando bibliotecas externas com `pip`

Agora vamos instalar uma biblioteca externa.

Com o ambiente virtual ativo, execute:

```bash
python -m pip install numpy
```

Depois, crie este código no `main.py`:

```python
import numpy as np

valores = np.array([10, 20, 30])
print(valores)
print(valores.mean())
```

Se tudo estiver certo, o programa deve rodar sem erro.

### O que aconteceu?

O `pip` baixou e instalou o NumPy dentro do ambiente virtual do projeto.

Ou seja, o NumPy não foi instalado “solto” no computador inteiro.

Ele foi instalado dentro da pasta `.venv`.

---

## Como verificar bibliotecas instaladas

Com o ambiente virtual ativo, use:

```bash
python -m pip list
```

Esse comando mostra as bibliotecas instaladas no ambiente atual.

Exemplo de saída:

```txt
Package    Version
---------- -------
numpy      2.x.x
pip        25.x.x
```

Também podemos checar informações de uma biblioteca específica:

```bash
python -m pip show numpy
```

Isso mostra detalhes como:

```txt
Name: numpy
Version: ...
Location: ...
```

Observe especialmente o campo `Location`.

Ele deve apontar para uma pasta dentro da `.venv`.

---

## Extra do Extra

### Atualizando o `pip`

Em alguns casos, o terminal pode sugerir atualizar o `pip`.

O comando é:

```bash
python -m pip install --upgrade pip
```

Isso atualiza o gerenciador de pacotes dentro do ambiente atual.

---

### Instalando outras bibliotecas

Exemplos:

```bash
python -m pip install pandas
```

```bash
python -m pip install matplotlib
```

```bash
python -m pip install requests
```

Também é possível instalar mais de uma biblioteca no mesmo comando:

```bash
python -m pip install numpy pandas matplotlib
```

---

### Testando uma biblioteca instalada

Depois de instalar uma biblioteca, o teste mais simples é tentar importá-la em um arquivo Python.

Exemplo com `requests`:

```bash
python -m pip install requests
```

No `main.py`:

```python
import requests

resposta = requests.get("https://httpbin.org/get")
print(resposta.status_code)
```

Se o código mostrar:

```txt
200
```

significa que a requisição funcionou.

> ⚠️ Se a internet estiver bloqueada ou instável, esse exemplo pode falhar mesmo com a biblioteca instalada corretamente.

---

### Criando um arquivo `requirements.txt`

Quando instalamos bibliotecas em um projeto, precisamos registrar quais são essas bibliotecas.

Assim, outra pessoa consegue preparar o mesmo ambiente no computador dela.

Para isso, usamos um arquivo chamado:

```txt
requirements.txt
```

Para gerar esse arquivo, use:

```bash
python -m pip freeze > requirements.txt
```

Isso cria um arquivo com as bibliotecas instaladas e suas versões.

Exemplo:

```txt
numpy==2.2.0
pandas==2.2.3
matplotlib==3.10.0
```

### Para que serve esse arquivo?

Ele serve para reproduzir o ambiente.

Se outra pessoa baixar seu projeto, ela poderá instalar as dependências com:

```bash
python -m pip install -r requirements.txt
```

Ou seja:

```txt
Instale tudo que está listado dentro do requirements.txt
```

---

## Fluxo completo de um projeto Python com `venv`

Um fluxo comum seria:

### 1. Criar a pasta do projeto

```txt
meu_projeto/
```

### 2. Abrir a pasta no VS Code

```txt
File > Open Folder
```

### 3. Criar o ambiente virtual

```bash
python -m venv .venv
```

### 4. Ativar o ambiente virtual

Windows PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

Windows cmd:

```bash
.venv\Scripts\activate.bat
```

Linux/macOS:

```bash
source .venv/bin/activate
```

### 5. Selecionar o interpretador no VS Code

```txt
Ctrl + Shift + P
Python: Select Interpreter
Escolher o Python dentro da .venv
```

### 6. Instalar bibliotecas

```bash
python -m pip install numpy pandas matplotlib
```

### 7. Testar no código

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("Bibliotecas importadas com sucesso!")
```

### 8. Registrar dependências

```bash
python -m pip freeze > requirements.txt
```

---

## Estrutura recomendada de projeto

Uma estrutura simples para os projetos da disciplina pode ser:

```txt
meu_projeto/
    .venv/
    main.py
    requirements.txt
    README.md
```

Em projetos um pouco maiores:

```txt
meu_projeto/
    .venv/
    src/
        main.py
        analise.py
    dados/
        entrada.csv
    docs/
        anotacoes.md
    requirements.txt
    README.md
```

A pasta `.venv` fica no projeto, mas normalmente não deve ser enviada para o GitHub.

---

## `.gitignore`: o que não versionar

Se o projeto usar Git/GitHub, crie um arquivo chamado `.gitignore`.

Dentro dele, coloque:

```txt
.venv/
__pycache__/
*.pyc
```

Isso evita enviar para o repositório arquivos desnecessários.

### Por que não enviar a `.venv`?

Porque a `.venv` pode ser grande e depende do computador onde foi criada.

O ideal é enviar o `requirements.txt`.

Assim, cada pessoa recria o ambiente no próprio computador.

---

## Como recriar um ambiente a partir de um projeto existente

Imagine que você recebeu um projeto com esta estrutura:

```txt
projeto_recebido/
    main.py
    requirements.txt
```

Para preparar o ambiente:

### 1. Abrir a pasta no VS Code

```txt
File > Open Folder
```

### 2. Criar o ambiente virtual

```bash
python -m venv .venv
```

### 3. Ativar o ambiente

Windows PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
source .venv/bin/activate
```

### 4. Instalar as dependências

```bash
python -m pip install -r requirements.txt
```

### 5. Selecionar interpretador no VS Code

```txt
Python: Select Interpreter
```

Escolha o Python dentro de `.venv`.

### 6. Rodar o projeto

```bash
python main.py
```

---

## Checagens importantes no VS Code

Quando algo não funcionar, verifique:

### O terminal mostra `(.venv)`?

Exemplo esperado:

```bash
(.venv) PS C:\Users\Aluno\meu_projeto>
```

Se não aparecer, talvez o ambiente não esteja ativo.

### O interpretador selecionado tem `.venv` no caminho?

Use:

```txt
Ctrl + Shift + P
Python: Select Interpreter
```

Escolha o ambiente correto.

### O Python usado pelo código é o da `.venv`?

No `main.py`:

```python
import sys

print(sys.executable)
```

O resultado deve conter `.venv`.

### A biblioteca aparece no `pip list`?

No terminal:

```bash
python -m pip list
```

Veja se a biblioteca está na lista.

### A biblioteca foi instalada no ambiente certo?

Use:

```bash
python -m pip show nome_da_biblioteca
```

Exemplo:

```bash
python -m pip show numpy
```

Veja se o campo `Location` aponta para a `.venv`.

---

## Erros comuns

### Criar o ambiente, mas esquecer de ativar

Problema:

```bash
python -m pip install numpy
```

A biblioteca pode ser instalada fora do ambiente virtual.

Solução:

Ative o ambiente antes:

```bash
.venv\Scripts\Activate.ps1
```

ou:

```bash
source .venv/bin/activate
```

Depois instale:

```bash
python -m pip install numpy
```

---

### Instalar a biblioteca, mas o VS Code usar outro Python

Problema:

```python
ModuleNotFoundError: No module named 'numpy'
```

Mesmo depois de instalar o NumPy.

Possível causa:

O NumPy foi instalado em um ambiente, mas o VS Code está executando outro Python.

Solução:

1. Use `Python: Select Interpreter`;
2. Escolha o Python dentro da `.venv`;
3. Rode novamente o programa.

---

### Abrir apenas o arquivo, em vez da pasta

Problema:

O VS Code pode não encontrar corretamente a `.venv`.

Solução:

Abra a pasta do projeto:

```txt
File > Open Folder
```

---

### Criar a `.venv` no lugar errado

Problema:

Você cria a `.venv` fora da pasta do projeto.

Solução:

Antes de criar, confira onde o terminal está:

```bash
pwd
```

No Windows PowerShell, também funciona:

```bash
pwd
```

Ou use:

```bash
ls
```

para listar os arquivos da pasta atual.

---

### Misturar comandos de sistemas diferentes

No Windows PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

No Linux/macOS:

```bash
source .venv/bin/activate
```

Não adianta usar `source` no PowerShell, nem `Activate.ps1` no Linux.

---

## Boas práticas

1. **Crie um ambiente virtual para cada projeto.**

   Evite instalar tudo no Python global do computador.

2. **Use o nome `.venv`.**

   Esse nome é comum e o VS Code costuma reconhecer bem.

3. **Ative o ambiente antes de instalar bibliotecas.**

   Assim, as dependências ficam no lugar certo.

4. **Use `python -m pip install`.**

   Isso reduz a chance de usar um `pip` associado ao Python errado.

5. **Crie um `requirements.txt`.**

   Ele ajuda outras pessoas a recriar o ambiente.

6. **Não envie a pasta `.venv` para o GitHub.**

   Envie o `requirements.txt`.

7. **Cheque o interpretador no VS Code.**

   O ambiente virtual ativo no terminal e o interpretador selecionado pelo VS Code precisam estar alinhados.

8. **Não instale bibliotecas sem necessidade.**

   Cada biblioteca adicionada aumenta a complexidade do projeto.

---

## Resumo dos principais comandos

| Objetivo                                    | Comando                                     |
| ------------------------------------------- | ------------------------------------------- |
| Criar ambiente virtual                      | `python -m venv .venv`                      |
| Criar ambiente no Windows com `py`          | `py -m venv .venv`                          |
| Criar ambiente no Linux/macOS com `python3` | `python3 -m venv .venv`                     |
| Ativar no PowerShell                        | `.venv\Scripts\Activate.ps1`                |
| Ativar no cmd                               | `.venv\Scripts\activate.bat`                |
| Ativar no Linux/macOS                       | `source .venv/bin/activate`                 |
| Desativar ambiente                          | `deactivate`                                |
| Instalar biblioteca                         | `python -m pip install nome`                |
| Instalar NumPy                              | `python -m pip install numpy`               |
| Listar bibliotecas instaladas               | `python -m pip list`                        |
| Ver detalhes de biblioteca                  | `python -m pip show nome`                   |
| Atualizar pip                               | `python -m pip install --upgrade pip`       |
| Gerar `requirements.txt`                    | `python -m pip freeze > requirements.txt`   |
| Instalar a partir do `requirements.txt`     | `python -m pip install -r requirements.txt` |
