def acha_menor(n1, n2, n3):
    menor = n1  # Inicializa o menor com o primeiro número
    if n2 < menor:
        menor = n2
    if n3 < menor:
        menor = n3
    return menor

#-----------CODIGO PRINCIPAL -----------
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

menor_todos = acha_menor(n1, n2, n3)      

print(f"O menor número é: {menor_todos}")