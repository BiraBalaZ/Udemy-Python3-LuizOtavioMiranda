# Exercício - Sistema de perguntas e respostas

perguntas = [
    {
        'pergunta': 'Quanto é 2+2?',
        'opções': ['1', '2', '3', '4', '5'],
        'resposta': '4',
     },
     {
        'pergunta': 'Quanto é 5*5?',
        'opções': ['25', '55', '10', '51'],
        'resposta': '25',
     },
     {
        'pergunta': 'Quanto é 10/2?',
        'opções': ['4', '5', '2', '1'],
        'resposta': '5',
     },
     {
        'pergunta': 'Quanto é 348-173?',
        'opções': ['150', '185', '175', '119', '235'],
        'resposta': '175',
     },
     {
        'pergunta': 'Dois zeros dois quatro?',
        'opções': ['2024', '0044', '0024', '2044'],
        'resposta': '0024',
     },
     {
        'pergunta': 'Uma pedra cumprimentou uma tora de madeira. Que horas são?',
        'opções': ['2:30', '7:45', '8:00', '1:45', '00:00'],
        'resposta': '8:00',
     },
     {
        'pergunta': 'Quanto é 10²',
        'opções': ['1000', '20', '10', '100'],
        'resposta': '100',
     },
     {
        'pergunta': 'Raiz quadrada de 81 é',
        'opções': ['3', '9', '18'],
        'resposta': '9',
     },
     {
        'pergunta': '15% de 380.000',
        'opções': ['57.000', '13.000', '42.000', '60.000', '73.500'],
        'resposta': '57.000',
     },
     {
        'pergunta': 'Se um evento começa às 14:30 e dura 2 horas e 45 minutos, a que horas o evento terminará?',
        'opções': ['17:00', '17:15', '16:15', '15:15', '17:30'],
        'resposta': '16:15',
     },
]

num = 0
pergunta = 0
questao = 1
acertadas = 0

for x in perguntas:
    print(f'{questao}. {perguntas[pergunta]['pergunta']}')

    for i in perguntas[pergunta]['opções']:
        print(f'{num}) {i}')
        num += 1

    while True:
        resposta = input('Escolha uma opção: ')

        if resposta not in ('1234567890'):
            continue
        else:
            break

    try:
        if perguntas[pergunta]['opções'][int(resposta)] == perguntas[pergunta]['resposta']:
            print('Acertou! ✅')
            acertadas += 1
        else:
            print('Errou ❌')
    except:
        print('Errou ❌')

    num = 0
    pergunta += 1
    questao += 1

print(f'Você acertou {acertadas}/{len(perguntas)} perguntas.')
