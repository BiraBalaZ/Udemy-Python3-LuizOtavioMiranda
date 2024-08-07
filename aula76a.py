# Dicionários em Python (tipo dict)
# 
# Dicionários são estrutras de dados do tipo
# par de "chave" e "valor".
# 
# Chaves popdem ser consideradas com o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# 
# O valor pode ser de qualuqer tipo, incluindo outro
# dicionário.
# 
# Usamos as chaves "{}" ou a classe dict para criar
# dicionários.
# 
# Imutáveis: str, int, float, bool, tuple
# Mutáveis: dict, list
# 
# pessoa = {
#   'nome': 'Luiz Otávio',
#   'sobrenome': 'Miranda',
#   'idade' : 18,
#   'altura': 1.8,
#   'endereços': [
#       {'rua': 'tal tal', 'número': 123},
#       {'rua': 'outra rua', 'número': 321}
#   ]
# }
# 
# print(pessoa, type(pessoa))

pessoa = {
  'nome': 'Erick Monteiro',
  'sobrenome': 'dos Anjos',
  'idade' : 21,
  'altura': 1.68,
  'endereços': [
      {'rua': 'R. Moreira e Costa', 'número': 21},
      {'rua': 'R. Professor Arnaldo João Semeraro', 'número': 730}
  ]
}

# print(pessoa, type(pessoa))
print(pessoa['nome'], pessoa['endereços'][1])
