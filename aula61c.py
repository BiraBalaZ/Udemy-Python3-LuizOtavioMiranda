# Coletando CPF do usuário
cpf = input('Digite o dígitos do seu CPF\n>>> ')

# Pegando até o nono dígito
nove_digitos = cpf[:9]
contador = 10
resultado = 0

# Fazendo a multiplicação dígito por dígito
for digito in nove_digitos:
    resultado += int(digito) * contador
    contador -= 1

# Multiplicando o valor da soma por 10
# E obtendo o resto da divisão por 11
resultado = (resultado * 10) % 11

# O resultado só é o valor da conta se
# # for menor ou igual a 9, senão, é 0
resultado = resultado if resultado <= 9 else 0
print(f"O primeiro dígito do CPF é {resultado}")
