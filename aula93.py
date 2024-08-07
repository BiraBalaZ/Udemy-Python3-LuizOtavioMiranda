# Try, except, else e finally

try:
    a = 18
    b = 0
    print('Hello There'[100])
    c = a / b
except ZeroDivisionError:
    print('Você tentou dividir por zero.')
except NameError:
    print('Alguma variável não está definida')
except (TypeError, IndexError) as error:
    print('Erro de endereço variável[??]')
    print('MSG:', error)
    print('Nome:', error.__class__.__name__)
except Exception:
    print('ERRO DESCONHECIDO')
