print("EXERCÍCIO 12 - Números Perfeitos")
  
def eh_perfeito(n):
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma += i
    return soma == n
 
numero = int(input("Digite um número para verificar se é perfeito: "))
if eh_perfeito(numero):
    print(f"{numero} é um número perfeito!")
else:
    print(f"{numero} não é um número perfeito.")
 
limite = int(input("Digite um limite n para listar todos os perfeitos até n: "))
print(f"Números perfeitos até {limite}:", end=" ")
for i in range(1, limite + 1):
    if eh_perfeito(i):
        print(i, end=" ")
print()