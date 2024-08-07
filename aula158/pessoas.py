import contas

class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: contas.Conta | None = None


if __name__ == '__main__':
    c1 = Cliente('Erick', 21)
    c1.conta = contas.ContaCorrente('0007', '01', 10000, 5000)
    c1.conta.detalhes()