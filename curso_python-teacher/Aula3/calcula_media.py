#Calcula a media de nros até digitar 0
nro = 1
cont = 0
acum = 0
while (nro != 0):
    nro = int(input("Digite um número: "))
    acum = acum + nro
    cont = cont + 1
if (cont != 1):
    media = acum / (cont -1)
    print("A média é:", media)
else:
    print("Nenhum número foi digitado")
