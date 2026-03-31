cursos_tecnicos =  ('Informatica', 'Administracao','Panificacao', 'Turismo')

# Variável ternario
print('Com ternário - verificação cursos')
hasPanificacao = 'Tem o curso de Panificação' if 'Panificacao' in cursos_tecnicos else 'Não tem Panificação'
hasLogistica = 'Tem o curso de Logistica' if 'Logistica' in cursos_tecnicos else 'Não tem Logistica'

print(hasPanificacao)
print(hasLogistica)

print('\nCom bool - veririficação cursos')
print('Tem o curso de panificação: ' + str('Panificacao' in cursos_tecnicos))
print('Tem o curso de logistica: ' + str('Logistica' in cursos_tecnicos))

print('\nTamanho do curso')
print(len(cursos_tecnicos))

print('\nImprimindo elementos da tupla')
for curso in cursos_tecnicos:
    print(curso)

print('\nImprimindo elementos da tupla ordenada')
print(f'Lista padrão {cursos_tecnicos}')

# Converte a tupla para lista - Casting
cursos_tecnicos_lista = list(cursos_tecnicos)

# Ordena a lista
cursos_tecnicos_lista.sort()

print(f'Lista ordenada: {cursos_tecnicos_lista}')

# Desempacotamento
print(f'\nLista ordenada por desempacotamento')
curso_lista = [*cursos_tecnicos]
print(type(curso_lista))
curso_lista.sort()

print(curso_lista)

# Com for e append
print(f'\nLista ordenada por for e append')
cursos_ordenados = []

for curso in cursos_tecnicos:
    cursos_ordenados.append(curso)

print(f'Lista padrão {cursos_ordenados}')
cursos_ordenados.sort()
print(f'Lista ordenada {cursos_ordenados}')
