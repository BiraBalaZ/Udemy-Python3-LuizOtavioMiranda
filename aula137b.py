class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    # @property
    # def motor(self):
    #     return self._motor
    
    # @motor.setter
    # def motor(self, valor):
    #     self._motor = valor

    # @property
    # def fabricante(self):
    #     return self._fabricante
    
    # @fabricante.setter
    # def fabricante(self, valor):
    #     self._fabricante = valor


class Motor():
    def __init__(self, nome):
        self.nome = nome


class Fabricante():
    def __init__(self, nome):
        self.nome = nome


corsa       = Carro('Corsa')
agile       = Carro('Agile')
uno         = Carro('Uno')
gol         = Carro('Gol')

motor_v6    = Motor('V6')
motor_v8    = Motor('V8')
motor_v10   = Motor('V10')
motor_v12   = Motor('V12')
motor_v16   = Motor('V16')

mercedes    = Fabricante('Mercedes')
volkswagen  = Fabricante('Volkswagen')
hyundai     = Fabricante('Hyundai')
chevrolet   = Fabricante('Chevrolet')
fiat        = Fabricante('Fiat')
ford        = Fabricante('Ford')

corsa._motor = motor_v6
corsa._fabricante = hyundai

print('Nome:', corsa.nome, '\nMotor:', corsa._motor.nome, '\nFabricante', corsa._fabricante.nome)

