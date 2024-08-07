"""
Higher Order Functions
Funções de primeira classe
"""

def saudacao(msg, nome):
    return f'{msg}, {nome}'

def executa(funcao, *args):
    return funcao(*args)

nome = 'Erick'

print(executa(saudacao, 'Bom dia', nome))
print(executa(saudacao, 'Bom tarde', nome))
print(executa(saudacao, 'Bom noite', nome))

