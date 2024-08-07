# Atributos de classe
class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
p1 = Pessoa('Erick', 21)
p2 = Pessoa('Fabio', 52)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
