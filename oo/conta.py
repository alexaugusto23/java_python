class Conta:

    def __init__(self, numero, titular, saldo, limite):
        #print("Construindo objeto...{}".format(self))
        # Atributos são caracteristicas que o objeto tem.
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

        # Incluindo métodos que são comportamnetos que o objeto possui a partir de seus atributos.
        # self = referência (.ponto) --> acessa atributo (váriavel) 
    def extrato(self):
        #print("Saldo {} do titular {}".format(self.saldo, self.titular))
        print(f"O Saldo do titular {self.titular} é: {self.saldo}")

    def deposita(self, valor):
        self.saldo += valor
    
    def saca(self, valor):
        if (self.saldo <= 0):
            if (valor > self.limite):
                print("Sem saldo")
                print(f"Seu saldo é: {self.saldo} ")
                self.saldo -= valor
                print(f"Limite disponivel é: {self.limite} ")
                self.saldo -= - self.limite


        else:
            self.saldo -= valor 

#conta1 é uma referência na memória para a classe(objeto) Conta
conta1 = Conta(1,"Alex", 0.00, 400.00)
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
conta1.saca(390.00)
conta1.extrato()