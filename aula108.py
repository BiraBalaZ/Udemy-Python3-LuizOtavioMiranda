# count é um iterator sem fim (itertools)
from itertools import count

c1 = count(8, 8)
r1 = range(8, 81, 8)

print('count')
for i in c1:
    if i >= 81:
        break

    print(i)

print('\nrange')
for i in r1:
    if i > 100:
        break

    print(i)
