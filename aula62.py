"""
Calculo do segundo dígito do CPF

Site utilizado para geração do CPF:
https://www.4devs.com.br/gerador_de_cpf

CPF Gerado: 746.824.890-70

1. Colete a soma dos 9 primeiros dígitos
do CPF, MAIS O PRIMEIRO DÍGITO,
mutiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.: 746.824.890-70 (746824890)

   11  10 9  8  7  6  5  4  3  2
x  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DÍGITO
   _____________________________
   77  40 54 64 14 24 40 36 0 14

2. Somar todos os resultados:

    70 + 36 + 48 + 56 + 12 + 20 + 32 + 27 + 0 + 14 = 363

3. Multiplicar o resultado anterior por 10:

    363 * 10 = 3630

4. Obter o resto da divisão da conta anterior por 11:

    3630 % 11 = 0


Se o resultado anterior for maior que 9:
    resultado é 0
Se não:
    resultado é o valor da conta


O segundo dígito do CPF é 0.
"""
import re

# Coletando CPF do usuário
# cpf = input('Digite o dígitos do seu CPF\n>>> ')
cpf = re.sub(r'[^0-9]', '', '746.824.890-70')
print(cpf)
contador_1 = 10
contador_2 = 11

resultado_digito_1 = 0
resultado_digito_2 = 0

# Fazendo a multiplicação dígito por dígito
# Primeiro dígito
for digito_1 in cpf[:9]:
    resultado_digito_1 += int(digito_1) * contador_1
    contador_1 -= 1

# segundo dígito
for digito_2 in cpf[:10]:
    resultado_digito_2 += int(digito_2) * contador_2
    contador_2 -= 1

# Multiplicando o valor da soma por 10
# E obtendo o resto da divisão por 11
primeiro_digito = (resultado_digito_1 * 10) % 11
segundo_digito = (resultado_digito_2 * 10) % 11

# O resultado só é o valor da conta se
# # for menor ou igual a 9, senão, é 0
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0
print(f"O primeiro dígito do CPF é {primeiro_digito}")

segundo_digito = segundo_digito if segundo_digito <= 9 else 0
print(f"O primeiro dígito do CPF é {segundo_digito}")

cpf_calculado = f'{cpf[:9]}{primeiro_digito}{segundo_digito}'

if cpf == cpf_calculado:
    print('CPF validado com sucesso!')
else:
    print('CPF inválido!')
