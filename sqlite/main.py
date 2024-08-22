import sqlite3
from pathlib import Path
from os import system

# Pegando o caminho do nosso arquivo
ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

# Conectando ao servidor
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

#------------------------------------ SQL -------------------------------------#
# CUIDADO: fazendo DELETE sem "WHERE"
# Deletando todo o DataBase
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)

# Deletando a sequencia de ID (resetando)
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name = "{TABLE_NAME}"'
)
connection.commit()

#----------------------------- Criando Nossa Table ----------------------------#
# Esse comando cria a tabela, mas só SE ela NÃO existir
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

#-------------------------- Primeira forma de inserir -------------------------#
# CUIDADO: Esta forma está sujeita à SQL Injection
# cursor.execute(
#     f'INSERT INTO {TABLE_NAME} '
#     '(name, weight) '
#     'VALUES '
#     '("Erik", 5), ("Erick", 5), ("Sarah", 4),',
#     '("Larissa", 5), ("Fernanda", 5), ("Victória", 5)'
# )
# connection.commit()

#-------------------------- Segunda forma de inserir --------------------------#
# sql = (
#     f'INSERT INTO {TABLE_NAME} '
#     '(name, weight) '
#     'VALUES '
#     '(?, ?)'
# )

# cursor.execute(sql, ['Erick', 5])
# connection.commit()

#-------------------------- Terceira forma de inserir -------------------------#
# sql = (
#     f'INSERT INTO {TABLE_NAME} '
#     '(name, weight) '
#     'VALUES '
#     '(?, ?)'
# )

# cursor.executemany(
#     sql,
#     [
#         ['Erick', 5], ['Sarah', 4], ['Larissa', 5],
#         ['Erik', 5], ['Fernanda', 5], ['Victória', 5]
#     ]
# )
# connection.commit()

#--------------------------- Quarta forma de inserir --------------------------#
# sql = (
#     f'INSERT INTO {TABLE_NAME} '
#     '(name, weight) '
#     'VALUES '
#     '(:name, :weight)'
# )

# cursor.execute(sql, {'name': 'Erick', 'weight': 5})
# connection.commit()

#--------------------------- Quinta forma de inserir --------------------------#
sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) '
    'VALUES '
    '(:name, :weight)'
)

cursor.executemany(
    sql,
    [
        {'name': 'Erik', 'weight': 5}, {'name': 'Erick', 'weight': 5},
        {'name': 'Sarah', 'weight': 4}, {'name': 'Larissa', 'weight': 5},
        {'name': 'Fernanda', 'weight': 5}, {'name': 'Victória', 'weight': 5}
    ]
)
connection.commit()

#---------------------------- Limpando o Terminal -----------------------------#
system('cls')

# Printando o código que foi enviado
print(sql)

#---------------------------- Fechando o servidor -----------------------------#
cursor.close()
connection.close()
