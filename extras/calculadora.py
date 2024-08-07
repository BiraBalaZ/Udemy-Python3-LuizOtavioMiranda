from os import system

# Limpado o Terminal
system('cls')

lista_de_operadores = ['+', '-', '/', '*']

def get_operator():
        '''
        Pergunta ao usuário qual operador matemático.

            Parameters:
                None;
            
            Returns:
                Operador (str).
        '''
        operador = input('Digite o operador [+ - / *]\n>>> ')

        if operador not in lista_de_operadores:
            print('Operador não reconhecido, por favor tente novamente:')
            get_operator()

        return operador

# Laço de repetição
while True:    
    # Perguntando ao usuário qual o número das operações.
    numero1 = float(input('Primeiro Número\n>>> '))
    operador = get_operator()
    numero2 = float(input('Segundo Número\n>>> '))

    # Dependendo do operador inserido anteriormente ele faz determinada conta.
    if operador == '+':
        resultado = numero1 + numero2
        print(f'{numero1} + {numero2} = {resultado}')
    elif operador == '-':
        resultado = numero1 - numero2
        print(f'{numero1} - {numero2} = {resultado}')
    elif operador == '/':
        resultado = numero1 / numero2
        print(f'{numero1} / {numero2} = {resultado}')
    elif operador == '*':
        resultado = numero1 * numero2
        print(f'{numero1} x {numero2} = {resultado}')
    else:
        system('cls')
        print(f'Operador inserido: {operador}')
        print('Algo deu errado.')
        break

    # Perguntando se o usuário deseja sair à cada fim de conta.
    sair = input('Quer sair? [S]Sim | [C]Clear terminal\n>>> ').upper()

    # Se ele escolheu sair, o laço de repetição termina.
    if sair.startswith('S'):
        system('cls') # Limpando o terminal
        break
    elif sair.startswith('C'):
        system('cls')
