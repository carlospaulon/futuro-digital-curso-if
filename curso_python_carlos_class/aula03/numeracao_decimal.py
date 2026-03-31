# Minha solução em aula
def verificar_quantidade1(num):
    centena = 100
    dezena = 10
    unidade = 1
    count_centena = 0
    count_dezena = 0
    count_unidade = 0

    while (num >= unidade):
        if (num >= centena):
            num -= centena
            count_centena += 1
        elif (num >= dezena):
            num -= dezena
            count_dezena += 1
        else:
            num -= unidade
            count_unidade += 1
    
    print(f'{count_centena} centena(s), {count_dezena} dezena(s), {count_unidade} unidade(s)')

# Solução com array (baseada no Ju)
def verificar_quantidade2(num):
    quantidades = [100, 10, 1]
    denominacao = ["centena(s)", "dezena(s)", "unidade(s)"]
    report = ""

    for i in range(len(quantidades)):
        count = 0

        while num >= quantidades[i]:
            num -= quantidades[i]
            count += 1
        
        if count > 0:
            report += f"{count} {denominacao[i]} "

    print(report.strip())

# Solução com array, realizando o cálculo matemático
def verificar_quantidade3(num):
    quantidades = [100, 10, 1]
    denominacao = ["centena(s)", "dezena(s)", "unidade(s)"]
    report = ""

    for i in range(len(quantidades)):
        count = num // quantidades[i] # Quantidade de vezes que será 'subtraído'
        num = num % quantidades[i] # Vai sempre dividir pelas quantidades, o que sobrar vai dividir de novo (quando cair em unidade, será dado o valor (1 para cada unidade))
        
        if count > 0:
            report += f"{count} {denominacao[i]} "

    print(report.strip())

# Solução com função Python (divmod - faz a divisão entre 2 valores, guarda o resultado e o resto em 2 variáveis (a, b))
def verificar_quantidade4(num):
    denominacoes = [("centena(s)", 100), ("dezena(s)", 10), ("unidade(s)", 1)]

    for nome, valor in denominacoes:
        quantidade, num = divmod(num, valor)
        print(f"{quantidade} {nome}", end=", " if valor > 1 else "\n")
    

# Pedindo um número e verificando se está dentro do intervalo
def pedir_numero():
    while True:
        numero = int(input("Informe um número (1 a 1000): "))
        if numero >= 1 and numero <= 1000:
            return numero
        else:
            print("Número fora do intervalo")

numero = pedir_numero()
verificar_quantidade1(numero)
verificar_quantidade2(numero)
verificar_quantidade3(numero)
verificar_quantidade4(numero)