# Exercicio 9 e 10 juntos.


class Temperatura:
    # Construtor
    def __init__(self, temperatura, tipo_temp):
        self.__temperatura = temperatura
        self.__tipo_temp = tipo_temp

    @property
    # Retorna valor da temperatura
    def temperatura(self):
        return float(self.__temperatura)

    @property
    # Retorna a escolha de conversão
    def tipo_temperatura(self):
        return int(self.__tipo_temp)

    @property
    # Retorna o nome da temperatura
    def nome_temperatura(self):
        if self.tipo_temperatura == 1:
            return 'Celsius'
        else:
            return 'Fahrenheit'

    # Faz o calculo de conversão
    def converter_temperatura(self, valor):
        if valor == 1:
            return round(5 * ((self.temperatura - 32) / 9), 3)
        else:
            return round((self.temperatura * (9/5)) + 32, 3)

    # Função para retornar valores
    def validar_valores(self):
        if self.tipo_temperatura < 1 or self.tipo_temperatura > 2:
            return False

    # Imprimir o objeto no console
    def __str__(self):
        str1 = f'\nTemperatura convertida: {round(self.converter_temperatura(self.tipo_temperatura), 3)} graus {self.nome_temperatura}'
        return str1
