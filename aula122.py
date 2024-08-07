# Entendendo self em classes Python
class Carro:
    def __init__(eumesmo, nome):
        eumesmo.nome = nome
    def acelerar(self):
        print(f'{self.nome} está acelerando...')

fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro(nome='Celta')
print(celta.nome)
celta.acelerar()
