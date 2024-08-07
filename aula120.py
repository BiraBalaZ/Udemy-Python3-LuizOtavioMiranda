# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Erick', 'Monteiro')
p2 = Pessoa('Sarah', 'Alcaide')
# p1.nome = 'Erick'
# p1.sobrenome = 'Monteiro'
# p2.nome = 'Sarah'
# p2.sobrenome = 'Alcaide'
print(p1.nome, p1.sobrenome)
print(p2.nome, p2.sobrenome)
