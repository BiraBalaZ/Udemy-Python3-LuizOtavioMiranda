# groupby - Agrupar valores (itertools)
from itertools import groupby

alunos = [
    {'nome': 'Erick',    'nota': 'B'},
    {'nome': 'Sarah',    'nota': 'A'},
    {'nome': 'Erik',     'nota': 'A'},
    {'nome': 'Fernanda', 'nota': 'B'},
    {'nome': 'Victória', 'nota': 'C'},
    {'nome': 'Larissa',  'nota': 'B'},
    {'nome': 'Tonhão',   'nota': 'B'},
    {'nome': 'Gustavo',  'nota': 'B'},
    {'nome': 'Jamilly',  'nota': 'C'},
    {'nome': 'Dacyla',   'nota': 'F'},
    {'nome': 'Beatriz',  'nota': 'C'},
    {'nome': 'Thiago',   'nota': 'D'},
    {'nome': 'Rafael',   'nota': 'A'},
    {'nome': 'Giovana',  'nota': 'B'},
]

def ordena(aluno):
    return aluno['nota']

alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados, key=ordena)


for chave, grupo in grupos:
    print(f'\n[Nota: {chave}]')
    for aluno in grupo:
        print(f'> {aluno['nome']}')
