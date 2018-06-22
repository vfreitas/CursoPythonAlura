def jogar():
    print("***************************\n"
          "-----  JOGO DA FORCA  -----\n"
          "***************************\n")

    palavra_secreta = "banana".upper()

    enforcou = False
    acertou = False
    erros = 0

    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    print("\nA palavra eh {}".format(letras_acertadas))

    while not enforcou and not acertou:
        chute = input("Informe a letra: ").strip().upper()
        print()

        if chute in palavra_secreta:
            posicao = 0

            for letra in palavra_secreta:

                if chute == letra:
                    print("Encontrei a letra {} na posicao {}!".format(chute, posicao))
                    letras_acertadas[posicao] = chute

                posicao = posicao + 1

        else:
            erros = erros + 1

        print("\n", letras_acertadas, "\n")
        enforcou = erros == 6


if __name__ == "__main__":
    jogar()
