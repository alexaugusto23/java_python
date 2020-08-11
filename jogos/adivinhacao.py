print("\n##################################")
print("Bem vindos ao jogo da Adivinhação!")
print("##################################")

numero_secreto = 42
total_de_tentativas = 3

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
        print("\nVocê acertou")
        break
    else:
        if(maior):
            print("\nVocê errou! O seu chute foi maior que o número secreto")
        elif(menor):
            print("\nVocê errou! O seu chute foi menor que o número secreto")
    print("\n--------------------------------------------------------------")

print("\nO Jogo Terminou !!!")