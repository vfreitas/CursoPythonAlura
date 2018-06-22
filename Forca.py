def jogar():
    print("***************************\n"
          "-----  JOGO DA FORCA  -----\n"
          "***************************\n")

    palavra_secreta = "banana".upper()

    enforcou = False
    acertou = False
    erros = 0

    letras_acertadas = ["_" for letra in palavra_secreta]

    print("\nA palavra eh {}".format(letras_acertadas))

    while not enforcou and not acertou:
        print("Tentativa {} de 6".format(erros+1))
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
            print("A palavra NAO tem esta letra!")
            erros = erros + 1

        enforcou = erros == 6

        if not "_" in letras_acertadas:
            print("\n\nVOCE GANHOU!!")
            break
        elif erros == 6:
            print("\n\nVOCE PERDEU!!")


        print("\n", letras_acertadas, "\n")


if __name__ == "__main__":
    jogar()
