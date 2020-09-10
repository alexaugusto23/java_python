class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        print('chamando @property')
        return self.__nome.title()

    @property
    def nome(self, nome):
        return self.__nome.title()
        
cliente = Cliente("alex")
print(cliente.nome)