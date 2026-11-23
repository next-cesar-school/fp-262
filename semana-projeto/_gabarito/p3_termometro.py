"""
GABARITO - Projeto 3: Termômetro de Avaliações (análise de sentimento com léxico)
Uso (dentro da pasta projeto03-termometro-avaliacoes):  python ../_gabarito_professor/p3_termometro.py
Usa apenas o que foi visto até a Aula 08 (sem import).
"""

CLASSES = ('positivo', 'neutro', 'negativo')
NEGADORES = {'não', 'nem', 'nada', 'nunca'}


def carregar_palavras(caminho):
    with open(caminho, encoding='utf-8') as arquivo:
        return {linha.strip() for linha in arquivo if linha.strip()}


def limpar_texto(texto):
    """Minúsculas + troca tudo que não for letra por espaço. Devolve lista de palavras."""
    limpo = ''
    for caractere in texto.lower():
        limpo += caractere if caractere.isalpha() else ' '
    return limpo.split()


def pontuar(palavras, positivas, negativas, tratar_negacao=False):
    pontos = 0
    for i, palavra in enumerate(palavras):
        valor = 0
        if palavra in positivas:
            valor = 1
        elif palavra in negativas:
            valor = -1
        if tratar_negacao and i > 0 and palavras[i - 1] in NEGADORES:
            valor = -valor
        pontos += valor
    return pontos


def classificar(pontos):
    if pontos > 0:
        return 'positivo'
    if pontos < 0:
        return 'negativo'
    return 'neutro'


def sentimento_da_nota(nota):
    if nota >= 4:
        return 'positivo'
    if nota == 3:
        return 'neutro'
    return 'negativo'


def carregar_avaliacoes(caminho):
    avaliacoes, invalidas = [], []
    with open(caminho, encoding='utf-8') as arquivo:
        arquivo.readline()
        for linha in arquivo:
            id_, produto, nota, comentario = linha.rstrip('\n').split(',', 3)
            try:
                nota = int(nota)
                if not 1 <= nota <= 5:
                    raise ValueError
            except ValueError:
                invalidas.append(id_)
                continue
            avaliacoes.append({'id': id_, 'produto': produto, 'nota': nota, 'comentario': comentario,
                               'palavras': limpar_texto(comentario)})
    return avaliacoes, invalidas


def avaliar(avaliacoes, positivas, negativas, tratar_negacao):
    matriz = {real: {prev: 0 for prev in CLASSES} for real in CLASSES}
    acertos = 0
    for a in avaliacoes:
        a['pontos'] = pontuar(a['palavras'], positivas, negativas, tratar_negacao)
        a['previsto'] = classificar(a['pontos'])
        a['real'] = sentimento_da_nota(a['nota'])
        matriz[a['real']][a['previsto']] += 1
        if a['previsto'] == a['real']:
            acertos += 1
    return acertos / len(avaliacoes), matriz


def top_palavras(avaliacoes, classe, stopwords, positivas, negativas, n=8):
    contagem = {}
    for a in avaliacoes:
        if a['real'] != classe:
            continue
        for p in a['palavras']:
            if p not in stopwords and len(p) > 2:
                contagem[p] = contagem.get(p, 0) + 1
    ranking = sorted(contagem.items(), key=lambda item: item[1], reverse=True)[:n]
    saida = []
    for palavra, qtd in ranking:
        marca = '(+)' if palavra in positivas else '(-)' if palavra in negativas else '   '
        saida.append(f'{palavra} {marca} {qtd}')
    return saida


def main():
    positivas = carregar_palavras('dados/lexico_positivo.txt')
    negativas = carregar_palavras('dados/lexico_negativo.txt')
    stopwords = carregar_palavras('dados/stopwords.txt')
    avaliacoes, invalidas = carregar_avaliacoes('dados/avaliacoes.csv')

    acc_simples, _ = avaliar(avaliacoes, positivas, negativas, tratar_negacao=False)
    acc, matriz = avaliar(avaliacoes, positivas, negativas, tratar_negacao=True)

    r = ['=' * 58, 'TERMÔMETRO DE AVALIAÇÕES - LOJA NExT', '=' * 58, '',
         f'Avaliações analisadas: {len(avaliacoes)}  |  descartadas (nota inválida): {len(invalidas)}',
         f'Léxico: {len(positivas)} palavras positivas, {len(negativas)} negativas, {len(stopwords)} stopwords', '',
         '>> DESEMPENHO DO CLASSIFICADOR (comparado com a nota)',
         f'  Acurácia sem tratar negação: {acc_simples * 100:.1f}%',
         f'  Acurácia COM negação:        {acc * 100:.1f}%', '',
         '  Matriz de confusão (linhas = real pela nota | colunas = previsto pelo texto)',
         f"  {'':<12}{'positivo':>10}{'neutro':>10}{'negativo':>10}"]
    for real in CLASSES:
        r.append(f'  {real:<12}' + ''.join(f'{matriz[real][prev]:>10}' for prev in CLASSES))

    r += ['', '>> RANKING DE PRODUTOS (% de comentários positivos)']
    por_produto = {}
    for a in avaliacoes:
        por_produto.setdefault(a['produto'], []).append(a)
    linhas_produto = []
    for produto, lista in por_produto.items():
        pos = sum(1 for a in lista if a['previsto'] == 'positivo')
        neg = sum(1 for a in lista if a['previsto'] == 'negativo')
        nota_media = sum(a['nota'] for a in lista) / len(lista)
        linhas_produto.append((produto, pos / len(lista) * 100, neg / len(lista) * 100, nota_media, len(lista)))
    linhas_produto.sort(key=lambda item: item[1], reverse=True)
    r.append(f"  {'Produto':<22}{'Positivos':>10}{'Negativos':>11}{'Nota média':>12}{'N':>5}  Termômetro")
    for produto, p_pos, p_neg, nota_media, n in linhas_produto:
        termometro = '🟩' * round(p_pos / 10) + '🟥' * round(p_neg / 10)
        r.append(f'  {produto:<22}{p_pos:>9.1f}%{p_neg:>10.1f}%{nota_media:>12.2f}{n:>5}  {termometro}')

    r += ['', '>> PALAVRAS MAIS FREQUENTES (sem stopwords)',
          '  Em avaliações positivas: ' + ', '.join(top_palavras(avaliacoes, 'positivo', stopwords, positivas, negativas)),
          '  Em avaliações negativas: ' + ', '.join(top_palavras(avaliacoes, 'negativo', stopwords, positivas, negativas))]

    erros = [a for a in avaliacoes if a['previsto'] != a['real']]
    r += ['', '>> EXEMPLOS DE ERROS DO CLASSIFICADOR (para investigar)']
    for a in erros[:4]:
        r.append(f"  [nota {a['nota']} | previsto {a['previsto']}] {a['comentario']}")

    relatorio = '\n'.join(r)
    print(relatorio)
    with open('saida/relatorio_sentimento.txt', 'w', encoding='utf-8') as arq:
        arq.write(relatorio + '\n')
    with open('saida/avaliacoes_classificadas.csv', 'w', encoding='utf-8') as arq:
        arq.write('id;produto;nota;sentimento_real;pontuacao;sentimento_previsto;acertou;comentario\n')
        for a in avaliacoes:
            arq.write(f"{a['id']};{a['produto']};{a['nota']};{a['real']};{a['pontos']};{a['previsto']};"
                      f"{'sim' if a['previsto'] == a['real'] else 'não'};{a['comentario']}\n")

    # modo interativo
    print('\nModo interativo - digite um comentário (ou "sair"):')
    while True:
        try:
            texto = input('> ')
        except (EOFError, KeyboardInterrupt):
            break
        if texto.strip().lower() == 'sair':
            break
        pts = pontuar(limpar_texto(texto), positivas, negativas, tratar_negacao=True)
        print(f'  Pontuação: {pts:+d} -> {classificar(pts).upper()}')
    print('Até mais!')


main()
