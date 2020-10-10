# Exercicio 4


class Notas:
    # Construtor
    def __init__(self, notaA, notaB, notaC, notaD):
        self.__notaA = notaA
        self.__notaB = notaB
        self.__notaC = notaC
        self.__notaD = notaD

    @property
    # Retorna nota A
    def get_nota_A(self):
        return float(self.__notaA)

    @property
    # Retorna nota B
    def get_nota_B(self):
        return float(self.__notaB)

    @property
    # Retorna nota C
    def get_nota_C(self):
        return float(self.__notaC)

    @property
    # Retorna nota D
    def get_nota_D(self):
        return float(self.__notaD)

    # Função para verificar se alguma nota é invalida
    def validar_notas(self):
        if self.get_nota_A < 0 or self.get_nota_A > 10:
            return False
        if self.get_nota_B < 0 or self.get_nota_B > 10:
            return False
        if self.get_nota_C < 0 or self.get_nota_C > 10:
            return False
        if self.get_nota_D < 0 or self.get_nota_D > 10:
            return False

    # Função que retorna a Média das notas
    def media(self):
        return ((self.get_nota_A + self.get_nota_B + self.get_nota_C
                 + self.get_nota_D) / 4)

    # Imprimir no console o objeto
    def __str__(self):
        str1 = f'A média das notas {self.get_nota_A}, {self.get_nota_B}, {self.get_nota_C}, {self.get_nota_D} é: {round(self.media(), 1)}'
        return str1
