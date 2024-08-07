# Listas em Python
# Tipo list - Mutável
# Suporta vários valores de qualquer tipo
# Conhecimentos reutilizáveis - índices e fatiamento

# Métodos úteis: 
#     append - Adiciona um item ao final;
#     insert - Adicionaum item no índice escolhido;
#     pop - Remove do final ou índice escolhido;
#     del - Apaga um índice;
#     clear - Limpa a lista;
#     extend - Estende a lista;
#     + - concatena listas

# Create Read Update Delete
# Criar, ler, alterar, apagar = lista[i] (CRUD)

"""
O programa precisa de duas listas, uma vazia e uma com os numeros.
Ele pega o ultimo item e checa se ele ja existe nas posições disponiveis

Se sim o programa para e retorna o numero repetido

Se nao, o item é inserido normalmente na lista.
"""

a = [2, 1, 3, 5, 3, 2]

def dentroDe(lista):
    numero_atual = 0
    numero_verificar = 0
    verificados = []
    repetido = 0
    i = len(lista)

    while i > 0:
        print(lista)
        print(verificados)
        numero_atual = lista.pop(0)

        if len(verificados) > 0:
            while len(verificados) > 0:
                if numero_atual == verificados[0]:
                    repetido = numero_atual
                    break
                else:
                    verificados.append(numero_atual)
                    repetido = -1
        else:
            verificados.append(numero_atual)
        
        i -= 1

    print(repetido)

dentroDe(a)