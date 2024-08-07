# namedtuples - tuplas imutáveis com nomes para valores
# Usamos namedtuples para criar classes de objetos que são apenas um
# agrupamento de atributos, como classes normais sem métodos, ou registros de
# bases de dados, etc.
# As namedtuples são imutáveis assim como as tuplas.
# https://docs.python.org/3/library/collections.html#collections.namedtuple
# https://docs.python.org/3/library/typing.html#typing.NamedTuple
# https://brasilescola.uol.com.br/curiosidades/baralho.htm

# from collections import namedtuple

# Carta = namedtuple('Carta', ['valor', 'naipe'])
# as_espadas = Carta('A', '♠')
# print(as_espadas)

from typing import NamedTuple

class Carta(NamedTuple):
    valor: str = 'VALOR'
    naipe: str = 'NAIPE'

as_espadas = Carta('A')
dois_espadas = Carta('2', '♠')

print(as_espadas._asdict())
print(dois_espadas._asdict())
