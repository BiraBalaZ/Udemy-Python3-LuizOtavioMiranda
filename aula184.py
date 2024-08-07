# Variáveis de ambiente com Python
# Para variáveis de ambiente
# Windows PS: $env:VARIAVEL="VALOR" | dir env:
# Linux e Mac: export NOME_VARIAVEL="VALOR" | echo $VARIAVEL
# Para obter o valor das variáveis de ambiente
# os.getenv ou os.environ['VARIAVEL']
# Para configurar variáveis de ambiente
# os.environ['VARIAVEL'] = 'valor'
# Ou usando python-dotenv e o arquivo .env
# pip install python-dotenv
# from dotenv import load_dotenv
# load_dotenv()
# https://pypi.org/project/python-dotenv/
# OBS.: sempre lembre-se de criar um .env-example
import os
from dotenv import load_dotenv  # type: ignore

# Carrega o arquivo .env que foi criado manualmente na raiz do programa
load_dotenv()

# print(os.environ)

# for item in os.environ:
#     print('-', item)

# print(os.getenv('SENHA'))

print(os.getenv('DB_USER'))
print(os.getenv('DB_PASSWORD'))
print(os.getenv('DB_PORT'))
print(os.getenv('DB_HOST'))
