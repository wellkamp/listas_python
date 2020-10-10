# Exercicio 2
from estrutura_sequencial.app_demonstrar_numero import Demonstrar_numero


def main():
    sair = False
    while sair is False:
        try:
            demonstrar_numero = Demonstrar_numero(
                input('Digite o numero para ser demonstrado: '))
            print(demonstrar_numero)
            sair = True
        except ValueError:
            print('Digite um numero válido! Não deixar em branco.')


if __name__ == '__main__':
    main()
