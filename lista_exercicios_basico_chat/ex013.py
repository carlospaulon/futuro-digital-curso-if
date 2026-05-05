turma = []
aluno: dict[str, list[float], float] = {}
notas = []

def cadastro_aluno(nome):
    aluno['nome'] = nome
    turma.append(aluno)

def cadastro_notas(aluno: str, notas_aluno: list):

    for student in turma:
        for key, value in student.items():
            if value == aluno:
                aluno['notas'] = notas_aluno
    print(turma)
    print(aluno.items())
    print(notas)
    print(notas_aluno)

def calcula_media():
    ...

menu = """
1 - Cadastrar novo aluno
2 - Cadastrar notas de um aluno
3 - Verificar média do aluno
4 - Verificar situação do aluno
5 - Listar todos os alunos aprovados, reprovados e exame
0 - Sair
"""

while True:
    print(menu)
    opcao = int(input('Informe a opcao: '))

    match opcao:
        case 1:
            print('Cadastro aluno')
            nome = input('Informe o nome do aluno: ')
            cadastro_aluno(nome=nome)
            print(*turma)
        case 2:
            print('Nota')
            for i in range(3):
                nota = float(input('Informe a nota do aluno: '))
                notas.append(nota)
            nome_aluno = input('Informe o nome do aluno: ')
            cadastro_notas(nome_aluno, notas)
        case 3:
            print('Média')
        case 4:
            print('Situação')
        case 5:
            print('Lista')
        case 0:
            print('Sair')
            break
        case _:
            print('Opção inválida')