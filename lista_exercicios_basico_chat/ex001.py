# EXERCÍCIO 1 - Aumento de Salário (15%)
 
print("=" * 60)
print("EXERCÍCIO 1 - Aumento de Salário (15%)")
print("=" * 60)
 
# --- Versão Básica ---
print("\n[BÁSICA]")
 
salario = float(input("Digite o salário do funcionário: "))
novo_salario = salario * 1.15
print(f"Novo salário: R$ {novo_salario:.2f}")
 

print("\n[ROBUSTA]")
 
def calcular_aumento_fixo(salario, percentual=15):
    # Calcula o novo salário com aumento percentual fixo
    if salario < 0:
        raise ValueError("Salário não pode ser negativo.")
    aumento = salario * (percentual / 100)
    novo_salario = salario + aumento
    return aumento, novo_salario
 
try:
    salario = float(input("Digite o salário do funcionário: R$ "))
    aumento, novo_salario = calcular_aumento_fixo(salario)
    print(f"\n--- Resultado ---")
    print(f"Salário atual:  R$ {salario:>10.2f}")
    print(f"Aumento (15%):  R$ {aumento:>10.2f}")
    print(f"Novo salário:   R$ {novo_salario:>10.2f}")
except ValueError as e:
    print(f"Erro: {e}")