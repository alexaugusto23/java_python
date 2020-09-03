class Conta:

    def __init__(self, numero, titular, saldo, limite):
        #print("Construindo objeto...{}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

#conta1 é uma referência na memória para a classe(objeto) Conta
conta1 = Conta(1,"Alex", 0.00, 400.00)
conta2 = Conta(2,"Ana", 10.00, 600.00)
conta3 = Conta(3, "Sicrano", 2000.0, 2000.0)

#Para acessar o conteúdo do Objeto conta usa-se
#a referência(conta1) e o ponto + atributo.
print(conta1.saldo)
print(conta2.saldo)
print(conta3.saldo)