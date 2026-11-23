"""
Gera os conjuntos de dados (fictícios) dos 3 projetos.
Uso (a partir da pasta projetos-semana):  python _gabarito_professor/gerar_dados.py
A semente é fixa: rodar de novo produz exatamente os mesmos arquivos.
"""
import random
import os

random.seed(2622)
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def salvar(caminho_relativo, linhas):
    caminho = os.path.join(BASE, caminho_relativo)
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with open(caminho, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(linhas) + '\n')
    print(f'{caminho_relativo}: {len(linhas)} linhas')


# ---------------------------------------------------------------------------
# PROJETO 1 - vendas_brutas.csv (dados sujos)
# ---------------------------------------------------------------------------
def gerar_vendas():
    catalogo = {
        'Eletrônicos': [('Fone Bluetooth', 129.90), ('Carregador Turbo', 59.90), ('Smartwatch', 399.00),
                        ('Caixa de Som', 249.90), ('Mouse sem Fio', 89.90)],
        'Livros': [('Python para Dados', 119.00), ('Estatística Básica', 159.90), ('Storytelling com Dados', 79.90),
                   ('Entendendo Algoritmos', 69.90)],
        'Casa': [('Cafeteira', 189.90), ('Luminária LED', 74.50), ('Garrafa Térmica', 54.90), ('Jogo de Toalhas', 99.90)],
        'Esporte': [('Tênis de Corrida', 349.90), ('Garrafa Squeeze', 29.90), ('Tapete de Yoga', 119.90),
                    ('Mochila Esportiva', 159.00)],
        'Papelaria': [('Caderno Inteligente', 89.00), ('Kit Canetas', 34.90), ('Planner 2025', 64.90)],
    }
    cidades = ['Recife', 'Olinda', 'Caruaru', 'Petrolina', 'Paulista', 'Garanhuns']
    pesos_cidade = [40, 15, 15, 10, 12, 8]
    pagamentos = ['pix', 'cartão de crédito', 'boleto', 'cartão de débito']
    pesos_pag = [45, 35, 8, 12]
    nomes = ['Ana', 'Bruno', 'Carla', 'Diego', 'Eduarda', 'Felipe', 'Gabriela', 'Heitor', 'Isabela', 'João',
             'Larissa', 'Marcos', 'Natália', 'Otávio', 'Paula', 'Rafael', 'Sofia', 'Thiago', 'Vitória', 'Yuri']
    sobrenomes = ['Silva', 'Souza', 'Lima', 'Oliveira', 'Santos', 'Ferreira', 'Albuquerque', 'Cavalcanti',
                  'Barbosa', 'Costa', 'Melo', 'Araújo']
    dias_mes = [31, 28, 31, 30, 31, 30]  # jan a jun de 2025

    linhas = ['id_pedido;data;cliente;cidade;categoria;produto;quantidade;preco_unitario;forma_pagamento']
    registros = []
    for i in range(1, 1201):
        id_pedido = f'PED-{i:05d}'
        mes = random.choices(range(1, 7), weights=[14, 12, 15, 16, 19, 24])[0]
        dia = random.randint(1, dias_mes[mes - 1])
        categoria = random.choices(list(catalogo), weights=[30, 18, 20, 20, 12])[0]
        produto, preco = random.choice(catalogo[categoria])
        qtd = random.choices([1, 2, 3, 4, 5], weights=[55, 25, 10, 6, 4])[0]
        cliente = f'{random.choice(nomes)} {random.choice(sobrenomes)}'
        cidade = random.choices(cidades, weights=pesos_cidade)[0]
        pag = random.choices(pagamentos, weights=pesos_pag)[0]

        # --- sujeira "cosmética" (deve ser CORRIGIDA, não rejeitada) ---
        data = f'2025-{mes:02d}-{dia:02d}'
        if random.random() < 0.30:
            data = f'{dia:02d}/{mes:02d}/2025'
        r = random.random()
        if r < 0.10:
            cidade = cidade.upper()
        elif r < 0.18:
            cidade = '  ' + cidade.lower() + ' '
        if random.random() < 0.12:
            categoria = categoria.lower()
        preco_txt = f'{preco:.2f}'
        r = random.random()
        if r < 0.15:
            preco_txt = f'R$ {preco:.2f}'.replace('.', ',')
        elif r < 0.30:
            preco_txt = f'{preco:.2f}'.replace('.', ',')
        r = random.random()
        if r < 0.12:
            pag = pag.upper()
        elif r < 0.20:
            pag = {'pix': 'Pix', 'cartão de crédito': 'cartao de credito', 'boleto': 'Boleto',
                   'cartão de débito': 'cartao de debito'}[pag]
        qtd_txt = str(qtd)
        registros.append([id_pedido, data, cliente, cidade, categoria, produto, qtd_txt, preco_txt, pag])

    # --- sujeira "grave" (deve ser REJEITADA) ---
    defeitos = ['qtd_texto', 'qtd_zero', 'qtd_negativa', 'qtd_vazia', 'preco_texto', 'preco_vazio',
                'data_vazia', 'data_invalida', 'colunas_faltando', 'categoria_vazia']
    alvos = random.sample(range(len(registros)), 70)
    for n, idx in enumerate(alvos):
        reg = registros[idx]
        defeito = defeitos[n % len(defeitos)]
        if defeito == 'qtd_texto':
            reg[6] = random.choice(['dois', 'três', 'um'])
        elif defeito == 'qtd_zero':
            reg[6] = '0'
        elif defeito == 'qtd_negativa':
            reg[6] = '-1'
        elif defeito == 'qtd_vazia':
            reg[6] = ''
        elif defeito == 'preco_texto':
            reg[7] = random.choice(['grátis', 'N/A', 'consultar'])
        elif defeito == 'preco_vazio':
            reg[7] = ''
        elif defeito == 'data_vazia':
            reg[1] = ''
        elif defeito == 'data_invalida':
            reg[1] = random.choice(['31/02/2025', '2025-13-01', 'ontem', '00/00/0000'])
        elif defeito == 'colunas_faltando':
            registros[idx] = reg[:random.randint(4, 7)]
        elif defeito == 'categoria_vazia':
            reg[4] = ''

    saida = [';'.join(r) for r in registros]
    # --- duplicatas exatas (mesmo pedido exportado duas vezes) ---
    for idx in random.sample(range(len(saida)), 35):
        pos = min(idx + random.randint(1, 30), len(saida))
        saida.insert(pos, saida[idx])
    # linhas em branco perdidas no meio do arquivo
    for _ in range(4):
        saida.insert(random.randint(10, len(saida) - 10), '')
    salvar('projeto01-pipeline-etl-vendas/dados/vendas_brutas.csv', linhas + saida)


# ---------------------------------------------------------------------------
# PROJETO 2 - pesquisa_salarial.csv
# ---------------------------------------------------------------------------
def gerar_salarios():
    cargos = {  # salário base (Júnior, mercado médio)
        'Analista de Dados': 4200,
        'Analista de BI': 4000,
        'Cientista de Dados': 5600,
        'Engenheiro(a) de Dados': 6000,
        'Engenheiro(a) de Machine Learning': 6800,
    }
    pesos_cargo = [32, 16, 20, 22, 10]
    niveis = [('Júnior', 1.0, (0, 2)), ('Pleno', 1.7, (2, 5)), ('Sênior', 2.6, (5, 10)), ('Especialista', 3.4, (8, 16))]
    pesos_nivel = [34, 32, 24, 10]
    ufs = {'SP': 1.22, 'RJ': 1.10, 'DF': 1.15, 'SC': 1.05, 'PR': 1.02, 'MG': 0.98, 'RS': 1.00,
           'PE': 0.92, 'CE': 0.88, 'BA': 0.87}
    pesos_uf = [26, 10, 6, 7, 7, 10, 6, 14, 7, 7]
    modelos = {'Remoto': 1.08, 'Híbrido': 1.02, 'Presencial': 0.92}
    pesos_modelo = [45, 38, 17]

    linhas = ['id,cargo,nivel,anos_experiencia,uf,modelo_trabalho,salario_mensal']
    for i in range(1, 641):
        cargo = random.choices(list(cargos), weights=pesos_cargo)[0]
        nivel, mult_nivel, (emin, emax) = random.choices(niveis, weights=pesos_nivel)[0]
        anos = random.randint(emin, emax)
        uf = random.choices(list(ufs), weights=pesos_uf)[0]
        modelo = random.choices(list(modelos), weights=pesos_modelo)[0]
        salario = cargos[cargo] * mult_nivel * ufs[uf] * modelos[modelo] * random.uniform(0.82, 1.20)
        salario += anos * random.uniform(40, 120)
        salario = round(salario / 50) * 50
        sal_txt = str(salario)
        if random.random() < 0.025:
            sal_txt = random.choice(['', 'prefiro não informar'])
        anos_txt = str(anos)
        if random.random() < 0.015:
            anos_txt = ''
        linhas.append(f'{i},{cargo},{nivel},{anos_txt},{uf},{modelo},{sal_txt}')
    # dois outliers plausíveis (erro de digitação: salário anual informado como mensal)
    linhas[57] = linhas[57].rsplit(',', 1)[0] + ',158000'
    linhas[402] = linhas[402].rsplit(',', 1)[0] + ',212000'
    salvar('projeto02-raio-x-salarial/dados/pesquisa_salarial.csv', linhas)


# ---------------------------------------------------------------------------
# PROJETO 3 - avaliacoes.csv + léxicos
# ---------------------------------------------------------------------------
def gerar_avaliacoes():
    produtos = ['Fone Bluetooth', 'Smartwatch', 'Cafeteira', 'Tênis de Corrida', 'Mochila Esportiva',
                'Caixa de Som', 'Luminária LED', 'Caderno Inteligente']
    # qualidade "real" de cada produto: probabilidade de uma avaliação ser positiva
    qualidade = [0.72, 0.45, 0.80, 0.65, 0.58, 0.38, 0.85, 0.70]

    aspectos = ['o produto', 'a entrega', 'o acabamento', 'a bateria', 'o material', 'a embalagem',
                'o atendimento', 'o som', 'o tamanho', 'a qualidade']
    pos_frases = [
        'Adorei {a}, ficou excelente', 'Muito bom, recomendo demais', '{A} é ótimo e chegou rápido',
        'Produto perfeito, superou as expectativas', 'Gostei muito, vale cada centavo',
        'Qualidade incrível pelo preço', 'Chegou antes do prazo e funciona perfeitamente',
        'Estou satisfeito, {a} é muito bom', 'Excelente compra, maravilhoso', 'Bonito, confortável e resistente',
        'Recomendo, {a} é top', 'Amei! Melhor compra do ano', 'Funciona bem e {a} é bom',
    ]
    neg_frases = [
        'Péssimo, {a} veio com defeito', 'Não recomendo, muito ruim', '{A} é horrível e quebrou na primeira semana',
        'Produto frágil, me arrependi', 'Atrasou muito e veio errado', 'Decepcionado com {a}, fraco demais',
        'Pior compra que já fiz', 'Parou de funcionar em poucos dias, lixo', '{A} é ruim e caro',
        'Quebrado e com defeito, quero devolver', 'Muito fraco, não vale o preço',
        'Esquentou e travou, terrível', 'Barulhento e desconfortável',
    ]
    neu_frases = [
        'Chegou no prazo, {a} é ok', 'Produto mediano, nada demais', 'Cumpre o que promete',
        'É razoável para o dia a dia', '{A} é normal, como esperado', 'Nem bom nem ruim',
        'Esperava um pouco mais, mas serve', 'Ainda estou testando {a}',
    ]
    # casos "difíceis" para o léxico (negação / ironia) -> geram erros de classificação de propósito
    dificeis_pos = ['Não é ruim, gostei', 'Achei que seria fraco, mas não é', 'Não tenho do que reclamar',
                    'Nada de defeito, tudo certo']
    dificeis_neg = ['Não gostei, nada bom', 'Não é bom, não recomendo', 'Ótimo... quebrou em dois dias. Parabéns',
                    'Bonito, mas parou de funcionar']
    complementos = ['', '', '', '!', '!!', '.', '...']

    def frase(lista):
        a = random.choice(aspectos)
        txt = random.choice(lista).format(a=a, A=a[0].upper() + a[1:])
        return txt

    linhas = ['id,produto,nota,comentario']
    for i in range(1, 901):
        idx = random.randrange(len(produtos))
        produto = produtos[idx]
        r = random.random()
        if r < qualidade[idx] * 0.85:
            sentimento = 'pos'
        elif r < qualidade[idx] * 0.85 + 0.15:
            sentimento = 'neu'
        else:
            sentimento = 'neg'

        if sentimento == 'pos':
            nota = random.choices([4, 5], weights=[40, 60])[0]
            partes = [frase(pos_frases)]
            if random.random() < 0.35:
                partes.append(frase(pos_frases))
            if random.random() < 0.10:
                partes = [random.choice(dificeis_pos)]
            if random.random() < 0.08:
                partes.append(frase(neg_frases))  # elogio com ressalva
        elif sentimento == 'neg':
            nota = random.choices([1, 2], weights=[60, 40])[0]
            partes = [frase(neg_frases)]
            if random.random() < 0.35:
                partes.append(frase(neg_frases))
            if random.random() < 0.12:
                partes = [random.choice(dificeis_neg)]
        else:
            nota = 3
            partes = [frase(neu_frases)]
            if random.random() < 0.25:
                partes.append(random.choice([frase(pos_frases), frase(neg_frases)]))
        comentario = '. '.join(partes) + random.choice(complementos)
        if random.random() < 0.15:
            comentario = comentario.upper()
        if random.random() < 0.02:
            nota = random.choice(['', 'cinco'])  # registros inválidos
        linhas.append(f'{i},{produto},{nota},{comentario}')
    salvar('projeto03-termometro-avaliacoes/dados/avaliacoes.csv', linhas)

    positivas = ['adorei', 'amei', 'bom', 'boa', 'bonito', 'confortável', 'excelente', 'gostei', 'incrível',
                 'maravilhoso', 'melhor', 'ótimo', 'ótima', 'perfeito', 'perfeitamente', 'rápido', 'recomendo',
                 'resistente', 'satisfeito', 'superou', 'top', 'vale', 'certo', 'funciona']
    negativas = ['arrependi', 'atrasou', 'barulhento', 'caro', 'decepcionado', 'defeito', 'desconfortável',
                 'devolver', 'errado', 'esquentou', 'fraco', 'frágil', 'horrível', 'lixo', 'péssimo', 'pior',
                 'quebrou', 'quebrado', 'reclamar', 'ruim', 'terrível', 'travou', 'parou']
    stopwords = ['a', 'o', 'e', 'é', 'de', 'do', 'da', 'em', 'no', 'na', 'um', 'uma', 'com', 'que', 'para',
                 'pelo', 'pela', 'me', 'muito', 'mais', 'mas', 'já', 'eu', 'os', 'as', 'se', 'ao', 'cada',
                 'como', 'dias', 'dia', 'primeira', 'semana', 'poucos', 'tudo', 'ainda', 'estou', 'ficou',
                 'veio', 'chegou', 'demais', 'do', 'que', 'fiz', 'achei', 'seria', 'tenho', 'nada', 'nem',
                 'quero', 'dois', 'ano', 'pouco', 'serve', 'antes']
    salvar('projeto03-termometro-avaliacoes/dados/lexico_positivo.txt', sorted(set(positivas)))
    salvar('projeto03-termometro-avaliacoes/dados/lexico_negativo.txt', sorted(set(negativas)))
    salvar('projeto03-termometro-avaliacoes/dados/stopwords.txt', sorted(set(stopwords)))


if __name__ == '__main__':
    gerar_vendas()
    gerar_salarios()
    gerar_avaliacoes()
