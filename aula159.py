# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass, field

@dataclass
class Pessoa:
    nome: str = field(default="Fulano") # "Fulano"
    sobrenome: str = field(default="de Tal") # "de Tal"
    idade: int = field(default='???')
    enderecos: list[str] = field(default_factory=list)


if __name__ == '__main__':
    p1 = Pessoa('Erick', 'Monteiro dos Anjos', 21, ['R. Moreira e Costa, 21', 'R. Prof. Arnaldo João Semeraro, 730'])
    p2 = Pessoa(enderecos=['Lugar Nenhum'])

    def show_message(person):
        print(f'\n{person.nome} {person.sobrenome} tem {person.idade} anos.')
        print('Seus endereços são:')
        for endereco in person.enderecos:
            print(endereco)
    
    show_message(p1)
    show_message(p2)
