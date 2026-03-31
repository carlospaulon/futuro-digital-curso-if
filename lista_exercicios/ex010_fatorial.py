# EXERCÍCIO 10 - Fatorial

def fatorial_iterativo(n):
    # Calcula o fatorial de n de forma iterativa 
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def fatorial_recursivo(n):
    # Calcula o fatorial de n de forma recursiva
    if n == 0 or n == 1:
        return 1
    return n * fatorial_recursivo(n - 1)

n = int(input("Digite um número inteiro positivo: "))

if n < 0:
    print("Erro: O número deve ser positivo.")
else:
    resultado_iter = fatorial_iterativo(n)
    resultado_rec  = fatorial_recursivo(n)

    partes = " × ".join(str(i) for i in range(1, n + 1)) if n > 0 else "1"
    print(f"\n--- Resultado ---")
    print(f"n = {n}")
    print(f"Desenvolvimento: {partes if n > 0 else '0! = 1'}")
    print(f"Resultado (iterativo):  {n}! = {resultado_iter}")
    print(f"Resultado (recursivo):  {n}! = {resultado_rec}")