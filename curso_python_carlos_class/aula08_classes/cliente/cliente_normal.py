class Cliente:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def get_nome(self):
        return self.__nome
    
    def get_cpf(self):
        return self.__cpf

    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def __eq__(self, value):
        if not isinstance(value, Cliente):
            return False
        return self.__cpf == value.__cpf
    
    def __str__(self):
        return f'Cliente: {self.__nome} e CPF: {self.__cpf}'
    
if __name__ == '__main__':
    cliente1 = Cliente('Maria', '000.000.000-00')
    cliente2 = Cliente('Maria', '000.000.000-00')

    print(cliente1.get_nome())
    print(cliente1.get_cpf())
    cliente1.set_nome('Flavia')
    print(cliente1.get_nome())
    print(cliente1)

    print(cliente1.__eq__(cliente2))