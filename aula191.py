# request para requisições HTTP
# pip install requests types-requests
import requests
import os
os.system('cls')

# http:// -> Rodando automaticamente na porta 80   \
#                                                   } Mas só se nao tiver informado outra porta
# https:// -> Rodando automaticamente na porta 443 /
url = 'http://localhost:3333/'
response = requests.get(url)
print(response.status_code)
# print(response.headers)
# print(response.content)
# print(response.json)
print(response.text)


