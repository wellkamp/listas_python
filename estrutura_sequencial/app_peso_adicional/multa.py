# Exercicio 14


class MultaPesoExcedente():
    # Construtor
    def __init__(self, peso):
        self.__peso = peso
        self.__multa = 4
        self.__excedente = 0

    @property
    # Retorna o peso
    def peso(self):
        return float(self.__peso)

    @property
    # Retorna o valor da multa
    def multa(self):
        return float(self.__multa)

    @property
    # Retorna o valor do peso excedente
    def peso_excedente(self):
        return float(self.__excedente)

    @peso_excedente.setter
    # Muda o valor do peso excedente
    def peso_excedente(self, excedente):
        self.__excedente = excedente


    '''
    Retorna o calculo da multa se o valor do peso excedente for maior que 50.
    A função pega o peso passado diminui de 50 depois multiplica o peso excedente
    pelo valor para gerar o preço da multa
    '''

    def calcula_excedente(self):
        if self.peso > 50:
            self.peso_excedente = self.peso - 50
            return round(self.peso_excedente * self.multa, 2)

    # Imprimir no console o objeto
    def __str__(self):
        if self.peso > 50:
            str1 = f'O valor a pagar de multa é {self.calcula_excedente()}0 Reais e o peso excedido foi {self.peso_excedente} kg'
        else:
            str1 = f'Peso dentro do padrão'
        return str1.replace('.', ',')
