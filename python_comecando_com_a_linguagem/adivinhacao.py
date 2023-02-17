import random


def jogar():
    print('*************************************')
    print('* Bem-vindo ao jogo de adivinhação! *')
    print('*************************************')

    numero_secreto = random.randrange(1,101)

    print('\nQual a dificuldade do jogo?')
    print('(1) - Fácil\n(2) - Médio\n(3) - Difícil')
    nivel = int(input('Digite o nível desejado: '))
    pontos = 1000

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1,total_de_tentativas + 1):
        print('\nTentativa {} de {}'.format(rodada,total_de_tentativas))

        chute_str = input('Digite um número entre 1 e 100: ')
        chute = int(chute_str)

        # print('Seu número é',chute)

        if chute < 1 or chute > 100:
            print('Você não chutou um número entre 1 e 100 e perdeu uma tentativa!')
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        pontos_perdidos = abs(chute - numero_secreto)
        pontos = pontos - pontos_perdidos

        if acertou:
            print('Você acertou e fez {}!'.format(pontos))
            break
        elif maior:
            print('Você errou! Seu chute foi maior que o número secreto.')
        elif menor:
            print('Você errou! Seu chute foi menor que o número secreto.')

    print('\nFim de jogo.')
    print('O número secreto era {}.'.format(numero_secreto))


if __name__ == '__main__':
    jogar()