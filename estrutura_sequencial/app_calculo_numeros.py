# Exercicio 11
from Estrutura_sequencial.app_calculo_numeros import Numeros


def main():
    sair = False
    while sair is False:
        try:
            print('Digite na seguinte ordem os números -> Inteiro, Inteiro e Real.')
            calculo_numeros = Numeros(input('Digite numero 1: '), input(
                'Digite numero 2: '), input('Digite numero 3: '))
            if calculo_numeros.get_nums() is not False:
                print(calculo_numeros)
                sair = True
            else:
                print('\nvalor invalido')
        except ValueError:
            print('\nDigite um numero valido')


if __name__ == '__main__':
    main()
