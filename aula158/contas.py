class Conta:
    limite_extra = 0

    def __init__(self, agencia, conta, saldo = 0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def mostra_saldo(self):
        print(f'O saldo da conta é de R$ {self.saldo} com Limite Especial de R$ {self.limite_extra} \t Total R$ {self.saldo + self.limite_extra}\n')

    def sacar(self, valor):
        print(f"Tentativa de \033[31msaque\033[m de \033[31mR$ {valor}\033[m na conta")

        if valor > (self.saldo + self.limite_extra):
            print(f"\033[31;1mERRO Saldo insuficiente\033[m. (R$ {self.saldo+self.limite_extra})\nValor em conta: R$ {self.saldo}\nLimite Extra: R$ {self.limite_extra}\n")
        elif valor >= self.saldo and valor <= (self.saldo + self.limite_extra):
            print('Operação bem sucedida')
            restante = (self.saldo - valor) * -1
            self.saldo -= valor
            self.limite_extra -= restante
            self.saldo += restante
        else:
            print('Operação bem sucedida')
            self.saldo -= valor

    def depositar(self, deposito):
        print(f'\033[32mDepositanto R$ {deposito}\033[m na conta')
        self.saldo += deposito

    def detalhes(self):
        msg1 = f"Conta: {self.conta} | Agência: {self.agencia}\nSaldo: R$ {self.saldo}"
        msg2 = msg1 + f" | Crédito Especial: R$ {self.limite_extra}\nTotal: R$ {self.saldo + self.limite_extra}\n"
        print(msg1 + '\n' if self.limite_extra == 0 else msg2)

class ContaCorrente(Conta):
    limite_extra = 500


class ContaPoupanca(Conta):
    ...
