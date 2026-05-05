from cursos_enum import Cursos

class AlunoGraduacao:
    def __init__(self, matricula, nome, dataNascimento, curso: Cursos):
        self.matricula = matricula
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.curso = curso

    def mensalidade(self):
        print(f'Mensalidade do curso é R$ {self.curso.value}')