# Bibliotecas

import random

# Função principal

def jogar():

    imprime_mensagem_de_abertura()

    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0 
    tentativas = 6

    input_dicas = dicas(palavra_secreta,letras_acertadas)


    while (not enforcou and not acertou):
        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
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

# Funções do jogo --------------------------

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
     index = 0
     for letra in palavra_secreta:
        if(chute.upper() == letra.upper()):
            letras_acertadas[index] = letra
        index += 1

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
    dica = int(input("Sim 1 | Não 2: "))
    
    if (dica == 1):
        print("\nQuantidade de letras da palavra secreta! = ", len(palavra_secreta))
        for i in letras_acertadas:
            return print(i, end = " "), print("\n")
    else:
        return print("\nContinue Jogando...\n")

# Chama o arquivo como principal e não como import

if (__name__ == "__main__"):
    jogar()