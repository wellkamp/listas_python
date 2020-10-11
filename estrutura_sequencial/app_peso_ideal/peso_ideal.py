# Exercicio 12 e 13.


class PesoIdeal():
    # Construtor
    def __init__(self, sexo, altura):
        self.__altura = altura
        self.__sexo = sexo

    @property
    # Retorna altura
    def altura(self):
        return float(self.__altura)

    @property
    # Retorna o sexo
    def sexo(self):
        return float(self.__sexo)

    @property
    # Retorna o genero
    def genero(self):
        if self.sexo == 1:
            return 'Masculino'
        else:
            return 'Feminino'

    def validar_valores(self):
        if self.altura < 0:
            return False
        if self.sexo < 1 or self.sexo > 2:
            return False

    # Função que calcula o peso ideal
    def calcula_peso_ideal(self):
        if self.sexo == 1:
            return round((72.7 * self.altura) - 58, 1)
        else:
            return round((62.1 * self.altura) - 44.7, 1)

    # Imprimir no console o objeto
    def __str__(self):
        str1 = f'\nO peso ideal de uma pessoa com altura de {self.altura} metros e do sexo {self.genero} é {self.calcula_peso_ideal()}'
        return str1.replace('.', ',')
