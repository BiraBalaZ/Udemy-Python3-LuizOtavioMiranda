# Funções decoradoras e decoradores com métodos

def meu_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr


def adiciona_repr(cls):
    cls.__repr__ = meu_repr
    return cls


def meu_planeta(metodo):
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)

        if 'Terra' in resultado: # ou: if resultado=='Terra':
            return 'Você está em casa'

        return resultado
    return interno


@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome


@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome

    @meu_planeta
    def falar_nome(self):
        return f'O planeta é {self.nome}'


brasil = Time('Brasil')
alemanha = Time('Alemanha')

terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(alemanha)
print(terra)
print(marte)

print(terra.falar_nome())
print(marte.falar_nome())

print(f'{brasil.nome} perdeu de 7x0 pra {alemanha.nome} no Planeta {terra.nome} mas vai ganhar no Planeta {marte.nome}!')
