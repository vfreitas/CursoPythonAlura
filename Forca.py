import random


def jogar():
    imprime_cabecalho()

    define_palavra_secreta()
    palavra_secreta = define_palavra_secreta()

    enforcou = False
    acertou = False
    erros = 0

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    print("\nA palavra eh {}".format(letras_acertadas))

    while not enforcou and not acertou:
        chute = pede_chute(erros)

        if chute in palavra_secreta:
            marca_chute_correto(chute, palavra_secreta, letras_acertadas)
        else:
            print("A palavra NAO tem esta letra!\n")
            desenha_forca(erros)
            erros = erros + 1

        enforcou = erros == 9

        if not "_" in letras_acertadas:
            imprime_ganhador()
            break
        elif erros == 9:
            imprime_perdedor(palavra_secreta)

        print("\n", letras_acertadas, "\n")


def imprime_cabecalho():
    print("***************************\n"
          "-----  JOGO DA FORCA  -----\n"
          "***************************\n")


def define_palavra_secreta():
    palavras = []

    arquivo = open("palavras.txt", "r")

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def pede_chute(erros):
    print("ERROS: {} de 8".format(erros))
    chute = input("Informe a letra: ").strip().upper()
    print()
    return chute


def marca_chute_correto(chute, palavra_secreta, letras_acertadas):
    posicao = 0

    for letra in palavra_secreta:

        if chute == letra:
            print("Encontrei a letra {} na posicao {}!".format(chute, posicao))
            letras_acertadas[posicao] = chute

        posicao = posicao + 1


def imprime_ganhador():
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

def imprime_perdedor(palavra_secreta):
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
        print(" |      \     ")
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

if __name__ == "__main__":
    jogar()
