"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índice inexistentes na lista.
"""
from os import system

lista = []

while True:
    print('Selecione uma opção')
    opcao = str(input('[i]nserir [a]pagar [l]istar: '))

    if opcao.startswith('i'):
        quantidade_item = 0
        item = str(input('Valor: '))

        lista.append(item)
        quantidade_item += 1
    elif opcao.startswith('a') and len(lista) > 0:
        item = int(input('Escolha o índice para apagar: '))

        try:
            del lista[item]
            print('Item deletado da lista')        
        except:
            print('Não foi possível apagar este índice')
        
    elif opcao.startswith('a') and len(lista) == 0:
        print('Nada para apagar')
    elif opcao.startswith('l') and len(lista) > 0:
        for valor, item in enumerate(lista):
            print(valor, '-', item, 'x',quantidade_item)
    elif opcao.startswith('l') and len(lista) == 0:
        print('Nada para listar')
    elif opcao.startswith('e'):
        break
    else:
        print('Insira uma opção válida!')
