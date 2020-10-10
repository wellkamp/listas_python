from estrutura_sequencial.app_peso_ideal import PesoIdeal

# Exercicio 12 e 13.


def main():
    sair = False
    try:
        while sair is False:
            peso_ideal = PesoIdeal(input('Digite 1 = Masculino ou 2 = feminino: '),
                                   input('Digite a sua altura em metros: '))

            if peso_ideal.validar_valores() is not False:
                print(peso_ideal)
                sair = True
            else:
                print(
                    'Valor invalido! Só é permitido os valores descritos e alturas positivas.')
    except ValueError:
        print('Valor invalido! Só é permitido os valores descritos e alturas positivas.')


if __name__ == '__main__':
    main()
