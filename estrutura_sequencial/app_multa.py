# Exercicio 14

from estrutura_sequencial.app_peso_adicional import MultaPesoExcedente


def main():
    sair = False
    while sair is False:
        try:
            pesca = MultaPesoExcedente(input('Digite o peso do pescado: '))
            if pesca.get_peso >= 0:
                print(pesca)
                sair = True
            else:
                print('Digite um valor válido!')
        except ValueError:
            print('Digite os valores válidos!')


if __name__ == '__main__':
    main()
