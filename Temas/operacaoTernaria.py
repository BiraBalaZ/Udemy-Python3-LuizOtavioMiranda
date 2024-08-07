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

