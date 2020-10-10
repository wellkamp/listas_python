# Exercicio 3

from estrutura_sequencial.app_soma import Soma


def main():
    sair = False
    while sair is False:
        try:
            soma = Soma(input('Coloque o valor de A: '),
                        input('Coloque o valor de B: '))
            print(soma)
            sair = True
        except ValueError:
            print('Digite um numero valido')


if __name__ == '__main__':
    main()
