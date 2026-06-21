"""
Serviços de cálculo de áreas geométricas.
Contém apenas regras de negócio.
"""


def area_triangulo(base, altura):
    """
    Área do triângulo = (base * altura) / 2
    """
    return (base * altura) / 2


def area_trapezio(base_maior, base_menor, altura):
    """
    Área do trapézio = ((B + b) * h) / 2
    """
    return ((base_maior + base_menor) * altura) / 2


def area_retangulo(base, altura):
    """
    Área do retângulo = base * altura
    """
    return base * altura


def area_losango(diagonal_maior, diagonal_menor):
    """
    Área do losango = (D * d) / 2
    """
    return (diagonal_maior * diagonal_menor) / 2