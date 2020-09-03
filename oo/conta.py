class Conta:

    def __init__(self, numero, titular, saldo, limite):
        # Atributos são caracteristicas que o objeto tem.
        print("Construindo objeto...{}".format(self)) 
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

        # Incluindo métodos que são comportamnetos que o objeto possui a partir de seus atributos.
        # self = referência (.ponto) --> acessa atributo (váriavel) 
    def extrato(self):
        #print("Saldo {} do titular {}".format(self.saldo, self.titular))
        print(f"O Saldo do titular {self.__titular} é: {self.__saldo}")

    def deposita(self, valor):
        self.__saldo += valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
        pass

    def saca(self, valor):
        self.__saldo -= valor
    
    #Getters e Setters
    def get_saldo(self):
        return self.__saldo
    
    def get_titular(self):
        return self.__titular

    def get_limite(self):
        return self.__limite



#conta1 é uma referência na memória para a classe(objeto) Conta
conta1 = Conta(1,"Alex", 30.00, 400.00)
conta2 = Conta(2,"Ana", 10.00, 600.00)
conta3 = Conta(3, "Sicrano", 2000.0, 2000.0)

#Para acessar o conteúdo do Objeto conta usa-se
#a referência(conta1) e o ponto + atributo.
#print(conta1.saldo)
#print(conta2.saldo)
#print(conta3.saldo)

# Chamando a função(comportamento) do objeto Conta
#conta1.extrato()
#conta1.deposita(100.00)
#conta1.extrato()

#conta2.extrato()
#conta3.extrato()
#conta3.transfere(100.00,conta2)
#conta2.extrato()
#conta3.extrato()

print("Nome:",conta1.get_titular())
print("Saldo:",conta1.get_saldo())
print("Limite:",conta1.get_limite())
