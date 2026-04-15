from validate_docbr import CPF

class Cliente:
    validador_cpf = CPF()

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome
    
    @property
    def cpf(self):
        return self._cpf


    @cpf.setter
    def cpf(self, novo_cpf):
        if self.validador_cpf.validate(novo_cpf):
            self._cpf = self.validador_cpf.mask(novo_cpf)
        else:
            self.cpf = None
    
    def __str__(self):
        return f'Cliente: {self.nome}, CPF: {self.cpf}'
    
    def __eq__(self, value):
        if not isinstance(value, Cliente):
            return False
        return self.cpf == value.cpf

if __name__ == '__main__':
    cliente = Cliente('Carlos', '51417756071')
    cpf_gerado = cliente.validador_cpf.generate() # Não faz sentido

    cliente2 = Cliente('Felipe', cpf_gerado)

    print(cliente)
    print(cliente2)