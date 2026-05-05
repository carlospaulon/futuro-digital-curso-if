# EXERCÍCIO 4 - Média Ponderada de Notas
 
print("\n" + "=" * 60)
print("EXERCÍCIO 4 - Média Ponderada de Notas")
print("=" * 60)
 
print("\n[BÁSICA]")
 
nota1 = float(input("Digite a nota da 1ª prova (peso 4): "))
nota2 = float(input("Digite a nota da 2ª prova (peso 6): "))
media = (nota1 * 4 + nota2 * 6) / 10
print(f"Nota final: {media:.2f}")
 
print("\n[ROBUSTA]")
 
def calcular_media_ponderada(nota1, nota2):
    # Calcula a média ponderada de duas notas (pesos 4 e 6)
    for n in [nota1, nota2]:
        if not (0 <= n <= 10):
            raise ValueError(f"Nota {n} fora do intervalo permitido (0 a 10).")
    media = (nota1 * 4 + nota2 * 6) / 10
    return media
 
def situacao(media):
    if media >= 7:
        return "Aprovado ✓"
    elif media >= 5:
        return "Recuperação ⚠"
    else:
        return "Reprovado ✗"
 
try:
    nota1 = float(input("Nota da 1ª prova (peso 4, entre 0 e 10): "))
    nota2 = float(input("Nota da 2ª prova (peso 6, entre 0 e 10): "))
    media = calcular_media_ponderada(nota1, nota2)
    print(f"\n--- Resultado ---")
    print(f"1ª Prova (peso 4): {nota1:.1f}")
    print(f"2ª Prova (peso 6): {nota2:.1f}")
    print(f"Média final:       {media:.2f}")
    print(f"Situação:          {situacao(media)}")
except ValueError as e:
    print(f"Erro: {e}")