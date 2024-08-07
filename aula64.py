import random

random_cpf = random.randrange(100000000, 999999999)
cpf = str(random_cpf)
lista_cpf = []
cpf_gerado = ''
contador_1 = 10
contador_2 = 11
resultado_digito_1 = 0
resultado_digito_2 = 0

# Fazendo a multiplicação dígito por dígito
# Primeiro dígito
for digito_1 in cpf:
    resultado_digito_1 += int(digito_1) * contador_1
    contador_1 -= 1

digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print(f"O primeiro dígito do CPF é {digito_1}")

cpf_gerado = f'{cpf}{digito_1}'

# Segundo dígito
for digito_2 in cpf_gerado:
    resultado_digito_2 += int(digito_2) * contador_2
    contador_2 -= 1

digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
print(f"O segundo dígito do CPF é {digito_2}")

cpf_formatado = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{digito_1}{digito_2}'

print(f'CPF gerado com sucesso: {cpf_formatado}')
