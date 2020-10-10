# Exercicio 1


class Hello:
    # Construtor
    def __init__(self, hello):
        self.__hello = hello

    @property
    # Retorna o atributo hello
    def get_hello(self):
        return self.__hello

    # Imprimir no console o objeto
    def __str__(self):
        return self.get_hello
