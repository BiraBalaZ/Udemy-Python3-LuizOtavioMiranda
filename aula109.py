# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importe
# Produto - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

pessoas = [
    'Erick', 'Sarah', 'Fernanda', 'Victória', 'Larissa', 'Erik',
]
camisetas = [
    ['preta', 'branca'],
    ['PP', 'P', 'M', 'G', 'GG', 'GGXL'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliester'],
]

# print_iter(combinations(pessoas, 2))
# print_iter(permutations(pessoas, 2))

print_iter(product(*camisetas))

