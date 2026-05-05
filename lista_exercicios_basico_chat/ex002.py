
# EXERCÍCIO 2 - Aumento de Salário com Percentual Variável
 
print("\n" + "=" * 60)
print("EXERCÍCIO 2 - Aumento com Percentual Variável")
print("=" * 60)
 
print("\n[BÁSICA]")
 
salario = float(input("Digite o salário: "))
percentual = float(input("Digite o percentual de aumento: "))
aumento = salario * (percentual / 100)
novo_salario = salario + aumento
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")
 


print("\n[ROBUSTA]")
 
def calcular_aumento(salario, percentual):
    #Calcula o aumento e o novo salário dado um percentual
    if salario < 0:
        raise ValueError("Salário não pode ser negativo.")
    if percentual < 0 or percentual > 100:
        raise ValueError("Percentual deve estar entre 0 e 100.")
    aumento = salario * (percentual / 100)
    novo_salario = salario + aumento
    return aumento, novo_salario
 
try:
    salario = float(input("Digite o salário: R$ "))
    percentual = float(input("Digite o percentual de aumento (%): "))
    aumento, novo_salario = calcular_aumento(salario, percentual)
    print(f"\n--- Resultado ---")
    print(f"Salário atual:     R$ {salario:>10.2f}")
    print(f"Percentual:            {percentual:>9.1f}%")
    print(f"Valor do aumento:  R$ {aumento:>10.2f}")
    print(f"Novo salário:      R$ {novo_salario:>10.2f}")
except ValueError as e:
    print(f"Erro: {e}")