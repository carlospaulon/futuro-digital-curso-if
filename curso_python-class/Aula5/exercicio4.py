cursos_tecnicos=('Informatica', 'Administracao', 'Panificacao', 'Turismo')
print(cursos_tecnicos)
print('Tem curso de Panificacao ?' + str('Panificacao' in cursos_tecnicos))
print('Tem curso de Logistica ? ' + str('Logistica' in cursos_tecnicos))
print('Quantos cursos tecnicos tem no IFRS ? ' + str(len(cursos_tecnicos)))
print('\n Lista de Cursos Tecnicos: ')
for curso in cursos_tecnicos:
    print(curso)

#Desafio 1: Imprima a lista com os nomes dos cursos de forma oredenada
print('\n Lista de Cursos Tecnicos ordenada: ')
cursos_ordenados = []
for curso in cursos_tecnicos:
    cursos_ordenados.append(curso)
cursos_ordenados.sort()
print(cursos_ordenados)