# Exercicio 6
from math import pi as PI


class Circulo:

    # Construtor
    def __init__(self, raio):
        self.__raio = float(raio)

    @property
    # Retorna o valor do atributo raio
    def raio(self):
        return self.__raio

    # Calcula area
    def area(self):
        return round(PI * self.__raio ** 2, 2)

    # Calcula a diâmetro
    def diametro(self):
        return round(self.__raio * 2, 2)

    # Calcula a circunferência
    def circunferencia(self):
        return round(PI * self.diametro(), 2)

    def validar_dados(self):
        if self.__raio < 0:
            return False

    # Imprimir no console o objeto
    def __str__(self):
        str1 = f'O raio deste circulo é: {self.__raio}.\nÁrea: {self.area()}.\nDiâmetro: {self.diametro()}.\nCircuferência: {self.circunferencia()}'
        return str1
