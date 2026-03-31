nota1 = float(input("Digite a primeira nota: "))
if (nota1 < 0 or nota1 > 10):
    print("Nota inválida. Digite um valor entre 0 e 10.")
    exit()
nota2 = float(input("Digite a segunda nota: "))
if (nota2 < 0 or nota2 > 10):
    print("Nota inválida. Digite um valor entre 0 e 10.")
    exit()
nota3 = float(input("Digite a terceira nota: "))
if (nota3 < 0 or nota3 > 10):
    print("Nota inválida. Digite um valor entre 0 e 10.")
    exit()
media = (nota1 + nota2 + nota3) / 3
print("Sua media foi: ", media)
if (media <=3): #se 
    print("Reprovado")
elif (media > 3 and media < 7):#senão se
    print("Recuperação")
else:    print("Aprovado") #senão