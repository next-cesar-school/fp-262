# 🛠️ Projeto 1: PyPipeline, ETL de Vendas

> **Área:** Engenharia de Dados · **Nível:** ⭐⭐ · **Tempo estimado:** 6 a 8 horas
> **Conteúdos usados:** arquivos (Aula 06), exceções e ETL (Aula 07), `set` e `dict` (Aula 08), funções (Aula 05)

## 📖 Contexto

A **Loja NExT** vende online para várias cidades de Pernambuco. Todo mês, o sistema de vendas exporta um arquivo com os pedidos. O problema é que esse sistema é antigo e foi alimentado por pessoas diferentes, de jeitos diferentes:

- uma pessoa escreve a data como `2025-03-14`, outra como `14/03/2025`;
- o preço às vezes vem como `49.90`, às vezes `49,90`, às vezes `R$ 49,90`;
- tem `RECIFE`, `Recife` e `  recife `;
- tem pedido exportado **duas vezes**;
- e tem linha que simplesmente não dá pra aproveitar (quantidade `"dois"`, preço `"grátis"`, data `31/02/2025`...).

A diretoria quer um painel de vendas, mas **ninguém confia nos números** enquanto os dados estiverem assim. Sua missão é construir o **pipeline** que transforma esse arquivo bagunçado em uma base **limpa e confiável**, e que mostra com transparência **o que foi descartado e por quê**.

> 💬 Esse é o trabalho de quem faz **Engenharia de Dados**: garantir que o dado chegue limpo, padronizado e rastreável para quem vai analisá-lo. No exercício 04 da Aula 07 você fez uma versão pequena disso. Agora é pra valer.

## 🎯 Objetivo

Escrever um programa que execute as 3 etapas de um **pipeline ETL**:

```txt
 ┌────────────────────┐       ┌───────────────────────────┐      ┌──────────────────────────┐
 │      EXTRACT       │       │         TRANSFORM         │      │           LOAD           │
 │ vendas_brutas.csv  │ ───▶ │ valida · corrige · padro- │ ───▶ │ vendas_limpas.csv        │
 │ (1.239 linhas)     │       │ niza · remove duplicatas  │      │ rejeitados.csv           │
 └────────────────────┘       └───────────────────────────┘      │ relatorio_etl.txt        │
                                                                 └──────────────────────────┘
```

## 📦 Dados de entrada

Arquivo: [`dados/vendas_brutas.csv`](dados/vendas_brutas.csv). Os dados são fictícios e se referem ao 1º semestre de 2025.

⚠️ **Atenção:** o separador é **ponto e vírgula (`;`)**, e não vírgula. É o padrão de muitos sistemas brasileiros, porque a vírgula é usada como separador decimal.

```txt
id_pedido;data;cliente;cidade;categoria;produto;quantidade;preco_unitario;forma_pagamento
PED-00001;04/02/2025;Felipe Santos;Recife;Esporte;Mochila Esportiva;2;159.00;cartão de crédito
PED-00002;27/01/2025;Carla Oliveira;Petrolina;Papelaria;Caderno Inteligente;3;R$ 89,00;CARTÃO DE CRÉDITO
PED-00003;2025-06-30;Otávio Santos;CARUARU;Esporte;Tênis de Corrida;dois;349.90;pix
```

### Dicionário de dados

| Coluna | Tipo esperado | Descrição |
| ------ | ------------- | --------- |
| `id_pedido` | texto | Identificador único do pedido (ex.: `PED-00042`) |
| `data` | data | Data do pedido. Aparece como `AAAA-MM-DD` **ou** `DD/MM/AAAA` |
| `cliente` | texto | Nome do cliente |
| `cidade` | texto | Cidade de entrega |
| `categoria` | texto | Categoria do produto |
| `produto` | texto | Nome do produto |
| `quantidade` | inteiro | Unidades compradas |
| `preco_unitario` | decimal | Preço de uma unidade |
| `forma_pagamento` | texto | Pix, cartão de crédito, cartão de débito ou boleto |

## 🔍 Passo 0: investigue antes de programar

Antes de escrever qualquer linha de código, **abra o arquivo** no VS Code e passe uns 10 minutos observando. Anote todos os tipos de problema que encontrar. Profissionais de dados chamam isso de **profiling**. Depois compare a sua lista com as regras abaixo: encontrou algum problema que não está nelas?

## 📏 Regras de negócio

Para que todo mundo chegue aos **mesmos números**, siga exatamente estas regras.

### A) Problemas que devem ser **CORRIGIDOS** (a linha continua válida)

| Campo | Problema | Como corrigir | Exemplo |
| ----- | -------- | ------------- | ------- |
| `data` | Dois formatos | Converter tudo para `AAAA-MM-DD` | `14/03/2025` → `2025-03-14` |
| `cidade` | Maiúsculas, minúsculas e espaços sobrando | `strip()` + `title()` | `'  recife '` → `Recife` |
| `categoria` | Maiúsculas e minúsculas misturadas | `strip()` + `capitalize()` | `eletrônicos` → `Eletrônicos` |
| `preco_unitario` | `R$` e vírgula decimal | Remover `R$`, espaços e trocar `,` por `.` | `R$ 89,00` → `89.0` |
| `forma_pagamento` | Maiúsculas e falta de acento | Padronizar com um **dicionário** de/para | `CARTAO DE CREDITO` → `Cartão de Crédito` |

Os valores finais de `forma_pagamento` devem ser **apenas**: `Pix`, `Cartão de Crédito`, `Cartão de Débito` e `Boleto`.

### B) Problemas que devem ser **REJEITADOS** (a linha vai para `rejeitados.csv`)

Verifique **nesta ordem**. O **primeiro** problema encontrado é o motivo registrado:

| Ordem | Verificação | Motivo (texto exato) |
| :---: | ----------- | -------------------- |
| 1 | O `id_pedido` já apareceu antes no arquivo | `pedido duplicado` |
| 2 | A linha não tem exatamente 9 colunas | `número de colunas inválido` |
| 3 | A data está vazia | `data ausente` |
| 4 | A data não existe (ex.: `31/02/2025`, mês 13) ou não está em nenhum dos dois formatos | `data inválida` |
| 5 | A categoria está vazia | `categoria ausente` |
| 6 | A quantidade não é um número inteiro (ex.: `dois`, vazio) | `quantidade inválida` |
| 7 | A quantidade é zero ou negativa | `quantidade não positiva` |
| 8 | O preço não pode ser convertido para número, ou é ≤ 0 | `preço inválido` |

> 📌 **Linhas em branco** não são rejeitadas: são apenas **ignoradas** e contadas à parte.
> 📌 **Duplicatas:** a **primeira** ocorrência do pedido é processada normalmente. As seguintes são rejeitadas como `pedido duplicado`, mesmo que a primeira tenha sido rejeitada por outro motivo.

### C) Coluna nova

Cada venda válida ganha a coluna **`valor_total = quantidade × preco_unitario`**, arredondada em 2 casas.

## 🧭 Passo a passo sugerido

Você **não** precisa seguir exatamente esta estrutura, mas ela ajuda a organizar o raciocínio.

### Etapa 1: Extract

```python
def extrair(caminho):
    """Lê o arquivo e devolve o cabeçalho e uma lista com as demais linhas."""
```

💡 `arquivo.read().splitlines()` devolve as linhas **sem** o `\n` no final.

### Etapa 2: Transform

Crie **uma função para cada regra**. Assim fica fácil testar cada uma isoladamente:

```python
def normalizar_data(texto):          # '14/03/2025' -> '2025-03-14' | lança ValueError('data inválida')
def converter_quantidade(texto):     # '3' -> 3 | lança ValueError('quantidade inválida')
def converter_preco(texto):          # 'R$ 89,00' -> 89.0 | lança ValueError('preço inválido')
def normalizar_pagamento(texto):     # 'PIX' -> 'Pix'
def transformar_linha(linha):        # devolve um dict com a venda limpa, ou lança ValueError(motivo)
def transformar(linhas):             # devolve (validos, rejeitados, linhas_em_branco)
```

O "pulo do gato" deste projeto: **as funções de validação lançam exceções com o motivo**, e quem as chama decide o que fazer:

```python
# dentro da função de validação
raise ValueError('quantidade não positiva')

# em quem chama
try:
    venda = transformar_linha(linha)
    validos.append(venda)
except ValueError as erro:
    rejeitados.append((numero_linha, linha, str(erro)))   # str(erro) é o motivo!
```

💡 **Duplicatas:** use um `set` com os IDs já vistos. A busca com `in` em um `set` é muito rápida, como vimos no Teclado Dominante.
💡 **Datas:** para validar o dia, você precisa saber quantos dias tem cada mês. Uma `tuple` resolve: `(31, 28, 31, 30, ...)`.
💡 **Testando aos poucos:** antes de processar o arquivo todo, teste suas funções com valores soltos:

```python
print(normalizar_data('14/03/2025'))   # 2025-03-14
print(converter_preco('R$ 1.234,50'))  # pense: o que deveria acontecer aqui?
```

### Etapa 3: Load

Gere os 3 arquivos na pasta `saida/`:

**`saida/vendas_limpas.csv`**: separado por **vírgula**, com ponto decimal e a coluna nova:

```txt
id_pedido,data,cliente,cidade,categoria,produto,quantidade,preco_unitario,valor_total,forma_pagamento
PED-00001,2025-02-04,Felipe Santos,Recife,Esporte,Mochila Esportiva,2,159.00,318.00,Cartão de Crédito
PED-00002,2025-01-27,Carla Oliveira,Petrolina,Papelaria,Caderno Inteligente,3,89.00,267.00,Cartão de Crédito
PED-00004,2025-01-19,Isabela Costa,Recife,Esporte,Tênis de Corrida,3,349.90,1049.70,Cartão de Crédito
```

**`saida/rejeitados.csv`**: número da linha no arquivo original, motivo e a linha original sem alterações. Assim alguém consegue ir lá corrigir na fonte:

```txt
linha_arquivo;motivo;conteudo_original
4;quantidade inválida;PED-00003;2025-06-30;Otávio Santos;CARUARU;Esporte;Tênis de Corrida;dois;349.90;pix
21;pedido duplicado;PED-00010;2025-01-10;Diego Costa;Caruaru;Casa;Cafeteira;4;189.90;PIX
41;categoria ausente;PED-00038;02/03/2025;Rafael Ferreira;Recife;;Kit Canetas;2;R$ 34,90;boleto
```

> A linha 1 do arquivo é o cabeçalho, então o primeiro pedido está na linha 2.

**`saida/relatorio_etl.txt`**: o relatório abaixo. Ele também deve ser **impresso no terminal**.

## 🖥️ Exemplo de saída esperada

Use estes números para **conferir** o seu resultado. Se algo não bater, volte às regras de negócio.

```txt
====================================================
RELATÓRIO DO PIPELINE ETL - VENDAS 1º SEMESTRE/2025
====================================================

>> QUALIDADE DOS DADOS
  Linhas lidas (sem cabeçalho): 1239
  Linhas em branco ignoradas:   4
  Registros válidos:            1130
  Registros rejeitados:         105
  Taxa de aproveitamento:       91.5%

  Rejeições por motivo:
    - pedido duplicado                35
    - quantidade inválida             14
    - quantidade não positiva         14
    - preço inválido                  14
    - categoria ausente                7
    - data ausente                     7
    - número de colunas inválido       7
    - data inválida                    7

>> INDICADORES DE NEGÓCIO
  Faturamento total: R$ 276.681,70
  Pedidos válidos:   1130
  Ticket médio:      R$ 244,85
  Produto campeão (unidades): Storytelling com Dados (146 un.)

  Faturamento por categoria:
  Eletrônicos            R$ 110.756,30  ( 40.0%)
  Esporte                 R$ 67.767,90  ( 24.5%)
  Livros                  R$ 42.919,60  ( 15.5%)
  Casa                    R$ 40.450,20  ( 14.6%)
  Papelaria               R$ 14.787,70  (  5.3%)

  Faturamento por cidade:
  Recife                 R$ 112.256,70  ( 40.6%)
  Olinda                  R$ 48.887,10  ( 17.7%)
  Caruaru                 R$ 36.860,90  ( 13.3%)
  Petrolina               R$ 30.450,60  ( 11.0%)
  Paulista                R$ 25.922,00  (  9.4%)
  Garanhuns               R$ 22.304,40  (  8.1%)

  Faturamento por forma de pagamento:
  Pix                    R$ 119.527,10  ( 43.2%)
  Cartão de Crédito       R$ 99.657,10  ( 36.0%)
  Cartão de Débito        R$ 34.558,20  ( 12.5%)
  Boleto                  R$ 22.939,30  (  8.3%)

  Faturamento por mês:
  Jan   R$ 41.296,30 ███████████████████
  Fev   R$ 31.478,60 ██████████████
  Mar   R$ 38.963,40 ██████████████████
  Abr   R$ 43.851,20 ████████████████████
  Mai   R$ 55.959,50 ██████████████████████████
  Jun   R$ 65.132,70 ██████████████████████████████
```

### Como fazer algumas partes do relatório

**Taxa de aproveitamento** = válidos ÷ (linhas lidas − linhas em branco) × 100.

**Agrupar valores** (por categoria, cidade...) é o mesmo padrão de contagem do PyVotação, usando dicionário:

```python
faturamento = {}
for venda in vendas:
    categoria = venda['categoria']
    faturamento[categoria] = faturamento.get(categoria, 0) + venda['valor_total']
```

> 🧠 Repare que você vai repetir esse padrão para categoria, cidade e forma de pagamento. Que tal uma **função** `somar_por(vendas, campo)`?

**Formatar em reais** (`R$ 1.234,56`): o Python formata no padrão americano (`1,234.56`). Um truque é trocar os separadores:

```python
texto = f'{valor:,.2f}'                                   # '276,681.70'
texto = texto.replace(',', '_').replace('.', ',').replace('_', '.')  # '276.681,70'
```

**Gráfico de barras no terminal:** a barra do maior mês tem 30 caracteres e as outras são proporcionais:

```python
barra = '█' * round(valor_do_mes / maior_valor * 30)
```

## ✅ Checklist de entrega

- [ ] O programa roda com `python main.py` a partir da pasta do projeto
- [ ] Os 3 arquivos são gerados em `saida/`
- [ ] Os números do relatório batem com o exemplo acima
- [ ] Existe pelo menos uma função para cada regra de validação
- [ ] Se `dados/vendas_brutas.csv` não existir, o programa mostra uma mensagem amigável (sem *traceback*)
- [ ] README do repositório com contexto, como rodar, exemplo de saída e descobertas

## 🏆 Desafios bônus

1. **Relatório de correções:** além dos rejeitados, conte quantas correções de cada tipo foram feitas (ex.: "312 datas convertidas de DD/MM/AAAA", "180 cidades padronizadas"). Mostrar o que foi **consertado** dá confiança em um pipeline.
2. **Preço de milhar:** o que acontece com `converter_preco('R$ 1.234,50')`? Ajuste a função para tratar esse caso corretamente.
3. **Pipeline reutilizável:** faça o programa perguntar o caminho do arquivo de entrada (com `input`) e continuar pedindo até receber um arquivo que exista.
4. **Clientes recorrentes:** usando um `dict` de `set`s, descubra quais clientes compraram em **3 ou mais meses diferentes**.
5. **Com `collections`:** refaça as contagens com `Counter` ou `defaultdict` e compare a legibilidade.

## 💼 Para o seu portfólio

Uma frase de exemplo para o README e o LinkedIn:

> *"Construí um pipeline ETL em Python puro que processa 1.200+ registros de vendas, padroniza 5 tipos de inconsistência, identifica 8 categorias de erro com rastreabilidade linha a linha e gera indicadores de faturamento por categoria, cidade, pagamento e mês."*

Na seção **Descobertas** do README, responda: *qual foi o problema de qualidade mais frequente? Se você fosse conversar com o time do sistema de vendas, o que pediria para mudarem na origem?*
