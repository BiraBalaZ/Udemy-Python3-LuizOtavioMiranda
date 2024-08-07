def executa(funcao, *args):
    return(funcao(*args))

# def soma(x, y):
#     return x + y

print(executa(lambda x, y: x + y, 2, 3))

# def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         return numero * multiplicador
#     return multiplica

duplica = executa(lambda m: lambda n: n * m, 2)
print(duplica(2))


