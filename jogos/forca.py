# Bibliotecas
import random
import time
import sys

# Função principal
def jogar():

    imprime_mensagem_de_abertura()

    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0 
    tentativas = 7
    print("numero de tentativas",tentativas)

    input_dicas = dicas(palavra_secreta,letras_acertadas)


    while (not enforcou and not acertou):
        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1 
            desenha_forca(erros)

        enforcou  = erros == tentativas
        acertou = "_" not in letras_acertadas

        jogando(letras_acertadas)

    if (acertou):
        imprime_msg_vencedor()

    else:
        imprime_msg_perdedor(palavra_secreta,tentativas) 

# Funções do jogo --------------------------
def jogando(letras_acertadas):
    print(letras_acertadas)

    load = []

    for i in range(0,4):
        load.append(".")

    print("\nJogando",end = " ")

    for i in range(0,len(load)-1):
        time.sleep(0.5)
        print(load[i], end = " " )
    print("\n")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |       _    ")
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |       _    ")
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |       _    ")
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |       _    ")
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |       _    ")
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |       _    ")
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |       _    ")
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print("_|___         ")
    print()

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
     index = 0
     for letra in palavra_secreta:
        if(chute.upper() == letra.upper()):
            print()
            letras_acertadas[index] = letra
            print()
        index += 1

def imprime_msg_vencedor():
    print("\nParabéns, você ganhou!")
    print("       ___________      ")
    print("        _________       ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_msg_perdedor(palavra_secreta ,tentativas):
    print("\nAcabou o número de tentativas |{}| deste nível. \nA palavra secreta era: {}".format(tentativas, palavra_secreta))
    print("Você foi enforcado !!!")
    print("     _______________         ")
    print("    /               \       ")
    print("   /                 \      ")
    print("/\/                   \/\  ")
    print("\ |   XXXX     XXXX   | /   ")
    print(" \|   XXXX     XXXX   |/     ")
    print("  |   XXX       XXX   |      ")
    print("  |                   |      ")
    print("  \__      XXX      __/     ")
    print("    |\     XXX     /|       ")
    print("    | |           | |        ")
    print("    | I I I I I I I |        ")
    print("    |  I I I I I I  |        ")
    print("|___    IIIIIIII    ___|    ")
    print("     \_           _/         ")
    print("       \_________/           ")

def pede_chute():
    chute = input("Qual a letra: ")
    chute = chute.strip().upper()
    return chute

def imprime_mensagem_de_abertura():
    print("\n##################################")
    print("Bem vindos ao jogo da Forca!")
    print("\n##################################")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt","r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def dicas(palavra_secreta,letras_acertadas):
    print("Você deseja dicas ? \n")
    dica = int(input("Deseja continuar? 1 para Sim | 2 para Não\nDigite:")) 

    if (dica == 1):
        print("\nQuantidade de letras da palavra secreta! = ", len(palavra_secreta))
        for i in letras_acertadas:
            return print(i, end = " "), print("\n")
    else:
        load = []

        for i in range(0,4):
            load.append(".")

        print("\nJogando",end = " ")

        for i in range(0,len(load)-1):
            time.sleep(0.5)
            print(load[i], end = " " )
        print("\n")

# Chama o arquivo como principal e não como import
if (__name__ == "__main__"):
    jogar()