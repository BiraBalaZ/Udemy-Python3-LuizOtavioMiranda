"""
Iterável -> str, range, etc (__iter__)
Iderador ->  quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
texto = 'Luiz'
numeros = range(0, 100, 8)

for numero in numeros:
    print(numero)
