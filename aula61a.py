"""
Gerando primeiro dígito de um CPF

Site utilizado para geração do CPF:
https://www.4devs.com.br/gerador_de_cpf

CPF Gerado: 746.824.890-70

1. Colete a soma dos 9 primeiros dígitos
do CPF mutiplicando cada um dos valores
por uma contagem regressiva começando de 10

Ex.: 746.824.890-70 (746824890)

   10  9  8  7  6  5  4  3  2
x  7   4  6  8  2  4  8  9  0
   __________________________
   70  36 48 56 12 20 32 27 0

2. Somar todos os resultados:

    70 + 36 + 48 + 56 + 12 + 20 + 32 + 27 + 0 = 301

3. Multiplicar o resultado anterior por 10:

    301 * 10 = 3010

4. Obter o resto da divisão da conta anterior por 11:

    3010 % 11 = 7


Se o resultado anterior for maior que 9:
    resultado é 0
Se não:
    resultado é o valor da conta


O primeiro dígito do CPF é 7.
"""
cpf = "45094660802"
# cpf = input('Digite o dígitos do seu CPF\n>>> ')
nove_digitos = cpf[:9]
lista = []
contador = 10
soma = 0

# Separando os itens da lista
# Transformando os números de String para Inteiros
for caractere in cpf:
    if caractere != '.' and caractere != '-':
        lista.append(int(caractere))

# Removendo os últimos dois dígitos do CPF
while len(lista) >= 9:
    lista.pop()

# Fazendo a multiplicação dpigito por dígito
for item in range(len(lista)):
    soma += lista[item] * contador
    contador -= 1

# Multiplicando o valor da soma por 10
# E obtendo o resto da divisão por 11
resultado = (soma * 10) % 11

resultado = resultado if resultado <= 9 else 0
print(resultado)
