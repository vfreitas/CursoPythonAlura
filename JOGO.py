import Forca
import Adivinhacao


def escolha_jogo():
    print("**************************\n"
          "----  ESCOLHA O JOGO -----\n"
          "**************************\n")

    print("(1) Forca ou (2) Adivinhacao\n")

    repetir = "S"

    while repetir == "S":

        jogo = int(input("Qual Jogo vc deseja jogar?"))

        while jogo != 1 and jogo != 2:
            jogo = int(input("Informe uma opcao valida"))

        if jogo == 1:
            print("\nVoce escolheu Forca\n\n")
            Forca.jogar()
        elif jogo == 2:
            print("\nVoce escolheu Adivinhacao\n\n")
            Adivinhacao.jogar()

        repetir = (input("Deseja jogar novamente? S/N")).upper().strip()



if __name__ == "__main__":
    escolha_jogo()
