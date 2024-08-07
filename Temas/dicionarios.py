# Dicionários em Python (tipo dict) 
# Dicionários são estrutras de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas com o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualuqer tipo, incluindo outro
# dicionário.
# Usamos as chaves "{}" ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutáveis: dict, list

pessoa = {
  'nome': 'Luiz Otávio',
  'sobrenome': 'Miranda',
  'idade' : 18,
  'altura': 1.8,
  'endereços': [
      {'rua': 'tal tal', 'número': 123},
      {'rua': 'outra rua', 'número': 321}
  ]
}

print(pessoa, type(pessoa))

# Métodos úteis dos dicionários em python.
# len        - Quantas chaves;
# keys       - Iterável com as chaves;
# values     - Iterável com os valores;
# items      - Iterável com chaves e valores;
# setdefault - Adiciona valor se a chave não existe ;
# copy       - Retorna uma cópia rasa (shallow copy);
# get        - Obtém uma chave;
# pop        - Apaga um item com a chave especificada (del);
# popitem    - Apaga o último item adicionado;
# update     - Atualiza um dicionário com outro.

pessoa = {
    'nome': 'Erick',
    'sobrenome': 'Monteiro dos Anjos',
    'idade': 21,
    'altura': 1.68,
    'peso': 57.4
}

print(pessoa.__len__())
print(pessoa.keys())
print(pessoa.values())

for key, value in pessoa.items():
    print(key, value)

from copy import deepcopy
d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}

d2 = deepcopy(d1)

d2['c1'] = 1000
d2['l1'][1] = 999999

print(d1)
print(d2)

p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}

print(p1['nome']) # Retorna erro

p1.update({'sobrenome': 'Miranda Oliveira', 'idade': 47}) # Atualiza e Adiciona novos valores

print(p1.get('nome', 'Not found'))
print(p1.get('sobrenome', 'Not found'))
print(p1.get('idade', 'Not found'))

print(p1)
