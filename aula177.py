# json.dump e json.load com arquivos
import json
import os

os.system('cls')

NOME_ARQUIVO = 'aula177.json'
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        NOME_ARQUIVO
    )
)


filme = {
    'title': 'O Senhor dos Aneis: A Sociedade do Anel',
    'original_title': 'The Lord of the Rings; The Fellowship of the Ring',
    'is_movie': True,
    'imbd_rating': 8.8,
    'year': 2001,
    'characters': ['Frodo', 'Sam', 'Gandalf', 'legolas', 'Boromir'],
    'budget': None
}

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'w', encoding='utf8') as arquivo:
    json.dump(filme, arquivo, ensure_ascii=False, indent=4)

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r', encoding='utf8') as arquivo:
    filme_do_json = json.load(arquivo)
    print(filme_do_json)
