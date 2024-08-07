# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários varros
# Exiba o nome do carro, motor e fabricante na tela

class Carro():
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
        self._cor = 'Preto'
        self._placa = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, valor):
        self._cor = valor

    @property
    def placa(self):
        return self._placa

    @placa.setter
    def placa(self, valor):
        self._placa = valor


class Motor():
    def __init__(self, nome):
        self.nome = nome


class Fabricante():
    def __init__(self, nome):
        self.nome = nome

mercedes    = Fabricante('Mercedes')
volkswagen  = Fabricante('Volkswagen')
hyundai     = Fabricante('Hyundai')
chevrolet   = Fabricante('Chevrolet')
fiat        = Fabricante('Fiat')

motor_1_0   = Motor('1.0')
motor_2_0   = Motor('2.0')
motor_3_0   = Motor('3.0')

fusca = Carro('Fusquinha')
fusca.cor = 'Azul'
fusca.fabricante = volkswagen
fusca.motor = motor_1_0
print(f'Carro: {fusca.nome}\nCor: {fusca.cor}\nFabricante: {fusca.fabricante.nome}\nMotor: {fusca.motor.nome}\n')

fiat_uno = Carro('Uno da Firma')
fiat_uno.cor = 'Vinho'
fiat_uno.fabricante = fiat
fiat_uno.motor = motor_1_0
print(f'Carro: {fiat_uno.nome}\nCor: {fiat_uno.cor}\nFabricante: {fiat_uno.fabricante.nome}\nMotor: {fiat_uno.motor.nome}\n')

porche = Carro('Porche Panamera')
porche.fabricante = mercedes
porche.motor = motor_3_0
print(f'Carro: {porche.nome}\nCor: {porche.cor}\nFabricante: {porche.fabricante.nome}\nMotor: {porche.motor.nome}\n')

corsa = Carro('Corsinha')
corsa.fabricante = chevrolet
corsa.motor = motor_1_0
corsa.placa = 'EBO-8915'
print(f'Carro: {corsa.nome}\nCor: {corsa.cor}\nPlaca: {corsa.placa}\nFabricante: {corsa.fabricante.nome}\nMotor: {corsa.motor.nome}\n')

agile = Carro('Agile')
agile.fabricante = hyundai
agile.cor = 'Prata'
agile.motor = motor_2_0
agile.placa = 'ERY-1364'
print(f'Carro: {agile.nome}\nCor: {agile.cor}\nPlaca: {agile.placa}\nFabricante: {agile.fabricante.nome}\nMotor: {agile.motor.nome}\n')
