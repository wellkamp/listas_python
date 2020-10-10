# Exercicio 3


class Soma:
    # Construtor
    def __init__(self, numA, numB):
        self.__numA = numA
        self.__numB = numB

    # Retorna o calculo dos dois atributos
    def soma(self):
        return float(self.numA) + float(self.numB)

    # Imprimir no console o objeto
    def __str__(self):
        return f'A soma de {self.numA} + {self.numB} é igual a: {self.soma()}'
