def jogar():

    import random

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("\n##################################")
    print("Bem vindos ao jogo da Adivinhação!")
    print("Qual o nível de dificuldade ?")
    print("(1) Fácil (2) Médio (3) Difícil")
    print("\n##################################")

    nivel = int(input("\nDefine o nível: "))

    if(nivel == 1):
        total_de_tentativas = 5
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 20


    for rodada in range (1, total_de_tentativas + 1):
        print("\n --- Tentativa {} de {} --- ".format (rodada, total_de_tentativas))
        
        chute_str = input ("\nDigite um número entre 1 e 100: ")
        print("\nVocê digitou", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("\nVocê deve digitar um número entre 1 e 100\n")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("\nVocê acertou e fez {} pontos".format(pontos))
            break
        else:
            if(maior):
                print("\nVocê errou! O seu chute foi maior que o número secreto")
            elif(menor):
                print("\nVocê errou! O seu chute foi menor que o número secreto")
            pontosperdidos = abs(numero_secreto - chute)
            pontos = pontos - pontosperdidos
        print("\n--------------------------------------------------------------")

    print("\nO numero secreto era: {}".format(numero_secreto))
    print("\nVocê não acertou dentro das tentativas do nível selecionado. \nSeus pontos foram {} pontos".format(pontos))
    print("\nO Jogo Terminou !!!")

if (__name__ == "__main__"):
    jogar()