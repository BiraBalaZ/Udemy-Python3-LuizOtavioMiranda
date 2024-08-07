# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__() # tem __iter__ e __nex__
iterator = iter(iterable)

# print(next(iterator)) # Eu
# print(next(iterator)) # Tenho
# print(next(iterator)) # __iter__
# print(next(iterator)) # erro

import sys

generator = (n for n in range(1000))
print(sys.getsizeof(generator))
