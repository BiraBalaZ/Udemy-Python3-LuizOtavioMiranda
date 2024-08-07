import json

# pessoa = {
#     'nome': 'Erick',
#     'sobrenome': 'Monteiro dos Anjos',
#     'enderecos': [
#         {'rua': 'R. Moreira e Costa', 'numero': 21},
#         {'rua': 'R. Professor Arnaldo João Semeraro', 'numero': 790},
#     ],
#     'altura': 1.6,
#     'numeros_preferidos': (11, 111),
#     'dev': True,
#     'nada': None,
# }

# with open('aula117.json', 'w', encoding='utf8') as arquivo:
#     json.dump(pessoa, arquivo, ensure_ascii=False, indent=4)

# puxando do .json
with open('aula117.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    # print(pessoa)

    print(pessoa['nome'], pessoa['sobrenome'])