from estrutura_sequencial.app_metro_p_c import MetroParaCentimetro


def main():
    sair = False
    while sair is False:
        try:
            valor = MetroParaCentimetro(
                input('Digite o valor para ser transformado em centimetros: '))
            if valor.valor > 0:
                print(valor)
                sair = True
            else:
                print('valor invalido')
        except ValueError:
            print('Digite um numero valido')


if __name__ == '__main__':
    main()
