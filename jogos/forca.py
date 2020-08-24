import random

def jogar():
    
    print("\n##################################")
    print("Bem vindos ao jogo da Forca!")
    print("\n##################################")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0 
    tentativas = 6

    print("Você deseja dicas ? \n")
    dica = int(input("Sim 1 | Não 2: "))

    if (dica == 1):
        print("\nQuantidade de letras da palavra secreta! = ", len(palavra_secreta))
        for i in letras_acertadas:
            print(i, end = " ")
        print("\n")
    else:
        print("\nContinue Jogando...\n")

    while (not enforcou and not acertou):
        chute = input("Qual a letra: ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1 
        enforcou  = erros == tentativas
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
        print("jogando...")
    
    if (acertou):
        print("Você Ganhou!!!")
    else: 
        print("Você perdeu... \nAcabou o número de tentativas |{}| deste nível".format(tentativas))

    print("\nO Jogo Terminou !!!")

if (__name__ == "__main__"):
    jogar()