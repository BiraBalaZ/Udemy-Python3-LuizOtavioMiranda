# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path
from os import system

system('cls')

CAMINHO_CSV = Path(__file__).parent / 'aula178.csv'

# Lendo em formato Dicionário
with open(CAMINHO_CSV, 'r') as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        print(linha['Nome'], linha['Idade'], linha['Endereço'])

# Lendo em formato Lista
# with open(CAMINHO_CSV, 'r', encoding='utf8') as arquivo:
#     leitor = csv.reader(arquivo)

#     # print(next(leitor))
#     for linha in leitor:
#         print(linha)
