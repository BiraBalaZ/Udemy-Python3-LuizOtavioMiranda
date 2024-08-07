'''
Faça um jogo para o usuario adivinhar qual a palavra secreta.
- Voce vai propor uma palavra secreta qualquer e vai dar a
possibilidade para o usuario digitar apenas uma letra.
- Qual o usuario digitar uma letra, voce vai conferir se a
letra digitada esta na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada nao estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuario.
'''
from os import system
from random import choice
from time import sleep

lista = ['perfume', 'amor', 'tecnologia', 'matematica', 'tempo', 'destino', 'nunca', 'sempre', 'quadrilha', 'dança', 'escola', 'copo', 'televisao', 'computador', 'teclado', 'mouse', 'garrafa', 'liquido', 'bengala', 'estante', 'quadro', 'cadeira', 'mesa', 'lixeira', 'guitarra', 'violao', 'casaco', 'camiseta', 'calçado', 'furia', 'cuidado', 'tomada', 'luminaria', 'parede', 'livraria', 'condominio', 'estrada', 'muralha', 'aprendizado', 'vidraça', 'musica', 'castigo', 'acontecer', 'acostumado', 'adentrar', 'assinar', 'trazer', 'jogatina', 'adormecer', 'comercializar', 'amargura', 'necessitar', 'liberdade', 'dirigir', 'segurança', 'suficiente', 'desaparecer', 'miragem', 'escalar', 'sonhar', 'universo', 'estilizar', 'responder', 'existir', 'desistir', 'solidao', 'tropeçar', 'acordar', 'aberto', 'afogar', 'nascer', 'morrer', 'revelar', 'inveja', 'gula', 'luxuria', 'ira', 'vaidade', 'ganancia', 'desespero', 'desejo', 'perpetuo', 'diamante', 'rubi', 'bloco', 'esmeralda', 'colar', 'tristeza', 'divertido', 'felicidade', 'raiva', 'medo', 'bagunça', 'organizaçao', 'vermelho', 'branco', 'preto', 'amarelo', 'azul', 'roxo', 'fogueira', 'purpura', 'escrever', 'apagar', 'errar', 'humano', 'cachorro', 'hipopotamo', 'mosquito', 'revisar', 'rapidez', 'lerdeza', 'concentrar', 'brincar', 'negaçao', 'afirmaçao', 'tapete', 'exaustao', 'simplesmente', 'pertencer', 'poder', 'dispensa', 'geladeira', 'surpresa', 'passar', 'teste', 'quadrado', 'encaixotar', 'planeta', 'sistema', 'navegar', 'espaçonave', 'decolar', 'ensopado', 'pescaria', 'carpintaria', 'linguado', 'atum', 'edificio', 'iluminaçao', 'escuridao', 'decepçao', 'problematico', 'existencia', 'especialidade', 'santificado', 'interesse', 'volante', 'comoda', 'enviar', 'professora', 'audiencia', 'sacrificar', 'estudar', 'escutar', 'palestra', 'agradecer', 'metade', 'inicio', 'completamente', 'expulsar', 'convidar', 'amaldiçoado', 'abandonar', 'torcer', 'dinheiro', 'festival', 'apos', 'sinceridade', 'internar', 'interno', 'externo', 'corroer', 'apodrecer', 'esforçar', 'aprender', 'embora', 'direito', 'amedrontar', 'receio', 'clareza', 'serenata', 'regras', 'regime', 'ditadura', 'teimosia', 'disciplina', 'selvagem', 'choramingar', 'escandalo', 'assustado', 'implorar', 'fracasso', 'culpa', 'extremamente', 'orgulho', 'contar', 'conceito', 'conhecimento', 'multidao', 'amontoar', 'empilhar', 'satira', 'ruindade', 'maldade', 'trocar', 'perturbar', 'independencia', 'tampouco', 'aroma', 'odor', 'procurar', 'esperar', 'perder', 'demonstrar', 'coraçao', 'novidade', 'antiguidade', 'listrado', 'distraçao', 'olhar', 'triangulo', 'escovar', 'agredir']

palavra_secreta = choice(lista)
letras_acertadas = ''

invalidos = ''' 01234567890-_=+?/\|~^´`[{()]}*&¨%$#'@"!,.<>;:eéóòèààíìúùâãôõ'''
validos = 'abcdefghijklmniopqrstuvwxyzç'
tentativas = 0
nota = ''

system('cls')
sleep(2)
print('\033[36mEu escolhi uma palavra...')
sleep(2)
print(f'Ela tem {len(palavra_secreta)} letras.')
sleep(2)
print('Tente adivinhar!\033[m')
sleep(2)
print('\033[30m-\033[m'*(15 + len(palavra_secreta)))
print('Palavra:', '*'*len(palavra_secreta), '\n')

while True:
    letra = input(str('Digite uma letra: ')).lower()

    if len(letra) > 1:
        print('\033[31mVoce precisa digitar apenas uma letra!\033[m')
        continue

    if letra in palavra_secreta:
        print(f'\033[32mA letra "{letra}" esta na palavra!\033[m')
        letras_acertadas += letra
        tentativas += 1
    elif letra in invalidos:
        print(f'\033[33m"{letra}" Nao e um caractere valido.\033[m')
    else:
        print(f'\033[31mA letra "{letra}" NÃO esta na palavra!\033[m')
        tentativas += 1

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        system('cls')
        print('\033[35mPARABeNS! VOCÊ GANHOU!\033[m\n')
        print(f'A palavra secreta era: \033[36m{palavra_secreta}\033[m.')
        print(f'Você precisou de {tentativas} tentativas.\n')

        if tentativas <= 14:
            nota = '⭐⭐⭐'
        elif tentativas > 14 and tentativas <= 20:
            nota = ' ⭐⭐ '
        else:
            nota = '  ⭐  '

        print(f'\033[33mPONTUAÇÃO: {nota}\033[m')
        break
