for numero in range(1, 40):
    caminho = f'..\\aula{numero}.py'

    print('Criando arquivo Nº', numero, '\t-  ', caminho)
    with open(caminho, 'w+', encoding='utf8') as arquivo:    
        arquivo.write(f'# Aula {numero}\n')
        arquivo.write('# Lorem Ipsum Dolor Sit Amet\n')
