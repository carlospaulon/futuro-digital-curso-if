while True:
    nro = int(input("Digite um número inteiro menor do que 1000\n"))
    if nro >=0 and nro <= 1000:
        centena = nro //100
        #print(centena)
        dezena = nro //10 %10
        #print(dezena)
        unidade = nro %10
        #print(unidade)
        print(centena,"centena(s)" ,dezena,"dezena(s)",unidade,"unidade(s)")
        break
    else:
        print("Número inválido")