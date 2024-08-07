# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe "callable".
from time import sleep
from os import system

system('cls')

class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome):
        text = f'{nome} está ligando para {self.phone}'

        for i in range(4):
            print(text + '.'*i)
            sleep(.8)
            system('cls')
        
        print('**o número chamado não atende no momento**')


call1 = CallMe('+55 11 1234-56789')
call1('Erick Monteiro')
