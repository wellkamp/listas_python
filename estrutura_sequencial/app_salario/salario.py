# Exercicio 8 e 15


class Salario:
    # Construtor
    def __init__(self, horas_trabalhadas, valor_hora):
        self.__horas_trabalhadas = horas_trabalhadas
        self.__valor_hora = valor_hora
        self.__imposto_renda = 0.11
        self.__inss = 0.08
        self.__sindicato = 0.05

    @property
    # Retorna o atributo horas trabalhadas
    def horas_trabalhadas(self):
        return float(self.__horas_trabalhadas)

    @property
    # Retorna o atributo valor de horas
    def valor_hora(self):
        return float(self.__valor_hora)

    @property
    # Retorna o atributo imposto de renda
    def imposto_renda(self):
        return float(self.__imposto_renda)

    @property
    # Retorna o atributo inss
    def inss(self):
        return float(self.__inss)

    @property
    # Retorna o atributo sindicato
    def sindicato(self):
        return float(self.__sindicato)


    # Faz o calculo do desconto do imposto de renda
    def salario_imposto_renda(self):
        return self.calculo_salario() - (self.calculo_salario() - (self.calculo_salario() * self.imposto_renda))

    # Faz o calculo do desconto do inss
    def salario_inss(self):
        return self.calculo_salario() - (self.calculo_salario() - (self.calculo_salario() * self.inss))


    # Faz o calculo do desconto do sindicato
    def salario_sindicato(self):
        return self.calculo_salario() - (self.calculo_salario() - (self.calculo_salario() * self.sindicato))

    # Faz o calculo do salario bruto
    def calculo_salario(self):
        return self.horas_trabalhadas * self.valor_hora

    # Faz o calculo do salario liquido
    def calculo_salario_liquido(self):
        return self.calculo_salario() - (self.salario_imposto_renda() + self.salario_inss() + self.salario_sindicato())

    # Valida os valores de entrada
    def validar_valores(self):
        if self.horas_trabalhadas < 0 or self.valor_hora < 0:
            return False

    # Imprimir o objeto no console
    def __str__(self):
        str1 = f'Salario Bruto: R$ {self.calculo_salario():.2f}'
        str2 = f'\n- Imposto de Renda (11%): R$ {self.salario_imposto_renda():.2f}'
        str3 = f'\n- INSS (8%): R$ {self.salario_inss():.2f}'
        str4 = f"\n- Sindicato (5%): R$ {self.salario_sindicato():.2f}"
        str5 = f'\n= Salário liquido : R$ {self.calculo_salario_liquido():.2f}'
        return (str1 + str2 + str3 + str4 + str5).replace('.', ',')
