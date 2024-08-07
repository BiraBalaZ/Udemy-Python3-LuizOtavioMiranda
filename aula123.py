# Escopo da classe e de métodos da classe
class Animal:
    # nome = 'Leão'

    def __init__(self, nome):
        self.nome = nome

leao = Animal('Leão')
print(leao.nome)