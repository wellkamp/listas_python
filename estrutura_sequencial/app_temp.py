from estrutura_sequencial.app_temperatura import Temperatura


def main():
    sair = False
    while sair is False:
        try:
            temp = Temperatura(input('Digite o valor para ser convertido: '), input(
                '1 - Farenheit para Celsius.\n2 - Celsius para Fahrenheit. \n'))
            if temp.validar_valores() is not False:
                print(temp)
                sair = True
            else:
                print('Escolha opções válidas! 1 ou 2')
        except ValueError:
            print('Digite um valor válido!')


if __name__ == '__main__':
    main()
