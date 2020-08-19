def jogar():

    print("\n##################################")
    print("Bem vindos ao jogo da Forca!")
    print("\n##################################")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False


    while (not enforcou and not acertou):
        chute = input("Qual a letra: ")
        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                print("Encontrei a Letra |{}| na posição {}".format(letra, index))
            index += 1
        print("jogando...")

    print("\nO Jogo Terminou !!!")

if (__name__ == "__main__"):
    jogar()