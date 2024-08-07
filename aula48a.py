"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento

Métodos úteis: 
    append - Adiciona um item ao final;
    insert - Adicionaum item no índice escolhido;
    pop - Remove do final ou índice escolhido;
    del - Apaga um índice;
    clear - Limpa a lista;
    extend - Estende a lista;
    + - concatena listas

Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40, 50, 60]
print('Mostrando a lista')
print(lista)

lista[2] = 300
print('\nAlterando o valor do índice 2')
print(lista)

del lista[2]
print('\nDeletando o valor do índice 2')
print(lista)

lista.append(70)
print('\nAdicionando um valor ao final da lista')
print(lista)

lista.pop()
print('\nRemovendo o último item da minha lista')
print(lista)

lista.insert(2, 30)
print('\nAdicionando um elemento em um índice espcífico')
print(lista)

lista.clear()
print('\nLimpando a lista')
print(lista)
