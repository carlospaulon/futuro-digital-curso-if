from posto_enum import PostoEnum

class PessoaTripulacao:
    def __init__(self, nome: str, posto: PostoEnum, idade: int, anos_experiencia: int):
        self.nome = nome
        self.posto = posto
        self.idade = idade
        self.experiencia_anos = anos_experiencia
    
    @property
    def idade(self):
        return self._idade

    @property
    def experiencia_anos(self):
        return self._experiencia_anos


    @idade.setter
    def idade(self, idade):
        if idade <= 18:
            raise ValueError('Membros da tripulação devem ter pelo menos 18 anos')
        else:
            self._idade = idade
        
    @experiencia_anos.setter
    def experiencia_anos(self, experiencia_anos):
        if experiencia_anos > self.idade - 1:
            raise ValueError('O tempo de experiência deve ser maior do que a idade')
        else:
            self._experiencia_anos = experiencia_anos