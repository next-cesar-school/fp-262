"""
GABARITO - Projeto 1: PyPipeline (ETL de vendas)
Uso (dentro da pasta projeto01-pipeline-etl-vendas):  python ../_gabarito_professor/p1_pipeline_vendas.py
Usa apenas o que foi visto até a Aula 08 (sem import).
"""

ARQUIVO_ENTRADA = 'dados/vendas_brutas.csv'
ARQUIVO_LIMPO = 'saida/vendas_limpas.csv'
ARQUIVO_REJEITADOS = 'saida/rejeitados.csv'
ARQUIVO_RELATORIO = 'saida/relatorio_etl.txt'

NUM_COLUNAS = 9
PAGAMENTOS = {
    'pix': 'Pix',
    'cartão de crédito': 'Cartão de Crédito',
    'cartao de credito': 'Cartão de Crédito',
    'cartão de débito': 'Cartão de Débito',
    'cartao de debito': 'Cartão de Débito',
    'boleto': 'Boleto',
}
NOMES_MESES = ('Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez')


# ------------------------------------------------------------------ EXTRACT
def extrair(caminho):
    """Lê o arquivo e devolve (cabecalho, lista de linhas sem o \\n)."""
    with open(caminho, encoding='utf-8') as arquivo:
        linhas = arquivo.read().splitlines()
    return linhas[0], linhas[1:]


# ---------------------------------------------------------------- TRANSFORM
def eh_bissexto(ano):
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)


def normalizar_data(texto):
    """Aceita AAAA-MM-DD ou DD/MM/AAAA e devolve AAAA-MM-DD. Lança ValueError se inválida."""
    texto = texto.strip()
    if texto == '':
        raise ValueError('data ausente')
    try:
        if '/' in texto:
            dia, mes, ano = texto.split('/')
        else:
            ano, mes, dia = texto.split('-')
        dia, mes, ano = int(dia), int(mes), int(ano)
    except ValueError:
        raise ValueError('data inválida')

    dias_no_mes = [31, 29 if eh_bissexto(ano) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if not 1 <= mes <= 12 or not 1 <= dia <= dias_no_mes[mes - 1]:
        raise ValueError('data inválida')
    return f'{ano:04d}-{mes:02d}-{dia:02d}'


def converter_quantidade(texto):
    try:
        qtd = int(texto.strip())
    except ValueError:
        raise ValueError('quantidade inválida')
    if qtd <= 0:
        raise ValueError('quantidade não positiva')
    return qtd


def converter_preco(texto):
    texto = texto.replace('R$', '').strip().replace(',', '.')
    try:
        preco = float(texto)
    except ValueError:
        raise ValueError('preço inválido')
    if preco <= 0:
        raise ValueError('preço inválido')
    return preco


def normalizar_pagamento(texto):
    chave = texto.strip().lower()
    if chave not in PAGAMENTOS:
        raise ValueError('forma de pagamento desconhecida')
    return PAGAMENTOS[chave]


def transformar_linha(linha):
    """Recebe uma linha bruta e devolve um dicionário limpo. Lança ValueError com o motivo."""
    campos = linha.split(';')
    if len(campos) != NUM_COLUNAS:
        raise ValueError('número de colunas inválido')
    id_pedido, data, cliente, cidade, categoria, produto, qtd, preco, pagamento = campos

    data = normalizar_data(data)
    categoria = categoria.strip().capitalize()
    if categoria == '':
        raise ValueError('categoria ausente')
    qtd = converter_quantidade(qtd)
    preco = converter_preco(preco)

    return {
        'id_pedido': id_pedido.strip(),
        'data': data,
        'cliente': cliente.strip(),
        'cidade': cidade.strip().title(),
        'categoria': categoria,
        'produto': produto.strip(),
        'quantidade': qtd,
        'preco_unitario': preco,
        'valor_total': round(qtd * preco, 2),
        'forma_pagamento': normalizar_pagamento(pagamento),
    }


def transformar(linhas):
    validos, rejeitados = [], []
    ids_vistos = set()
    em_branco = 0
    for numero, linha in enumerate(linhas, start=2):  # linha 1 é o cabeçalho
        if linha.strip() == '':
            em_branco += 1
            continue
        id_pedido = linha.split(';')[0].strip()
        if id_pedido in ids_vistos:
            rejeitados.append((numero, linha, 'pedido duplicado'))
            continue
        ids_vistos.add(id_pedido)
        try:
            validos.append(transformar_linha(linha))
        except ValueError as erro:
            rejeitados.append((numero, linha, str(erro)))
    return validos, rejeitados, em_branco


# --------------------------------------------------------------------- LOAD
def carregar_limpos(caminho, vendas):
    colunas = ['id_pedido', 'data', 'cliente', 'cidade', 'categoria', 'produto',
               'quantidade', 'preco_unitario', 'valor_total', 'forma_pagamento']
    with open(caminho, 'w', encoding='utf-8') as arquivo:
        arquivo.write(','.join(colunas) + '\n')
        for v in vendas:
            arquivo.write(f"{v['id_pedido']},{v['data']},{v['cliente']},{v['cidade']},{v['categoria']},"
                          f"{v['produto']},{v['quantidade']},{v['preco_unitario']:.2f},{v['valor_total']:.2f},"
                          f"{v['forma_pagamento']}\n")


def carregar_rejeitados(caminho, rejeitados):
    with open(caminho, 'w', encoding='utf-8') as arquivo:
        arquivo.write('linha_arquivo;motivo;conteudo_original\n')
        for numero, linha, motivo in rejeitados:
            arquivo.write(f'{numero};{motivo};{linha}\n')


# ----------------------------------------------------------------- ANÁLISE
def somar_por(vendas, campo):
    totais = {}
    for v in vendas:
        totais[v[campo]] = totais.get(v[campo], 0) + v['valor_total']
    return totais


def reais(valor):
    texto = f'{valor:,.2f}'
    return 'R$ ' + texto.replace(',', '_').replace('.', ',').replace('_', '.')


def bloco_ranking(titulo, totais, total_geral):
    linhas = [titulo]
    for chave, valor in sorted(totais.items(), key=lambda item: item[1], reverse=True):
        linhas.append(f'  {chave:<20}{reais(valor):>16}  ({valor / total_geral * 100:5.1f}%)')
    return linhas


def montar_relatorio(total_lidas, vendas, rejeitados, em_branco):
    motivos = {}
    for _, _, motivo in rejeitados:
        motivos[motivo] = motivos.get(motivo, 0) + 1

    total = sum(v['valor_total'] for v in vendas)
    por_mes = {}
    for v in vendas:
        mes = NOMES_MESES[int(v['data'][5:7]) - 1]
        por_mes[mes] = por_mes.get(mes, 0) + v['valor_total']
    unidades = {}
    for v in vendas:
        unidades[v['produto']] = unidades.get(v['produto'], 0) + v['quantidade']
    campeao = max(unidades.items(), key=lambda item: item[1])

    r = ['=' * 52, 'RELATÓRIO DO PIPELINE ETL - VENDAS 1º SEMESTRE/2025', '=' * 52, '',
         '>> QUALIDADE DOS DADOS',
         f'  Linhas lidas (sem cabeçalho): {total_lidas}',
         f'  Linhas em branco ignoradas:   {em_branco}',
         f'  Registros válidos:            {len(vendas)}',
         f'  Registros rejeitados:         {len(rejeitados)}',
         f'  Taxa de aproveitamento:       {len(vendas) / (total_lidas - em_branco) * 100:.1f}%',
         '', '  Rejeições por motivo:']
    for motivo, qtd in sorted(motivos.items(), key=lambda item: item[1], reverse=True):
        r.append(f'    - {motivo:<30}{qtd:>4}')
    r += ['', '>> INDICADORES DE NEGÓCIO',
          f'  Faturamento total: {reais(total)}',
          f'  Pedidos válidos:   {len(vendas)}',
          f'  Ticket médio:      {reais(total / len(vendas))}',
          f'  Produto campeão (unidades): {campeao[0]} ({campeao[1]} un.)', '']
    r += bloco_ranking('  Faturamento por categoria:', somar_por(vendas, 'categoria'), total) + ['']
    r += bloco_ranking('  Faturamento por cidade:', somar_por(vendas, 'cidade'), total) + ['']
    r += bloco_ranking('  Faturamento por forma de pagamento:', somar_por(vendas, 'forma_pagamento'), total) + ['']
    r.append('  Faturamento por mês:')
    maior = max(por_mes.values())
    for mes in NOMES_MESES:
        if mes in por_mes:
            barra = '█' * round(por_mes[mes] / maior * 30)
            r.append(f'  {mes} {reais(por_mes[mes]):>14} {barra}')
    return '\n'.join(r)


def main():
    try:
        cabecalho, linhas = extrair(ARQUIVO_ENTRADA)
    except FileNotFoundError:
        print(f'ERRO: arquivo {ARQUIVO_ENTRADA} não encontrado. Verifique a pasta dados/.')
        return
    vendas, rejeitados, em_branco = transformar(linhas)
    try:
        carregar_limpos(ARQUIVO_LIMPO, vendas)
        carregar_rejeitados(ARQUIVO_REJEITADOS, rejeitados)
        relatorio = montar_relatorio(len(linhas), vendas, rejeitados, em_branco)
        with open(ARQUIVO_RELATORIO, 'w', encoding='utf-8') as arquivo:
            arquivo.write(relatorio + '\n')
    except FileNotFoundError:
        print('ERRO: crie a pasta saida/ antes de rodar o pipeline.')
        return
    print(relatorio)


main()
