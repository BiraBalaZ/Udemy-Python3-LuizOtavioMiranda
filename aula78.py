# Sets - Conjuntos em Python (tipo set)

# Conjuntos são ensinados na matemática
# Representados graficamente pelo diagrama de Venn.
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}

# sets são eficientes para remover valores duplicados
# de iteráveis.
# - eles não tem índexes;
# - eles não garantem ordem;
# - eles são iteráveis (for, in, not, in)

"""
s1 = set('Luiz')
# Não garante a ordem
print(s1, type(s1)) # {'z', 'L', 'i', 'u'} <class 'set'>

l1 = [1, 3, 1, 2, 2, 2, 2, 3]
s2 = set(l1)
# Ele remove itens duplicados
print(s2) # {1, 2, 3}

for numero in s2:
    print(numero)

s3 = {1, 2, 3, {123}} # Gera erro, não pode haver set dentro de outro set
"""

# Métodos úteis:
# add, update, clear, discard

"""
s1 = set()
s1.add('Erick')
s1.add(1)
print(s1)

s1.update(('Olá mundo', 1, 2, 3, 4))
print(s1)

s1.discard(3)
print(s1)
"""

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intesection) - Itens presentes em ambos
# diferença - itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos


s1 = {1, 2, 3}
s2 = {2, 3, 4}

s3 = s1 | s2 # Une os dois e elimina duplicados           >>> {1, 2, 3, 4}
s3 = s1 & s2 # Retorna aqueles que se repetemm            >>> {2, 3}
s3 = s1 - s2 # Retorna o que nao se repete no da esquerda >>> {1}
s3 = s1 ^ s2 # Retorna o que nao se repete no da direita  >>> {4}

print(s3)
