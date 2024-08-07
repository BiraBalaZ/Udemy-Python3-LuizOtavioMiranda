# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.
class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def inserir_endereco_externo(self, endereco):
        self.enderecos.append(endereco)


    def listar_enderecos(self):
        # print(*self.enderecos, sep='\n')
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self):
        print('APAGANDO,', self.nome)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('APAGANDO,', self.rua, self.numero)

cliente1 = Cliente('Maria')
cliente1.inserir_endereco('Av. Brasil', 54)
cliente1.inserir_endereco('R. Limoeiro', 6745)
endereco_externo = Endereco('R. Legal', 1234)
cliente1.inserir_endereco_externo(endereco_externo)
cliente1.listar_enderecos()

# print()
# cliente2 = Cliente('Erick')
# cliente2.inserir_endereco('R. Moreira e Costa', 21)
# cliente2.inserir_endereco('R. Prof. Arnaldo João Semeraro', 790)
# cliente2.listar_enderecos()
