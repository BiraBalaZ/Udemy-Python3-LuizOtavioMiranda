"""
Cuidados com dados mutáveis
= - copiando o valor (imutáveis)
= - aponta para o mesmo valor na maioria (mutável)
"""

lista_a = ['Erick', 'Sarah']
lista_b = lista_a.copy()

lista_a[0] = 'E.M.A.'
lista_a[1] = 'S.A.F.'
print(lista_a)
print(lista_b)