# Exercicio 16 e 17 juntos. A letra 'C' não consegui fazer/entender

from math import ceil as round_up

# Variaveis que serão constantes
LATA_LITROS = 18
LITRO_METRO_QUADRADO = 6
PRECO_TINTA = 80
PRECO_GALAO_TINTA = 25
LITRO_GALAO = 3.6


class LojaTintas():
    # Construtor
    def __init__(self, metros_quadrados):
        self.__metros_quadrados = float(metros_quadrados)

    @property
    # Retorna o valor de metros quadrados
    def metros_quadrados(self):
        return self.__metros_quadrados

    # Cacula a quantidade de litros de tinta que irá usar por metro quadrado
    def calculo_litros_metros(self):
        return round(self.metros_quadrados / LITRO_METRO_QUADRADO, 2)

    # Calcula quantas latas de tinta irá precisar
    def calculo_lata_tinta(self):
        return round_up(self.calculo_litros_metros() / LATA_LITROS)

    # Calcula o preço total pago pelo cliente lata
    def calculo_preco_lata(self):
        return self.calculo_lata_tinta() * PRECO_TINTA

    # Calcula o número de galões de tinta necessarios
    def calculo_galoes_tinta(self):
        return round_up(self.calculo_litros_metros() / LITRO_GALAO)

    # Caculo o preço total pago pelo cliente galão
    def preco_por_galao(self):
        return self.calculo_galoes_tinta() * PRECO_GALAO_TINTA

    # Função para validar dados
    def validar_dados(self):
        if self.metros_quadrados < 0:
            return False

    # Imprimir no console o objeto
    def __str__(self):
        str1 = f'Litros de tinta: {self.calculo_litros_metros()}'
        str2 = f'\nLatas de tinta: {self.calculo_lata_tinta()}'
        str3 = f'\nPreço total a ser pago somente lata: R$ {self.calculo_preco_lata()}'.replace(
            '.', ',')
        str4 = f'\nGalões de tinta: {self.calculo_galoes_tinta()}'
        str5 = f'\nPreço total a ser pago somente galão: R$ {self.preco_por_galao()}'.replace(
            '.', ',')
        return str1 + str2 + str3 + str4 + str5
