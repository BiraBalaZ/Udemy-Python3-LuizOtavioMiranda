"""
Faça uma lista de ompras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índice inexistentes na lista.
"""
from os import system

lista = []

while True:
    print('Selecione uma opção')
    opcao = str(input('[i]nserir [a]pagar [l]istar [e]xit: '))

    if opcao == 'i':
        system('cls')
        item = input('Valor ')
        lista.append(item)
    elif opcao == 'a':
        system('cls')
        indice = int(input('Escolha o índice para apagar: '))

        try:
            del lista[indice]
        except:
            print('Não foi possível apagar este índice')
    elif opcao == 'l':
        system('cls')

        if len(lista) == 0:
            print('Nada para listar')

        for indice, item in enumerate(lista):
            print(f'{indice} - {item}')
    elif opcao == 'e':
        break
    else:
        print('Por favor, escolha uma opçao válida.')
