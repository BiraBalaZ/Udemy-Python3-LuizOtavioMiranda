"""
split e join com list e str
split - divide uma string
join - une uma string
"""
frase = 'Maria e João comem pão, somente de finais de semana'
lista_palavras = frase.split(',')

for indice, frase in enumerate(lista_palavras):
    print(lista_palavras[indice].strip())

# print(lista_palavras)
