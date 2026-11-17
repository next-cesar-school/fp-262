import os


print(os.getcwd())          # Diretório atual
os.mkdir("nova_pasta")      # Cria uma pasta chamada 'nova_pasta'
os.rmdir("nova_pasta")      # ⚠️ Remove a pasta chamada 'nova_pasta'
os.path.exists('teste.txt') # Verifica se um caminho existe
