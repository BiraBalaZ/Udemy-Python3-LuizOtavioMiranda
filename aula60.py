"""
Operação ternária (condicional de uma linha)
<valor> if <condição> else <outro valor>
"""
# print('Valor' if True else 'Outro valor')

# condicao = 10 == 10
# variavel = 'Valor' if condicao else 'Outro valor'
# print(variavel)

digito = 9
# novo_digito = digito if digito <= 9 else 0
# novo_digito = 0 if digito > 9 else digito
# print(novo_digito)

"""
Operação ternária (condicional de uma linha)
<valor> if <condição> else <outro valor>
"""
# Exemplo 1
button = 0 # 0 é Desligado; 1 é Ligado
print('Luz ligada' if button == 1 else 'Luz desligada')

# Exemplo 2
nome = 'Erick'
sexo = 'M'
print(f'{nome} pertence ao sexo masculino' if sexo == 'M' else f'{nome} pertence ao sexo feminino')
