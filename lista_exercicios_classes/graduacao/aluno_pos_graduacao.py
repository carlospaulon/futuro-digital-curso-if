from linha_pesquisa_enum import LinhaPesquisa

class AlunoPosGraduacao:
    def __init__(self, linhaPesquisa: LinhaPesquisa, orientador, bolsaEstudos):
        self.linha_pesquisa = linhaPesquisa
        self.orientador = orientador
        self.bolsa_estudos = bolsaEstudos

    def mensalidade(self):
        porcentagem = (self.bolsa_estudos / 100) * self.linha_pesquisa.value
        mensalidade = self.linha_pesquisa.value - porcentagem

        print(f'Mensalidade de pós graduação {mensalidade}')