"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira.

Loop infinito --> Quando um código não tem fim.
While True:
    <code>
"""
name_list = []

while True:
    contador = 0
    nome = input('Qual o nome? ').capitalize()

    if nome == 'Sair':
        break
    else:
        contador += 1
        print(f'{nome} adicionado na lista!')
        name_list.append(nome)

if len(name_list) > 0:
    print(f'Você decidiu sair e cadastrou {len(name_list)} nomes:\n{name_list}')
else:
    print('Você decidiu sair e não cadastrou nenhum nome.')
