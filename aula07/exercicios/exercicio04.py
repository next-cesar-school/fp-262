# Definindo os nomes dos arquivos
arquivo_entrada = 'dados_sujos.csv'
arquivo_saida = 'dados_limpos.csv'

print("--- Iniciando a limpeza de dados ---\n")

try:
    # Abrindo os dois arquivos simultaneamente (leitura e escrita)
    with open(arquivo_entrada, 'r', encoding='utf-8') as f_in, open(arquivo_saida, 'w', encoding='utf-8') as f_out:
        
        linhas = f_in.readlines()
        
        if linhas:
            # Pega a primeira linha (cabeçalho) e já escreve no arquivo de saída
            cabecalho = linhas[0]
            f_out.write(cabecalho)
            
            # Percorre as demais linhas (pulando o cabeçalho)
            for linha in linhas[1:]:
                # Remove quebras de linha no final e pula linhas vazias
                linha_limpa = linha.strip()
                if not linha_limpa:
                    continue
                
                # Divide as colunas pela vírgula
                dados = linha_limpa.split(',')
                
                try:
                    # Tenta acessar as colunas 2 e 3 (pode dar IndexError)
                    # Tenta converter para int e float (pode dar ValueError)
                    idade = int(dados[2])
                    valor_compra = float(dados[3])
                    
                    # Se chegou aqui sem erros, a linha é válida! 
                    # Gravamos a linha original (com o \n) no arquivo novo
                    f_out.write(linha)
                    
                except ValueError:
                    # Cai aqui se a idade não for int ou a compra não for float (ex: 'N/A', 'cem reais', 'NULL', vazios)
                    print(f"❌ Erro de Valor | Linha ignorada: {linha_limpa}")
                    
                except IndexError:
                    # Cai aqui se a linha não tiver vírgulas suficientes (ex: '9,Igor,50')
                    print(f"❌ Erro de Coluna | Linha ignorada: {linha_limpa}")

    print(f"\n✅ Processamento concluído! Dados válidos salvos em '{arquivo_saida}'.")

except FileNotFoundError:
    print(f"Erro: O arquivo '{arquivo_entrada}' não foi encontrado na pasta.")
