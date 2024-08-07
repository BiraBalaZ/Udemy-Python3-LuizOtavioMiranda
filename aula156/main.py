from umaLinha import clear
import documentando_funcoes
clear()

pi = 3.14

# print(help(documentando_funcoes))
print(documentando_funcoes.soma(pi, 2.5, 1))
soma = documentando_funcoes.soma(pi, 2.5)
multiplicacao = documentando_funcoes.multiplica(pi**2, 3)

print(documentando_funcoes.multiplica(pi, soma, multiplicacao))
