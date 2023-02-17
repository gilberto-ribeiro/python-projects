import adivinhacao
import forca


def selecionar_jogo():
    print('*******************************')
    print('* Bem-vindo à seção de jogos! *')
    print('*******************************')

    print('Selecione o jogo que deseja jogar:')
    print('(1) - Adivinhação\n(2) - Forca')
    jogo = int(input('Digite o código do jogo: '))

    if jogo == 1:
        adivinhacao.jogar()
    elif jogo == 2:
        forca.jogar()


if __name__ == '__main__':
    selecionar_jogo()