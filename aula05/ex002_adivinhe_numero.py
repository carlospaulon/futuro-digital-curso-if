import random

numero_aleatorio = random.randint(1, 100) # aleatorio
numeros_tentados = [] # lista tentativa
count_tentativa = 0 # contador

tentativa = 0 # inicializa variavel

while True:
    tentativa = int(input('Informe um número entre 1 e 100: ')) # input tentativa

    if tentativa != numero_aleatorio: # verifica se o numero é diferente (errei)
        count_tentativa += 1 # incrementa contador
        numeros_tentados.append(tentativa) # adiciona tentativa errada a lista
        if tentativa > numero_aleatorio: # tentativa maior que numero
            print('Tentativa maior que número (tente um menor)') 
        else:
            print('Tentativa menor que número (tente um maior)') # tentativa menor que numero
    else: # Acertei o numero
        print(f'\n{count_tentativa+1} tentativas') #Tentativas
        print(numeros_tentados) # Lista de numeros tentados (erros)
        print(f'Número acertado: {tentativa}') # Numero acertado
        break # Para o While/programa