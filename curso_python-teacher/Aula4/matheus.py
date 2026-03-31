def seperardor(num):
    unidade =int( num % 10 )
    dezena = int((num % 100) / 10) 
    if num == 1000:
        centena =  10
    else:
        centena = int((num % 1000) / 100)
    return[centena, dezena, unidade]

#---------------------Principal----------------------

num = int(input('Digite um numero (0 a 1000): '))
while num > 1000:
    num = int(input('Digite um numero (0 a 1000): '))

lista = seperardor(num)
print(f'Centena: {lista[0]} Dezena: {lista[1]} Unidade: {lista[2]}')