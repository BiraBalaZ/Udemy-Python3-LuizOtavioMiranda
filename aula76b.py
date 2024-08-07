# Manipulando chaves e valores em dicionários
pessoa = dict()

pessoa['nome'] = 'Erick Monteiro'
pessoa['sobrenome'] = 'dos Anjos'

print(pessoa)
print(pessoa['nome'])
print(pessoa['sobrenome'])

del pessoa['sobrenome']

print(pessoa['nome'])
print(pessoa['sobrenome']) # Retornará erro
