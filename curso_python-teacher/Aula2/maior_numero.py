n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if n1 > n2:
    maior = n1
elif n2 > n1:
    maior = n2
else:
    print("Os números são iguais.")
    exit()

print(f"o maior número é: {maior}")