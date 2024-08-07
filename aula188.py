# argparse.ArgumentParser para argumentos mais complexos
# Tutorial Oficial:
# https://docs.python.org/pt-br/3/howto/argparse.html
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('-b', '--b')
args = parser.parse_args()

if args.b is None:
    print('Você não passou o valor de b.')
else:
    print('O Valor de b:', args.b)
