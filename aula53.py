'''
enumerate - numera iteráveis (índices)
'''
lista = ['Erick', 'Sarah', 'Alice', 'Larissa', 'Fernanda', 'Victória', 'Erik', 'Fábio', 'Renata']
lista.append('Pochita')

# for item in enumerate(lista):
#      print(item)

# for item in enumerate(lista):
#      indice, nome = item
#      print(indice, nome)

for indice, nome in enumerate(lista):
     print(indice, '\t', nome)

# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')
