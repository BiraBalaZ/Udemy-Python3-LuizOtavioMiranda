from os import system
system('cls')
# O Python é uma linguagem de programação multiparadigma.\nPython foi criado por Guido Van Rossum.
frase = 'aaaooo'

i = 0
quantidade = 0 # Quantidade que a letra que apareceu mais vezes apareceu
letra = '' # Qual a letra que apareceu mais vezes

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ': # Se for um espaço, ele não contabiliza e prossegue
        i += 1
        continue

    quantidade_atual = frase.count(letra_atual)

    if quantidade < quantidade_atual:
        quantidade = quantidade_atual
        letra = letra_atual

    i += 1

print(frase)
print(f'A letra "{letra}" apareceu: {quantidade}x')
