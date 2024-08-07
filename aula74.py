"""
Closure e funções que retornam outras funções.
"""


def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

saudacao = criar_saudacao('Saudações')
despedida = criar_saudacao('Adeus')

for nome in ['Erick', 'Sarah', 'Fernanda', 'Larissa', 'Victória']:
    print(saudacao(nome))
    print(despedida(nome))
    print('')
