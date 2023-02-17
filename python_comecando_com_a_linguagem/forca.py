import random


def jogar():

    imprime_mensagem_inicial()

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = len(palavra_secreta) * ['_']

    acertou = False
    enforcou = False
    erros = 0
    erros_max = 7

    while not enforcou and not acertou:

        chute = solicita_chute()

        if chute in palavra_secreta:
            captura_chute_correto(palavra_secreta, letras_acertadas, chute)
        else:
            erros += 1
            desenha_forca(erros)
            # imprime_quantidade_de_erros(erros, erros_max)
        
        print('\n'+' '.join(letras_acertadas))

        enforcou = erros == erros_max
        acertou = '_' not in letras_acertadas

    imprime_mensagem_final(palavra_secreta, acertou)
    
    print('\nFim de jogo!')


def imprime_mensagem_final(palavra_secreta, acertou):
    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_quantidade_de_erros(erros, erros_max):
    if erros_max - erros == 1:
        print('\nVocê pode errar ainda {:d} vez.'.format(erros_max - erros))
    elif erros_max - erros > 1:
        print('\nVocê pode errar ainda {:d} vezes.'.format(erros_max - erros))


def captura_chute_correto(palavra_secreta, letras_acertadas, chute):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1


def solicita_chute():
    chute = input('\nInsira uma letra para seu chute: ')
    chute = chute.strip().upper()
    return chute


def carrega_palavra_secreta(file='palavras.txt'):
    with open(file, 'r') as arquivo:
    # arquivo = open('palavras.txt', 'r')
        palavras = [linha.strip() for linha in arquivo]
    # arquivo.close()
    palavra_secreta = palavras[random.randrange(len(palavras))].upper()
    return palavra_secreta


def imprime_mensagem_inicial():
    print('\n*******************************')
    print('* Bem-vindo ao jogo de forca! *')
    print('*******************************')
 

if __name__ == '__main__':
    jogar()