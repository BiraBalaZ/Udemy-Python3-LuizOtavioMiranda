
"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input("Digite um número inteiro: ")
mensgem = None

if numero.isdigit():
    if int(numero) % 2 == 0:
        mensagem = 'Par'
    else:
        mensagem = 'Ímpar'
else:
    mensagem = 'Você não digitou um npumero inteiro.'

print(mensagem)
