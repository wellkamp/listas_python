from estrutura_sequencial.app_circulo import Circulo


def main():
    sair = False
    while sair is False:
        try:
            circ = Circulo(input('Digite o valor do raio: '))
            if circ.validar_dados() is not False:
                print(circ)
                sair = True
            else:
                print('Valor inválido! Não deixar em branco ou digitar número negativo.')
        except ValueError:
            print('Valor inválido! Não deixar em branco ou digitar número negativo.')


if __name__ == '__main__':
    main()
