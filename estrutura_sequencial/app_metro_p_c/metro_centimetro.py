class MetroParaCentimetro:
    # Construtor
    def __init__(self, valor):
        self.__valor = float(valor)

    @property
    # Retorna o atributo valor
    def get_valor(self):
        return self.__valor

    # Converte metro(s) para centimentros
    def transformar(self):
        return self.get_valor * 100

    # Imprimir no console o objeto
    def __str__(self):
        return f'{self.__valor} metro(s) em centrimetros são: {self.transformar()} centimetros'
