"""
Argumentos nomeados e não nomeados em funções Python.
Argumento nomeado tem nome com sinal de igual.
Argumento não nomeado recee apenas o argumento (valor).
"""
def soma(x, y):
    # Docstring
    res = f'{x=} y={y} | x + y = {x + y}'

    return res

# Argumento NÃO nomeado
print(soma(1, 2))

# Argumento nomeado
soma(y=2, x=1)

