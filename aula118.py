# Problema dos parâmetros mutáveis em funções Python
def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = adiciona_clientes('Erick')
adiciona_clientes('Sarah', cliente1)
adiciona_clientes('Fernanda', cliente1)
cliente2 = adiciona_clientes('Victória')
adiciona_clientes('Larissa', cliente2)
adiciona_clientes('Erik', cliente2)

print(cliente1)
print(cliente2)
