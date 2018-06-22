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
            print("A palavra NAO tem esta letra!")
            erros = erros + 1

        enforcou = erros == 6

        if not "_" in letras_acertadas:
            print("\n\nVOCE GANHOU!!")
            break
        elif erros == 6:
            print("\n\nVOCE PERDEU!!")

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
    print("ERROS: {} de 6".format(erros))
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


if __name__ == "__main__":
    jogar()
