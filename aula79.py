# Exemplo de uso dos sets

letras = set()

while True:
    letra = input('Digite uma letra: ')

    if letra in '0123456789':
        break
    else:
        letras.add(letra[0].lower())
    
    print(letras)
