def limpar_palavra(palavra):
    """
    Remove pontuações e mantém apenas letras (e o 'ç').
    Retorna a palavra limpa.
    """
    return ''.join(char for char in palavra if char.isalpha() or char == 'ç')

def avaliar_dominancia(palavra, letras_esquerda, letras_direita):
    """
    Conta as letras da palavra baseadas nos conjuntos de cada mão.
    Retorna 'esquerda', 'direita' ou 'empate'.
    """
    pontos_esq = 0
    pontos_dir = 0
    
    for letra in palavra:
        if letra in letras_esquerda:
            pontos_esq += 1
        elif letra in letras_direita:
            pontos_dir += 1
            
    if pontos_esq > pontos_dir:
        return 'esquerda'
    elif pontos_dir > pontos_esq:
        return 'direita'
    else:
        return 'empate'

def analisar_arquivo(nome_arquivo):
    """
    Lê o arquivo de texto, utiliza as funções auxiliares para avaliar
    cada palavra e contabiliza os resultados em um dicionário.
    Retorna o placar (dicionário) e o total de palavras processadas.
    """
    letras_esquerda = set('qwertasdfgzxcvb')
    letras_direita = set('yuiophjklçnm')
    
    placar = {'esquerda': 0, 'direita': 0, 'empate': 0}
    total_palavras = 0
    
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                palavras = linha.lower().split()
                
                for palavra in palavras:
                    palavra_limpa = limpar_palavra(palavra)
                    
                    # Ignora se a palavra ficou vazia após a limpeza
                    if not palavra_limpa:
                        continue
                        
                    total_palavras += 1
                    
                    # Chama a função que avalia a dominância e usa o 
                    # retorno diretamente como chave do dicionário!
                    resultado = avaliar_dominancia(palavra_limpa, letras_esquerda, letras_direita)
                    placar[resultado] += 1
                    
        return placar, total_palavras
        
    except FileNotFoundError:
        print(f"❌ Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return None, 0

def exibir_relatorio(placar, total_palavras):
    """
    Recebe o placar e o total de palavras para calcular 
    e exibir as porcentagens finais.
    """
    if total_palavras > 0:
        print("\n--- ⌨️ Resultado da Análise ---")
        print(f"Total de palavras processadas: {total_palavras}\n")
        print(f"Dominantes com a Mão Esquerda: {placar['esquerda'] / total_palavras:.1%}")
        print(f"Dominantes com a Mão Direita:  {placar['direita'] / total_palavras:.1%}")
        print(f"Palavras Balanceadas (Empate): {placar['empate'] / total_palavras:.1%}")
    else:
        print("O arquivo está vazio ou não contém palavras válidas.")


if __name__ == "__main__":
    print("🔍 Analisando o arquivo de texto...")
    
    arquivo_alvo = 'meu_texto.txt'
    meu_placar, meu_total = analisar_arquivo(arquivo_alvo)
    
    # Só exibe o relatório se a leitura do arquivo não falhou (retorno diferente de None)
    if meu_placar:
        exibir_relatorio(meu_placar, meu_total)
