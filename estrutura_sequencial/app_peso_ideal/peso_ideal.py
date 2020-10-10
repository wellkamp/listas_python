# Exercicio 12 e 13.


class PesoIdeal():
    # Construtor
    def __init__(self, sexo, altura):
        self.__altura = altura
        self.__sexo = sexo

    @property
    # Retorna altura
    def get_altura(self):
        return float(self.__altura)

    @property
    # Retorna o sexo
    def get_sexo(self):
        return float(self.__sexo)

    @property
    # Retorna o genero
    def get_genero(self):
        if self.get_sexo == 1:
            return 'Masculino'
        else:
            return 'Feminino'

    def validar_valores(self):
        if self.get_altura < 0:
            return False
        if self.get_sexo < 1 or self.get_sexo > 2:
            return False

    # Função que calcula o peso ideal
    def calcula_peso_ideal(self):
        if self.get_sexo == 1:
            return round((72.7 * self.get_altura) - 58, 1)
        else:
            return round((62.1 * self.get_altura) - 44.7, 1)

    # Imprimir no console o objeto
    def __str__(self):
        str1 = f'\nO peso ideal de uma pessoa com altura de {self.get_altura} metros e do sexo {self.get_genero} é {self.calcula_peso_ideal()}'
        return str1.replace('.', ',')
