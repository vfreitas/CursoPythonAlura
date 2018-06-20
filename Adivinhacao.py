import random


def jogar():
    print("***************************\n"
          "--- JOGO DA ADIVINHACAO ---\n"
          "***************************\n")

    numero_secreto = round(random.randrange(1,101))
    pontos = 100

    nivel = int(input("\nQual o nivel de dificuldade??\n1 - Facil\n2 - Medio\n3 - Dificil\n"))

    if (nivel == 1):
        total_de_tentativas = 10
    elif (nivel == 2):
        total_de_tentativas = 5
    elif (nivel == 3):
        total_de_tentativas = 3

    for rodada in range(1,total_de_tentativas + 1):
        print("\n\nTentativa {} de {}".format(rodada, total_de_tentativas))

        chute = int(input("\nTente adivinhar o numero secreto:"))
        while (chute < 1) or (chute > 100):
            print("Numero Invlido")
            chute = int(input("Informe um numero entre  e 100: "))

        acertou = numero_secreto == chute
        maior = numero_secreto > chute
        menor = numero_secreto < chute

        if (acertou):
            print("\nVoce acertou")
            break
        elif (maior):
            print("\nVoce errou")
            print("O numero secreto eh maior que", chute)
            pontos = pontos - (numero_secreto - chute)
        elif (menor):
            print("\nVoce errou")
            print("O numero secreto eh menor que", chute)
            pontos = pontos - (chute - numero_secreto)

    print("\n\nFim de jogo")
    print("O numero secreto era {}".format(numero_secreto))
    print("Voce terminou com {:03} pontos".format(pontos))

if (__name__ == "__main__"):
    jogar()

