"""
args - Argumentos não nomeados.
* - *args (empacotamento e desempacotamento).
"""
# Lembre-te de desempacotamento
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

def soma(x, y):
    return x + y

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

res = soma(1, 2, 3, 4, 5, 6)
print(res)
