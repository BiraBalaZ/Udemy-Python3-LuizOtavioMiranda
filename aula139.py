# super() é a classe na sub classe
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class 
# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         return super().upper()


# nome = MinhaString('Erick')
# print(nome.upper())

class A:
    atributo_a = 'Valor A'
    
    def metodo(self):
        print('A')


class B(A):
    atributo_b = 'valor B'
    
    def metodo(self):
        print('B')


class C(B):
    atributo_c = 'valor C'
    
    def metodo(self):
        super().metodo()        # B
        super(B, self).metodo() # A
        print('C')


c = C()
print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
c.metodo()
