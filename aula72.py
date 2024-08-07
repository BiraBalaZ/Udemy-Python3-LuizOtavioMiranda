"""
Exercícios com funções

Crie uma função que multiplica todos os argumentos
não nomeados recebidos.
Retorne o total para uma variável e mostre o valor
da variável.

Crie uma função fala se o número é par ou ímpar.
Retorne se o número é par ou ímpar.
"""
def multiplicador(*args):
    res = 1
    for numero in args:
        res = res * numero
    return res

print(multiplicador(1, 2, 3, 10))

def parimp(numero):
    if numero % 2 == 0:
        return "par"
    return "ímpar"

print(parimp(3))
print(parimp(2))
