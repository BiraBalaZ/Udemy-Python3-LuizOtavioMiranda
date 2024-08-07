# dir, hasttr e getattr em Python
string = 'Erick'
print(string)

print(dir(string)) # Listando todos os métodos
print(hasattr(string, 'upper')) # verificando se existe o metodo upper() >>> True

# Se tentarmos escrever por exemplo:
string = 'Erick'
metodo = 'upper'

if hasattr(string, metodo):
    print(f'Existe o método {metodo}')
    print(string.metodo()) # isso não irá funcionar. O Python está 
                           # procurando a stringupper ao inves do metodo upper


# Aí entra o getattr();
string = 'Erick'
metodo = 'upper'

if hasattr(string, metodo):
    print(f'Existe o método {metodo}')
    print(getattr(string, metodo)())
else:
    print(f'Não existe o método {metodo}')
