"""Este é um módulo de exemplo

Este módulo contém funções e exemplos de documentação de funções.
A função soma você já conhece bastante.
"""
variavel_1 = 1


# def soma(x: int | float, y: int | float) -> int | float:
def soma(x, y, show_count = 0):
    """
    Soma x e y

    :param x: Número 1
    :type x: int or float
    :param y: Número 2
    :type y: int or float
    :param show_count: 0, 1 
    :type show_count: bool
    
    :return: A soma entre x e y
    :rtype: int or float
    """
    if show_count == 1:
        return f'{x} + {y} = {x+y}'
    return x + y


def multiplica (
        x: int | float,
        y: int | float,
        z: int | float | None = None
) -> int | float:
    """Multiplica x, y e/ou z
    
    Multiplica x e y. Se z for enviado, multiplica x, y , z.
    """
    if z is None:
        return x * y
    return x * y * z


variavel_2 = 2
variavel_3 = 3
variavel_4 = 4
