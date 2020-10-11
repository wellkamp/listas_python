# Exercicio 7


class Quadrado:
    # Construtor
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    @property
    # Retornar atributo base
    def base(self):
        return float(self.__base)

    @property
    # Retornar atributo altura
    def altura(self):
        return float(self.__altura)

    # Função para validar valores
    def validar_valores(self):
        if self.base < 0 or self.altura < 0:
            return False

    # Calculo da area
    def area(self):
        return self.base * self.altura

    # Calculo do dobro da area
    def dobro_area(self):
        return self.area() * 2

    # Imprimir o objeto no console
    def __str__(self):
        return f'O quadrado com {self.base} de base e {self.altura} de altura possui área de {self.area()} e o dobro da sua area é {self.dobro_area()}'
