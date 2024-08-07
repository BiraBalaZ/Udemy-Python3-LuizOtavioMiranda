# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load
import os
caminho_arquivo = 'C:\\Users\\erick\\OneDrive\\Documentos\\Udemy\\Python\\'
caminho_arquivo += 'aula116.txt'

# try:
#     arquivo = open(caminho_arquivo, 'r')
# except FileNotFoundError:
#     arquivo = open(caminho_arquivo, 'w')
# finally:
#     arquivo.close()

# "with" já abre e fecha o arquivo
# with open(caminho_arquivo, 'w') as arquivo:
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
    
#     arquivo.writelines(
#         ('Linha 3\n','Linha 4\n')
#     )

#     # arquivo.seek(0, 0)

# with open(caminho_arquivo, 'r') as arquivo:
#     print(arquivo.read())

# with open(caminho_arquivo, 'a+') as arquivo:
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')

with open(caminho_arquivo, 'w+', encoding='utf8') as arquivo:    
    arquivo.write('ANTENÇÃO\n')
    arquivo.write('Lorem Ipsum Dolor Sit Amet\n')

os.unlink(caminho_arquivo)
# os.rename(caminho_arquivo, 'aula116-2.txt')
# os.unlink('aula116-2.txt')