from aluno_graduacao import AlunoGraduacao
from aluno_pos_graduacao import AlunoPosGraduacao
from datetime import date
from cursos_enum import Cursos
from linha_pesquisa_enum import LinhaPesquisa

class Main():
    if __name__ == '__main__':
        data = date.today()
        curso_atual = Cursos.ENGENHARIA


        aluno_graduacao = AlunoGraduacao(12, 'Carlos', data, curso_atual)

        aluno_graduacao.mensalidade()

        print('=' * 40)

        curso_pos = LinhaPesquisa.EDUCAÇÃO

        aluno_pos = AlunoPosGraduacao(curso_pos, 'Carlos', 50)

        aluno_pos.mensalidade()
