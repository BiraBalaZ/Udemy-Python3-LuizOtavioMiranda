# os.walk
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
#  três elementos: o diretória atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files)
import os
from itertools import count
os.system('cls')

caminho = os.path.join('C:\\Users', 'erick', 'OneDrive', 'Documentos', 'Udemy', 'Python', 'EXEMPLO')
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, 'Pasta atual', root)

    # Listando os diretórios
    for dir_ in dirs:
        print('    -', the_counter, 'Dir:', dir_)

    # Listando os arquivos
    for file_ in files:
        print('    -', the_counter, 'FILE:', file_)

    print()
