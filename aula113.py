# reduce - faz a redução de um iterável em um valor
from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

""" Resolução 1 """
# def funcao_reduce(acumulador, produto):
#     # print('Total R$', acumulador)
#     # print('produto', produto)
#     # print()
#     return acumulador + produto['preco']

""" Resolução 2 """
# total = reduce(
#     funcao_reduce,
#     produtos,
#     0
# )

# total = 0
# for produto in produtos:
#     total += produto['preco']


""" Resolução 3 """
total = reduce(
    lambda ac, p: ac + p['preco'],
    produtos,
    0
)

print(f'Total R$ {total:.2f}')
