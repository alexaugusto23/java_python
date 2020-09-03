class Conta:

    def __init__(self):
        print("Construindo objeto...{}".format(self))
        self.numero = 123
        self.titulo = "Nico"
        self.saldo = 55.00
        self.limite = 1000.00



conta = Conta()
print(conta)