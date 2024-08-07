# Context Manager com função - Criando e Usando gerenciamento de contexto
from contextlib import contextmanager
from os import system
system('cls')


@contextmanager
def  my_open(caminho_arquivo, modo):
    try:
        print('Abrindo o arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo # Yield faz a função e tornar um Generator
    except Exception as error:
        print('AN ERROR HAS OCCURRED:', error)
    finally:
        print('Fechando o arquivo')
        arquivo.close()

with my_open('aula150.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n', 123)
    arquivo.write('Linha 3\n')
    print('WITH', arquivo)

