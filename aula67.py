"""
Valores padrão para parâmetros.
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
"""

def soma(x, y, z=None):
    if z != None:
        print(f'{x = }\n{y = }\n{z = }\nx + y + z =', x + y + z)
    else:
        print(f'{x = }\n{y = }\nx + y =', x + y)

soma(4, 5)
soma(4, 5, 6)
soma(1, 1, 0)


