class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        print('chamando get @property')
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print('chamando set @property')
        self.__nome = nome

cliente = Cliente("alex")
print(cliente.nome)
cliente.nome = "Claudia"
print(cliente.nome)