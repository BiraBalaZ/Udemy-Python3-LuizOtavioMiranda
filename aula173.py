# os + shutil - Copiando arquivos com Pthon
# 1 - Vamos copiar os arquivos de uma pasta para outra.
# Copiar -> shutil.copy
import os
import shutil
from itertools import count
from aula172 import formata_tamanho
os.system('cls')

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'OneDrive', 'Documentos', 'Udemy', 'Python')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'EXEMPLO')
NOVA_PASTA = os.path.join(DESKTOP, 'NOVA_PASTA')

################################################################################
# caminho = os.path.join('C:\\Users', 'erick', 'OneDrive', 'Documentos', 'Udemy', 'Python', 'EXEMPLO')
# counter = count()

# for root, dirs, files in os.walk(caminho):
#     the_counter = next(counter)
#     print(the_counter, 'Pasta atual', root)

#     # Listando os diretórios
#     for dir_ in dirs:
#         print('    -', the_counter, 'Dir:', dir_)

#     # Listando os arquivos
#     for file_ in files:
#         caminho_completo_arquivo = os.path.join(root, file_)
#         tamanho = os.path.getsize(caminho_completo_arquivo)
#         print('    -', the_counter, 'FILE:', file_, formata_tamanho(tamanho))

#     print()
################################################################################

try:
    os.makedirs(NOVA_PASTA)
except FileExistsError:
    print('\033[31mOpss... Esta pasta já existe!\033[m\n')

for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for dir_ in dirs:
        caminho_novo_diretorio = os.path.join(root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_)
        os.makedirs(caminho_novo_diretorio, exist_ok=True)

    for file in files:
        caminho_arquivo = os.path.join(root, file)
        caminho_novo_arquivo = os.path.join(root.replace(PASTA_ORIGINAL, NOVA_PASTA), file)
        print(caminho_novo_arquivo)

        # copiando
        shutil.copy(caminho_arquivo, caminho_novo_arquivo)
