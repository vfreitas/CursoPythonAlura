def jogar():
    print("JOGO DA FORCA\n"
          "*************")

    palavra_secreta = "banana"

    enforcou = False
    acertou  = False

    letras_acertadas = ["_","_","_","_","_","_"]

    while(not enforcou and not acertou):
        print("A palavra eh {}".format(letras_acertadas))
        chute =  (input("Informe a letra: ").strip())
        posicao = 0

        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                print("Encontrei a letra {} na mosicao {}!".format(chute, posicao))
                letras_acertadas[posicao] = chute

            posicao = posicao + 1


        print("Jogando...")

if (__name__ == "__main__"):
    jogar()
