# Exercicio 2


class Demonstrar_numero:
    def __init__(self, numero):
        self.__numero = float(numero)

    @property
    # Retorna o atributo numero
    def numero(self):
        return self.__numero

    # Imprimir no console o objeto
    def __str__(self):
        str1 = f'O número digitado foi {self.numero}'
        return str1
