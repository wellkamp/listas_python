# Exercicio 11


class Numeros():
    # Construtor
    def __init__(self, num_int_1, num_int_2, num_real):
        self._num_int_1 = int(num_int_1)
        self._num_int_2 = int(num_int_2)
        self._num_real = float(num_real)

    # Retorna numero inteiro 1
    @property
    def num_int_1(self):
        return self._num_int_1

    # Retorna numero inteiro 2
    @property
    def num_int_2(self):
        return self._num_int_2

    @property
    # Retorna numero Real
    def num_real(self):
        return self._num_real

    # Calculo A do exercicio
    def calculo_A(self):
        calculo = float((self.num_int_1 * 2) * (self.num_int_2 / 2))
        return calculo

    # Calculo B do exercicio
    def calculo_B(self):
        return (self.num_int_1 * 3) + self.num_real

    # Calculo C do exercicio
    def calculo_C(self):
        return self.num_real ** 3

    # Função para verificar os valores
    def get_nums(self):
        if self._num_int_1 is float:
            return False
        if self._num_int_2 is float:
            return False

    # Imprimir o objeto no console
    def __str__(self):
        str1 = f'\nNumero 1: {self._num_int_1}\nNumero 2: {self._num_int_2}\nNumero 3: {self._num_real}\n'
        str2 = f'\nCalculos:\nO produto do dobro do primeiro com metade do segundo: {self.calculo_A()}'
        str3 = f'\nA soma do triplo do primeiro com o terceiro: {self.calculo_B()}'
        str4 = f'\nO terceiro elevado ao cubo: {self.calculo_C()}'
        return str1 + str2 + str3 + str4
