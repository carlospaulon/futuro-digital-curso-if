from nave_base import NaveBase
from sistema_defesa_mixin import SistemaDefesaMixin
from missao_invalida_erro import MissaoInvalidaErro

class NaveGuerra(NaveBase, SistemaDefesaMixin):
    def __init__(self, nome, capitao, quantidade_combustivel=0):
        super().__init__(nome)
        self.capitao = capitao
        self.quantidade_combustivel = quantidade_combustivel
        self.tripulacao.append(capitao)

    @property
    def capitao(self):
        return self._capitao
    
    @capitao.setter
    def capitao(self, membro):
        if membro.posto.value >= 3:
            self._capitao = membro
        else:
            raise MissaoInvalidaErro(f'A pessoa designada como capitao na verdade é um {membro.posto.name}')
        
    
    def preparar_para_decolagem(self):
        # Verificar tripulação para pegar um de cada posto
        tripulacao_completa = False
        lista_tripulacao = [1, 2, 3, 4, 5]
        tripulacao_atual = []

        for membro in self.tripulacao:
            if membro.posto.value in lista_tripulacao:
                tripulacao_atual.append(membro.posto.value)
        
        tripulacao_atual.sort()
        tripulacao_atual = tripulacao_atual[0:5:1]
        if tripulacao_atual.__eq__(lista_tripulacao):
            tripulacao_completa = True

        if self.nivel_combustivel > 80 and tripulacao_completa:
            return f'{self.nome} pronta para decolagem com comandante {self.capitao.nome}'
        else:
            raise MissaoInvalidaErro('A nave ainda não está pronta para decolagem')