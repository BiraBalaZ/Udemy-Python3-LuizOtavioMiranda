# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
from os import system

to_do = []
to_do_refazer = []
while True:
    print('Comandos: listar, desfazer, refazer')
    prompt = input('Digite uma tarefa ou comando: ')

    if prompt == 'listar':
        if len(to_do) > 0:
            print('TAREFAS')
            for item in to_do:
                print(f'\t{item}')
        else:
            print('Nada para listar.')
        continue
    elif prompt == 'desfazer':
        item = to_do.pop()
        to_do_refazer.append(item)
        continue
    elif prompt == 'refazer':
        item = to_do_refazer.pop()
        to_do.append(item)
    elif prompt == 'clear':
        system('cls')
    elif prompt == 'exit':
        break
    else:
        to_do.append(prompt)
        continue
