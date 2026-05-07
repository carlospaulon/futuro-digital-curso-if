from abc import ABC, abstractmethod
from pessoa_tripulacao import PessoaTripulacao

class NaveBase(ABC):
    def __init__(self, nome):
        self.nome = nome # string
        self.nivel_combustivel = 0 # int (0 a 100)
        self.status = False # Bool
        self.tripulacao = [] # Lista
        self.integridade_casco = 100 # int (0 a 100)

    @abstractmethod
    def preparar_para_decolagem(self):
        pass

    def exibir_status(self):
        return f'Olá, {self.nome}. Status atual: {self.status}'
    
    def adicionar_tripulante(self, pessoa_tripulacao: PessoaTripulacao):
        if pessoa_tripulacao not in self.tripulacao:
            self.tripulacao.append(pessoa_tripulacao)
        else:
            raise ValueError(f'{pessoa_tripulacao.nome} já está na tripulação da {self.nome}')
        
    def abastecer(self, quantidade_combustivel):
        pode_abastecer = self.nivel_combustivel + quantidade_combustivel

        if pode_abastecer < 0:
            raise ValueError('Não foi possível abastecer! Quantidade inválida!')

        # Melhorar condição
        if pode_abastecer <= 100:
            self.nivel_combustivel += quantidade_combustivel
            return f'Abastecendo a nave em {quantidade_combustivel}L, ficando com {pode_abastecer}L'
        else:
            raise ValueError(f'Não foi possível abastecer! Muito combustível! Iria transbordar com {pode_abastecer}L')
    
    def decolar(self):
        self.status = False
        return f'A nave está decolando'
    
    def pousar(self):
        self.status = True
        return f'A nave está pousando'