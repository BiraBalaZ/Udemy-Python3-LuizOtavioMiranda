# copy, sorted, produtos.sort
# Exercícios
from copy import deepcopy

produtos = [
    {'nome': 'Caderno', 'preco':  10.00},
    {'nome': 'Estojo', 'preco':  12.58},
    {'nome': 'Canetas', 'preco':  22.32},
    {'nome': 'Lapizeira', 'preco':  10.11},
    {'nome': 'Mochila', 'preco': 105.87},
    {'nome': 'Calculadora', 'preco':  69.90},
]

# Questão 1.
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
novos_produtos = deepcopy(produtos)

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.10}
    for produto in novos_produtos
]

indice = 0
for chave1, chave2, in novos_produtos:
    print(f'{novos_produtos[indice][chave1]} - {novos_produtos[indice][chave2]:.2f}')
    indice += 1

# Questão 2.
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
def pegar_nome(element):
    return element['nome']

produtos_ordenados_por_nome = deepcopy(novos_produtos)
produtos_ordenados_por_nome.sort(key=pegar_nome, reverse=True)

indice = 0
for chave1, chave2, in produtos_ordenados_por_nome:
    print(f'{produtos_ordenados_por_nome[indice][chave1]} - {produtos_ordenados_por_nome[indice][chave2]:.2f}')
    indice += 1

# Questão 3.
# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
def pegar_preco(element):
    return element['preco']

produtos_ordenados_por_preco = deepcopy(novos_produtos)
produtos_ordenados_por_preco.sort(key=pegar_preco)

indice = 0
for chave1, chave2, in produtos_ordenados_por_preco:
    print(f'{produtos_ordenados_por_preco[indice][chave1]} - {produtos_ordenados_por_preco[indice][chave2]:.2f}')
    indice += 1
