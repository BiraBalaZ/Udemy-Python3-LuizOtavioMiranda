# Função lambda em Python
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única expressão.
#
# lista = [
#     {'nome': 'Erick', 'sobrenome': 'Monteiro'},
#     {'nome': 'Sarah', 'sobrenome': 'Fernandes'},
#     {'nome': 'Fernanda', 'sobrenome': 'Sousa'},
#     {'nome': 'Victória', 'sobrenome': 'Martins'},
#     {'nome': 'Larissa', 'sobrenome': 'Dohany'},
# ]

# lista = [4, 32, 1, 34, 5, 6, 6, 21]
# lista.sort(reverse=False)
# print(lista)

lista = [
    {'nome': 'Erick',    'sobrenome': 'Monteiro',  'idade': 21},
    {'nome': 'Sarah',    'sobrenome': 'Fernandes', 'idade': 21},
    {'nome': 'Fernanda', 'sobrenome': 'Sousa',     'idade': 21},
    {'nome': 'Victória', 'sobrenome': 'Martins',   'idade': 21},
    {'nome': 'Larissa',  'sobrenome': 'Dohany',    'idade': 21},
]

def show(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista,key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

show(l1)
show(l2)
