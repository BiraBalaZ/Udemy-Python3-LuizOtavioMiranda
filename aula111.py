from functools import partial

# map - para mapear dados
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [
    {'nome': 'Produto5', 'preco': 10.00},
    {'nome': 'Produto1', 'preco': 22.32},
    {'nome': 'Produto3', 'preco': 10.11},
    {'nome': 'Produto2', 'preco': 105.87},
    {'nome': 'Produto4', 'preco': 69.90},
]

def aumentar_porcontagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

aumentar_dez_procento = partial(
    aumentar_porcontagem,
    porcentagem = 1.1
)

# novos_produtos = [
#     {**p,
#      'preco':aumentar_dez_procento(p['preco'])}
#     for p in produtos
# ]

def muda_preco(produto):
    return {
        **produto,
        'preco':aumentar_dez_procento(
             produto['preco']
         )
    }

novos_produtos = map(
    muda_preco,
    produtos
)

print_iter(produtos)
print_iter(novos_produtos)
