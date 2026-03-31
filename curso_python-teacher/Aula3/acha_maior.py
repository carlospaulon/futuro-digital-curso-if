maior = 0
for cont in range(5):
    n = int(input("Digite um número: "))
    if n > maior:
        maior = n
        print("O maior número até agora é:", maior)
print("O maior número é:", maior)