# EXERCÍCIO 6 - Imposto de Renda
 
FAIXAS_IR = [
    (2428.00,    0.0,  "Isento"),
    (2826.65,    7.5,  "7,5%"),
    (3751.05,   15.0,  "15%"),
    (4664.68,   22.5,  "22,5%"),
    (float("inf"), 27.5, "27,5%"),
]
 
def calcular_ir(rendimento):
    # Calcula o imposto de renda com base nas faixas vigentes.
    if rendimento < 0:
        raise ValueError("Rendimento não pode ser negativo.")
    for limite, aliquota, descricao in FAIXAS_IR:
        if rendimento <= limite:
            imposto = rendimento * (aliquota / 100)
            return aliquota, descricao, imposto
    # Fallback
    return 27.5, "27,5%", rendimento * 0.275
 
try:
    rendimento = float(input("Digite o rendimento anual: R$ "))
    aliquota, faixa, imposto = calcular_ir(rendimento)
    print(f"\n--- Resultado ---")
    print(f"Rendimento anual:  R$ {rendimento:>10.2f}")
    print(f"Faixa tributária:  {faixa}")
    print(f"Alíquota:          {aliquota:.1f}%")
    print(f"Imposto a pagar:   R$ {imposto:>10.2f}")
    if aliquota == 0:
        print("→ Você está isento de imposto de renda.")
except ValueError as e:
    print(f"Erro: {e}")