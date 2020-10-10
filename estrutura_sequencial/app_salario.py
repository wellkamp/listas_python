from Estrutura_sequencial.app_salario import Salario

# Exericicio 8 e 15


def main():
    sair = False
    while sair is False:
        try:
            salario = Salario(input('Quantas horas você trabalhou este mês?: '),
                              input('Quanto você ganhar por hora trabalhada?: '))
            if salario.validar_valores() is not False:
                print(salario)
                sair = True
            else:
                print('Valor invalido! Só é permitido valores positivos.')
        except ValueError:
            print('Valor invalido! Só é permitido valores positivos.')


if __name__ == '__main__':
    main()
