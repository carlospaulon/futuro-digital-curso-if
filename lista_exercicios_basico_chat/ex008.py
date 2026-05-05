count = 0

for i in range(0, 11):
    value = int(input('Informe um número: '))
    
    if value < 0:
        count += 1
        print(f'Achamos {count} negativo(s)')
