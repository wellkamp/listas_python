# Exercicio 4
from estrutura_sequencial.app_notas import Notas


def main():
    sair = False
    while sair is False:
        try:
            print('Digite valores válidos entre 0 e 10.\n')
            notaAluno = Notas(input('Digite a primeira nota: '), input('Digite a segunda nota: '), input(
                'Digite a terceira nota: '), input('Digite a quarta nota: '))
            if notaAluno.validar_notas() is not False:
                print(notaAluno)
                sair = True
            else:
                print('Digite uma nota valida! Valores entre 0 e 10')
        except ValueError:
            print('Digite uma nota valida! Valores entre 0 e 10')


if __name__ == '__main__':
    main()
