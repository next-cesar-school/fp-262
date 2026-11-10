# NExT 26.2 | Fundamentos de Python Aplicado a Dados

![CESAR School](/cesar_school.png)

## 🚀 Semana de Projetos

Até aqui vocês já aprenderam muita coisa: variáveis, condicionais, listas, `while`, `for`, funções, arquivos, tratamento de exceções, `tuple`, `set` e `dict`. Nos mini projetos (💸 PyFinanceiro, 🗳️ PyVotação e ⌨️ Teclado Dominante) e no exercício de "dados sujos" da Aula 07, vocês já fizeram **pedaços** do trabalho de quem trabalha com dados.

Nesta semana, a proposta é juntar esses pedaços em **3 projetos completos**, parecidos com o que se faz no dia a dia da área e pensados para entrar no **portfólio** de vocês.

| # | Projeto | Área | O que você vai construir |
| - | ------- | ---- | ------------------------ |
| 1 | [🛠️ PyPipeline: ETL de Vendas](/semana-projeto/projeto01-pipeline-etl-vendas/) | Engenharia de Dados | Um pipeline que **extrai** um CSV sujo, **transforma** (valida, corrige, remove duplicatas) e **carrega** arquivos limpos com um relatório de qualidade |
| 2 | [📊 Raio-X Salarial da Área de Dados](/semana-projeto/projeto02-raio-x-salarial/) | Análise / Ciência de Dados | Uma **análise exploratória (EDA)** com estatística feita à mão (média, mediana, desvio padrão, correlação) e gráficos no terminal |
| 3 | [🌡️ Termômetro de Avaliações](/semana-projeto/projeto03-termometro-avaliacoes/) | Ciência de Dados / NLP | Um **classificador de sentimento** de comentários de clientes, avaliado com acurácia e matriz de confusão |

---

## 🧰 Regras do jogo

1. **Python puro.** Nada de `pandas`, `numpy`, `csv` ou `statistics`: a ideia é **construir as ferramentas com as próprias mãos** e entender o que elas fazem por dentro. Nas próximas aulas (Módulos e NumPy) você vai poder comparar seu código com essas bibliotecas e refatorar com o uso dessas ferramentas.
   - ✅ Pode: tudo o que vimos até a Aula 08, mais `sorted(..., key=lambda ...)`, que apareceu no PyVotação.
   - 🟡 Pode, nos **bônus**: `collections` (`Counter`, `defaultdict`), apresentado como bônus na Aula 08.
2. **Use funções.** Cada etapa do problema deve ser uma função com um nome que diga o que ela faz. Evite um "script corrido" de 200 linhas;
3. **Trate os erros.** Arquivo que não existe, valor que não converte e entrada inválida do usuário **não podem** derrubar o programa;
4. **Leia os arquivos com `with open(...)`** e sempre informe `encoding='utf-8'`;

## 📁 Estrutura sugerida para cada repositório

```txt
nome-do-projeto/
├── dados/            # arquivos de entrada (fornecidos)
├── saida/            # arquivos gerados pelo seu programa
├── main.py           # ponto de entrada do programa
└── README.md         # a documentação e apresentação do seu projeto
```

> ⚠️ Crie a pasta `saida/` **antes** de rodar o programa. Se ela não existir, `open('saida/arquivo.txt', 'w')` lança `FileNotFoundError`.

## 🌟 Como transformar o projeto em portfólio

Recrutadores raramente rodam o seu código, mas **sempre leem o README**. Para cada projeto, o seu README deve ter:

1. **Título e uma frase** dizendo o problema que o projeto resolve;
2. **Contexto**: quem usaria isso e por quê;
3. **Como rodar**, com os comandos;
4. **Exemplo de saída**: cole um trecho do relatório gerado;
5. **Principais descobertas / decisões**: o que os dados mostraram, ou que regras você criou para tratar os problemas;
6. **Tecnologias e conceitos**: Python, ETL, EDA, NLP, tratamento de exceções...;
7. **Próximos passos**: o que você melhoraria com mais tempo, por exemplo "refazer com pandas".
