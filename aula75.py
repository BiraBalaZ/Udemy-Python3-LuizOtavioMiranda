# Exercícios
# Crie funções que duplicam, triplicam e quadriplicam
# o número recebido como parâmetro.

# def duplicar(numero):
#     return numero * 2

# def triplicar(numero):
#     return numero * 3

# def quadruplicar(numero):
#     return numero * 4

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar     = criar_multiplicador(2)
triplicar    = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)
quintuplicar = criar_multiplicador(5)

numero = 2

print(duplicar(numero))
print(triplicar(numero))
print(quadruplicar(numero))
print(quintuplicar(numero))
