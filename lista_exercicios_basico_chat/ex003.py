# EXERCÍCIO 3 - Área da Circunferência
 
print("\n" + "=" * 60)
print("EXERCÍCIO 3 - Área da Circunferência")
print("=" * 60)
 
print("\n[BÁSICA]")
 
raio = float(input("Digite o raio da circunferência: "))
area = 3.14159 * raio ** 2
print(f"Área da circunferência: {area:.2f}")
 
print("\n[ROBUSTA]")
 
def calcular_area_circulo(raio):
    # Calcula a área de um círculo dado o raio.
    PI = 3.14159
    if raio < 0:
        raise ValueError("O raio não pode ser negativo.")
    area = PI * raio ** 2
    return area
 
try:
    raio = float(input("Digite o raio da circunferência: "))
    area = calcular_area_circulo(raio)
    print(f"\n--- Resultado ---")
    print(f"Raio:  {raio:.2f}")
    print(f"Área:  {area:.4f}")
    print(f"Área:  {area:.2f} (arredondada)")
except ValueError as e:
    print(f"Erro: {e}")