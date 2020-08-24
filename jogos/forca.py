import random

def jogar():
    
    print("\n##################################")
    print("Bem vindos ao jogo da Forca!")
    print("\n##################################")

    palavra_secreta = "Claudia"
    letras_acertadas = []

    enforcou = False
    acertou = False
    erros = 0 

    for i in palavra_secreta:
        letras_acertadas.append("_")
    print("Você deseja dicas ? \n")
    dica = int(input("Sim 1 | Não 2: "))
    if (dica == 1):
        print("\nDica - 1 = Quantidade de palavras = ", len(palavra_secreta))
        for i in letras_acertadas:
            print(i, end = " ")
        print("\n")
    else:
        print("\nContinue Jogando...\n")

    while (not enforcou and not acertou):
        chute = input("Qual a letra: ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra

            index += 1

        print(letras_acertadas)
        
        print("jogando...")

    print("\nO Jogo Terminou !!!")

if (__name__ == "__main__"):
    jogar()