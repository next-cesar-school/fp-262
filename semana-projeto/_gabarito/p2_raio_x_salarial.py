"""
GABARITO - Projeto 2: Raio-X Salarial da Área de Dados (EDA)
Uso (dentro da pasta projeto02-raio-x-salarial):  python ../_gabarito_professor/p2_raio_x_salarial.py
Usa apenas o que foi visto até a Aula 08 (sem import).
"""

ARQUIVO = 'dados/pesquisa_salarial.csv'
LIMITE_OUTLIER = 60000  # salários mensais acima disso são tratados como erro de digitação
ORDEM_NIVEIS = ('Júnior', 'Pleno', 'Sênior', 'Especialista')
ORDEM_MODELOS = ('Remoto', 'Híbrido', 'Presencial')


# ---------------------------------------------------------- estatística "na mão"
def media(valores):
    return sum(valores) / len(valores)


def mediana(valores):
    ordenados = sorted(valores)
    n = len(ordenados)
    meio = n // 2
    if n % 2 == 1:
        return ordenados[meio]
    return (ordenados[meio - 1] + ordenados[meio]) / 2


def desvio_padrao(valores):
    m = media(valores)
    soma = 0
    for v in valores:
        soma += (v - m) ** 2
    return (soma / (len(valores) - 1)) ** 0.5  # desvio padrão amostral


def correlacao(xs, ys):
    """Coeficiente de correlação de Pearson."""
    mx, my = media(xs), media(ys)
    cov = sx = sy = 0
    for x, y in zip(xs, ys):
        cov += (x - mx) * (y - my)
        sx += (x - mx) ** 2
        sy += (y - my) ** 2
    return cov / (sx ** 0.5 * sy ** 0.5)


def resumo(valores):
    return {'n': len(valores), 'media': media(valores), 'mediana': mediana(valores),
            'min': min(valores), 'max': max(valores), 'dp': desvio_padrao(valores)}


# ------------------------------------------------------------------ leitura
def carregar(caminho):
    respostas, invalidas, outliers = [], [], []
    with open(caminho, encoding='utf-8') as arquivo:
        arquivo.readline()  # cabeçalho
        for linha in arquivo:
            campos = linha.strip().split(',')
            try:
                salario = float(campos[6])
            except ValueError:
                invalidas.append(campos[0])
                continue
            if salario > LIMITE_OUTLIER:
                outliers.append((campos[0], salario))
                continue
            try:
                anos = int(campos[3])
            except ValueError:
                anos = None  # sem experiência informada: entra nas análises, menos na correlação
            respostas.append({'id': campos[0], 'cargo': campos[1], 'nivel': campos[2], 'anos': anos,
                              'uf': campos[4], 'modelo': campos[5], 'salario': salario})
    return respostas, invalidas, outliers


def agrupar(respostas, campo):
    grupos = {}
    for r in respostas:
        grupos.setdefault(r[campo], []).append(r['salario'])
    return grupos


# ----------------------------------------------------------------- saída
def reais(valor):
    return 'R$ ' + f'{valor:,.0f}'.replace(',', '.')


def tabela(titulo, grupos, ordem=None):
    chaves = ordem if ordem else sorted(grupos, key=lambda c: mediana(grupos[c]), reverse=True)
    linhas = [titulo, f"  {'Grupo':<36}{'N':>4}{'Média':>12}{'Mediana':>12}{'Mín':>12}{'Máx':>12}",
              '  ' + '-' * 86]
    for chave in chaves:
        s = resumo(grupos[chave])
        linhas.append(f"  {chave:<36}{s['n']:>4}{reais(s['media']):>12}{reais(s['mediana']):>12}"
                      f"{reais(s['min']):>12}{reais(s['max']):>12}")
    return linhas


def grafico_barras(titulo, rotulos_valores, largura=40):
    maior = max(v for _, v in rotulos_valores)
    linhas = [titulo]
    for rotulo, valor in rotulos_valores:
        barra = '█' * round(valor / maior * largura)
        linhas.append(f'  {rotulo:<36}{barra} {reais(valor)}')
    return linhas


def histograma(salarios, faixa=3000):
    contagem = {}
    for s in salarios:
        inicio = int(s // faixa) * faixa
        contagem[inicio] = contagem.get(inicio, 0) + 1
    maior = max(contagem.values())
    linhas = ['>> DISTRIBUIÇÃO DOS SALÁRIOS (faixas de R$ 3.000)']
    for inicio in range(0, max(contagem) + faixa, faixa):
        qtd = contagem.get(inicio, 0)
        rotulo = f'{reais(inicio)} a {reais(inicio + faixa - 1)}'
        linhas.append(f"  {rotulo:<22}{'▇' * round(qtd / maior * 40)} {qtd}")
    return linhas


def main():
    try:
        respostas, invalidas, outliers = carregar(ARQUIVO)
    except FileNotFoundError:
        print(f'ERRO: não encontrei {ARQUIVO}')
        return

    salarios = [r['salario'] for r in respostas]
    geral = resumo(salarios)
    por_cargo = agrupar(respostas, 'cargo')
    por_nivel = agrupar(respostas, 'nivel')
    por_modelo = agrupar(respostas, 'modelo')
    por_uf = agrupar(respostas, 'uf')

    com_anos = [r for r in respostas if r['anos'] is not None]
    rho = correlacao([r['anos'] for r in com_anos], [r['salario'] for r in com_anos])

    top_ufs = sorted(por_uf, key=lambda uf: mediana(por_uf[uf]), reverse=True)

    junior = mediana(por_nivel['Júnior'])
    senior = mediana(por_nivel['Sênior'])

    r = ['=' * 60, 'RAIO-X SALARIAL DA ÁREA DE DADOS - PESQUISA 2025', '=' * 60, '',
         '>> SOBRE OS DADOS',
         f'  Respostas válidas:              {len(respostas)}',
         f'  Sem salário informado:          {len(invalidas)}',
         f'  Outliers removidos (> {reais(LIMITE_OUTLIER)}): {len(outliers)} -> ids {", ".join(i for i, _ in outliers)}',
         f'  Cargos distintos:               {len(por_cargo)}',
         f'  Estados (UF) representados:     {len(por_uf)}', '',
         '>> PANORAMA GERAL',
         f"  Média:          {reais(geral['media'])}",
         f"  Mediana:        {reais(geral['mediana'])}",
         f"  Desvio padrão:  {reais(geral['dp'])}",
         f"  Menor salário:  {reais(geral['min'])}",
         f"  Maior salário:  {reais(geral['max'])}", '']
    r += tabela('>> SALÁRIO POR CARGO (ordenado pela mediana)', por_cargo) + ['']
    r += tabela('>> SALÁRIO POR NÍVEL', por_nivel, ORDEM_NIVEIS) + ['']
    r += tabela('>> SALÁRIO POR MODELO DE TRABALHO', por_modelo, ORDEM_MODELOS) + ['']
    r += grafico_barras('>> MEDIANA POR CARGO',
                        [(c, mediana(por_cargo[c])) for c in sorted(por_cargo, key=lambda c: mediana(por_cargo[c]),
                                                                     reverse=True)]) + ['']
    r += ['>> TOP 5 ESTADOS (mediana salarial)']
    for pos, uf in enumerate(top_ufs[:5], start=1):
        r.append(f'  {pos}º {uf}  {reais(mediana(por_uf[uf])):>10}  ({len(por_uf[uf])} respostas)')
    pe_pos = top_ufs.index('PE') + 1
    r.append(f'  ... PE aparece em {pe_pos}º lugar, com mediana de {reais(mediana(por_uf["PE"]))}')
    r += [''] + histograma(salarios) + ['']
    r += ['>> INSIGHTS AUTOMÁTICOS',
          f'  - Um(a) Sênior ganha, na mediana, {senior / junior:.1f}x o salário de um(a) Júnior.',
          f'  - Correlação entre anos de experiência e salário: {rho:.2f} '
          f'({"forte" if rho >= 0.7 else "moderada" if rho >= 0.4 else "fraca"}).',
          f'  - Remoto x Presencial (mediana): {reais(mediana(por_modelo["Remoto"]))} x '
          f'{reais(mediana(por_modelo["Presencial"]))}.']
    relatorio = '\n'.join(r)
    print(relatorio)

    with open('saida/relatorio_salarial.txt', 'w', encoding='utf-8') as arq:
        arq.write(relatorio + '\n')
    with open('saida/resumo_por_cargo.csv', 'w', encoding='utf-8') as arq:
        arq.write('cargo,n,media,mediana,minimo,maximo,desvio_padrao\n')
        for cargo in sorted(por_cargo):
            s = resumo(por_cargo[cargo])
            arq.write(f"{cargo},{s['n']},{s['media']:.2f},{s['mediana']:.2f},{s['min']:.2f},"
                      f"{s['max']:.2f},{s['dp']:.2f}\n")


main()
