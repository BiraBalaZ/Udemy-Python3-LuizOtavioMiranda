from pessoas import Cliente
import contas
from os import system

system('cls')

c1 = Cliente('Erick', 21)
c1.conta = contas.ContaCorrente('0001', '01', 1000)
c1.conta.detalhes()

c2 = Cliente('Sarah', 21)
c2.conta = contas.ContaPoupanca('0002', '01', 2200)
c2.conta.detalhes()

c3 = Cliente('Larissa', 21)
c3.conta = contas.ContaCorrente('0003', '01', 4500)
c3.conta.detalhes()

c4 = Cliente('Victória', 21)
c4.conta = contas.ContaPoupanca('0004', '01')
c4.conta.detalhes()

c5 = Cliente('Fernanda', 21)
c5.conta = contas.ContaPoupanca('0005', '01', 3150)
c5.conta.detalhes()
