# Exercicio 7


class Quadrado:
    # Construtor
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    @property
    # Retornar atributo base
    def get_base(self):
        return float(self.__base)

    @property
    # Retornar atributo altura
    def get_altura(self):
        return float(self.__altura)

    # Função para validar valores
    def validar_valores(self):
        if self.get_base < 0 or self.get_altura < 0:
            return False

    # Calculo da area
    def area(self):
        return self.get_base * self.get_altura

    # Calculo do dobro da area
    def dobro_area(self):
        return self.area() * 2

    # Imprimir o objeto no console
    def __str__(self):
        return f'O quadrado com {self.get_base} de base e {self.get_altura} de altura possui área de {self.area()} e o dobro da sua area é {self.dobro_area()}'
