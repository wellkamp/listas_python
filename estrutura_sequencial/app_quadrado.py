# Exercicio 7

from estrutura_sequencial.app_quadrado import Quadrado


def main():
    sair = False
    while sair is False:
        try:
            areaQuadrado = Quadrado(input('Digite a base do quadrado: '),
                                    input('Digite a altura do quadrado: '))
            if areaQuadrado.validar_valores() is not False:
                print(areaQuadrado)
                sair = True
            else:
                print(
                    'Valor inválido! Não deixar em branco e digitar valores positivos.')
        except ValueError:
            print('Valor inválido! Não deixar em branco e digitar valores positivos.')


if __name__ == '__main__':
    main()
