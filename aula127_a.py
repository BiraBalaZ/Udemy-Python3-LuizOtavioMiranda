# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json
CAMINHO = 'aula127.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Erick', 21)  # 2003
p2 = Pessoa('Renata', 40) # 1984
p3 = Pessoa('Fabio', 51)  # 1973
p4 = Pessoa('Alice', 6)  # 2018

database = [vars(p1), vars(p2), vars(p3), vars(p4)]

def fazer_dump():
    with open(CAMINHO, 'w', encoding='utf8') as arquivo:
        print('FAZENDO DUMP')
        json.dump(database, arquivo, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    fazer_dump()
