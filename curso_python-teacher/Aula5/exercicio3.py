def ler_notas():
    notas = []
    while True:
        entrada = input("Digite uma nota entre 0 e 10 (ou -1 para finalizar): ")
        if entrada == '-1':
            break
        elif (entrada.isdigit()):
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("⚠️ Nota deve ser entre 0 e 10.")
        else:
            print("⚠️ Entrada inválida. Por favor, digite um número entre 0 e 10 ou -1 para finalizar.")
    return notas

def exibir_notas(notas):
    if not notas:
        print("Nenhuma nota foi inserida.")
        return
    print("\nNotas inseridas:")
    for i in notas:
        print(notas.index(i) + 1, "-", i)

def exibir_notas_invertidas(notas):
    if not notas:
        print("Nenhuma nota foi inserida.")
        return
    print("\nNotas em ordem invertida:")
    notas.reverse() # Inverte a lista de notas (não é ordenação inversa)
    for i in notas:
        print(notas.index(i) + 1, "-", i)

def somar_notas(notas):
    return sum(notas)

def calcular_media(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

def exibir_acima_media(notas, media=7):
    cont = 0
    print(f"\nNotas acima da média ({media:.2f}):")
    for nota in notas:
        if nota >= media:
            print(nota)
            cont += 1
    print(f"Total de notas acima da média: {cont}")

def exibir_abaixo_media(notas, media=7):
    cont = 0
    print(f"\nNotas abaixo da média ({media:.2f}):")
    for nota in notas:
        if nota < media:
            print(nota)
            cont += 1
    print(f"Total de notas abaixo da média: {cont}")

def main():
    notas = ler_notas()
    exibir_notas(notas)
    exibir_notas_invertidas(notas)
    total = somar_notas(notas)
    media = calcular_media(notas)
    print(f"\nSoma das notas: {total:.2f}")
    print(f"Média das notas: {media:.2f}")
    exibir_acima_media(notas, media)
    exibir_abaixo_media(notas)

if __name__ == "__main__":
    main()