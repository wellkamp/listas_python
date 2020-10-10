# Exercicio 16 e 17


from Estrutura_sequencial.app_loja_tintas import LojaTintas


def main():
    sair = False
    while sair is False:
        try:
            calculo_tintas = LojaTintas(input('Digite o valor em m²: '))
            if calculo_tintas.validar_dados() is not False:
                print(calculo_tintas)
                sair = True
            else:
                print('Digite um número válido em branco ou negativo não será aceito!')
        except ValueError:
            print('Digite um número válido em branco ou negativo não será aceito!')


if __name__ == '__main__':
    main()
