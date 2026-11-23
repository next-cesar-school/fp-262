# 🔒 Gabarito (uso do professor, não publicar para a turma)

Esta pasta contém as soluções de referência e o gerador dos dados. **Não suba esta pasta** para o repositório público dos estudantes.

| Arquivo | Para que serve |
| ------- | -------------- |
| `gerar_dados.py` | Gera todos os arquivos de `dados/` dos 3 projetos. A semente é fixa (`random.seed(2622)`), então os arquivos são sempre idênticos |
| `p1_pipeline_vendas.py` | Solução do Projeto 1 |
| `p2_raio_x_salarial.py` | Solução do Projeto 2 |
| `p3_termometro.py` | Solução do Projeto 3 |
| `saidas/` | Arquivos gerados pelas soluções. Os exemplos dos enunciados foram copiados daqui |

## Como rodar

Cada solução deve ser executada **de dentro da pasta do projeto** e precisa de uma pasta `saida/`:

```bash
cd projeto01-pipeline-etl-vendas
mkdir saida
python ../_gabarito_professor/p1_pipeline_vendas.py
```

## Observações

- As soluções usam só o que foi visto até a Aula 08, com três pequenas exceções que vale comentar em sala se aparecerem: `enumerate`, `zip` e `dict.setdefault`.
- **Projeto 1:** os 70 registros com defeito grave foram distribuídos igualmente entre 10 tipos de defeito (7 de cada). Os tipos "quantidade vazia" e "quantidade em texto" caem no mesmo motivo (`quantidade inválida`, 14), e "preço em texto" e "preço vazio" também (`preço inválido`, 14). São 35 duplicatas exatas e 4 linhas em branco.
- **Projeto 2:** os outliers são os ids 57 e 402 (salário anual digitado como mensal).
- **Projeto 3:** os comentários foram montados a partir de frases-modelo, com cerca de 10% de casos difíceis (negação, ironia, "mas") inseridos de propósito, para que a análise de erros tenha material.
- Se quiser uma turma com dados diferentes (por exemplo, para evitar cópia entre turmas), mude a semente em `gerar_dados.py`, rode o gerador e as 3 soluções, e atualize os exemplos de saída nos enunciados.
