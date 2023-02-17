import random


def resultado_por_rodada(selecao_do_jogador, selecao_do_computador, pontuacao_jogador, pontuacao_computador):
    alternativas = {'pedra': (0, 2), 'papel': (1, 0), 'tesoura': (2, 1)}
    valor_do_jogador = alternativas[selecao_do_jogador]
    valor_do_computador = alternativas[selecao_do_computador]
    print('Você jogou {} e o computador jogou {}.'.format(selecao_do_jogador, selecao_do_computador))
    if valor_do_jogador[0] == valor_do_computador[1]:
        print('Você perdeu esta rodada! {} ganha de {}!'.format(selecao_do_computador.capitalize(), selecao_do_jogador))
        pontuacao_computador += 1
    elif valor_do_jogador[1] == valor_do_computador[0]:
        print('Você ganhou esta rodada! {} ganha de {}!'.format(selecao_do_jogador.capitalize(), selecao_do_computador))
        pontuacao_jogador += 1
    else:
        print('Ocorreu um empate nesta rodada!')
    return pontuacao_jogador, pontuacao_computador


def entrada():
    alternativas = ('pedra', 'papel', 'tesoura')
    while True:
        selecao_do_jogador = input('Insira sua opção: ').lower()
        if selecao_do_jogador in alternativas:
            break
    selecao_do_computador = alternativas[random.randint(0, 2)]
    return selecao_do_jogador, selecao_do_computador


def jogo(numero_de_rodadas):
    rodada_de_vitoria = numero_de_rodadas // 2 + 1
    pontuacao_jogador = 0
    pontuacao_computador = 0
    for rodada in range(numero_de_rodadas):
        print('\n>>> RODADA {} <<<'.format(rodada + 1))
        selecao_do_jogador, selecao_do_computador = entrada()
        pontuacao_jogador, pontuacao_computador = resultado_por_rodada(selecao_do_jogador, selecao_do_computador, pontuacao_jogador, pontuacao_computador)
        if pontuacao_jogador == rodada_de_vitoria:
            print('\nVOCÊ GANHOU EM {} RODADAS!!!'.format(rodada + 1))
            break
        elif pontuacao_computador == rodada_de_vitoria:
            print('\nVOCÊ PERDEU EM {} RODADAS!!!'.format(rodada + 1))
            break
        elif rodada == numero_de_rodadas - 1 and (pontuacao_computador < rodada_de_vitoria or pontuacao_jogador < rodada_de_vitoria):
            print('\nO JOGO TERMINOU EM EMPATE!')
    print('\n>>> FIM DE JOGO <<<\n')


jogo(9)