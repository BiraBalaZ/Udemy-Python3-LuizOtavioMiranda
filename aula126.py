# __dict__ e vars para atributos de instância
class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

dados = {'nome':'João','idade': 45}
joao = Pessoa(**dados)
# print(joao.nome)
# print(joao.idade)
print(joao.__dict__)

p1 = Pessoa('Erick', 21)
# p1.nome = 'Erique'
# print(p1.nome)

print(p1.__dict__)
print(vars(p1))
