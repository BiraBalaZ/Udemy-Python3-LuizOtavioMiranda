# Classes decoradoras (Decorator Classes)
from typing import Any


class Multiplicar():
    def __init__(self, func):
        self.func = func
        self.multiplicador = 10

    def __call__(self, *args, **kwargs):
        print(*args)
        resultado = self.func(*args, **kwargs)
        return resultado * self.multiplicador

@Multiplicar
def soma(x, y):
    return x + y

dois_mais_quatro = soma(2, 4)
print(dois_mais_quatro)
