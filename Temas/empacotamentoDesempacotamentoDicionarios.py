# Empacotamento e desempacotamento de dicionários

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

a, b = 1, 2
a, b = b, a
print(a, b)

(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2)
print(b1, b2)

for chave, valor in pessoa.items():
    print(chave, valor)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoas_completa = {**pessoa, **dados_pessoa}

print(pessoas_completa)

# args e kwargs
# args (já vimos)
# kawargs - keyword arguments (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

mostro_argumentos_nomeados(1, 2, nome = 'Joana', qlq=123)

mostro_argumentos_nomeados(**pessoas_completa)
