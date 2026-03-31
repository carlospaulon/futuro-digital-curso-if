#Faça um programa na linguagem Python que leia 
# um número inteiro positivo, referente ao tipo
# de transformação de unidade decimal desejada
# (comprimento, massa, capacidade, superfície, 
# volume). Em seguida apresente os simbolos de 
# unidades do sistema e solicite o valor que 
# deseja converter, a unidade de medida desse 
# número e a unidade de medida para o qual 
# deseja converter. A conversão deve ser feita 
# através de uma ou mais funções com pelo menos 
# 3 parâmetros: o valor, a unidade de medida 
# original e a unidade de medida desejada. 
# A saída deve ser algo do tipo “O resultado da 
# conversão de 345m para cm é 34500 cm”
def converte_comprimento(valor, unidade_origem, unidade_destino):
    unidades = {"mm": 0.001, "cm": 0.01, "m": 1, "km": 1000}
    if unidade_origem in unidades and unidade_destino in unidades:
        valor_em_metros = valor * unidades[unidade_origem]
        valor_convertido = valor_em_metros / unidades[unidade_destino]
        print(f"O resultado da conversão de {valor}{unidade_origem} para {unidade_destino} é {valor_convertido} {unidade_destino}")
    else:
        print("Unidade de medida inválida.")


def converte_massa(valor, unidade_origem, unidade_destino):
    unidades = {"mg": 0.001, "g": 1, "kg": 1000, "t": 1000000}
    if unidade_origem in unidades and unidade_destino in unidades:
        valor_em_gramas = valor * unidades[unidade_origem]
        valor_convertido = valor_em_gramas / unidades[unidade_destino]
        print(f"O resultado da conversão de {valor}{unidade_origem} para {unidade_destino} é {valor_convertido} {unidade_destino}")
    else:
        print("Unidade de medida inválida.")


def converte_capacidade(valor, unidade_origem, unidade_destino):
    unidades = {"ml": 0.001, "cl": 0.01, "dl": 0.1, "l": 1}
    if unidade_origem in unidades and unidade_destino in unidades:
        valor_em_litros = valor * unidades[unidade_origem]
        valor_convertido = valor_em_litros / unidades[unidade_destino]
        print(f"O resultado da conversão de {valor}{unidade_origem} para {unidade_destino} é {valor_convertido} {unidade_destino}")
    else:
        print("Unidade de medida inválida.")


def converte_superficie(valor, unidade_origem, unidade_destino):
    unidades = {"mm²": 0.000001, "cm²": 0.0001, "m²": 1, "km²": 1000000}
    if unidade_origem in unidades and unidade_destino in unidades:
        valor_em_metros_quadrados = valor * unidades[unidade_origem]
        valor_convertido = valor_em_metros_quadrados / unidades[unidade_destino]
        print(f"O resultado da conversão de {valor}{unidade_origem} para {unidade_destino} é {valor_convertido} {unidade_destino}")
    else:
        print("Unidade de medida inválida.")


def converte_volume(valor, unidade_origem, unidade_destino):
    unidades = {"mm³": 0.000001, "cm³": 0.001, "m³": 1, "km³": 1000000}
    if unidade_origem in unidades and unidade_destino in unidades:
        valor_em_metros_cubicos = valor * unidades[unidade_origem]
        valor_convertido = valor_em_metros_cubicos / unidades[unidade_destino]
        print(f"O resultado da conversão de {valor}{unidade_origem} para {unidade_destino} é {valor_convertido} {unidade_destino}")
    else:
        print("Unidade de medida inválida.")

#-------------------------- Principal --------------------------
opcao = 0
while (opcao < 1 or opcao > 5):
    opcao = int(input("""Digite o número inteiro positivo referente ao tipo de transformação de unidade decimal desejada:
1 - Comprimento
2 - Massa
3 - Capacidade
4 - Superfície
5 - Volume"""))
    if opcao >= 1 and opcao <= 5:
        valor = float(input("Digite o valor que deseja converter: "))
        match opcao:
            case 1:
                print("Unidades de comprimento: mm, cm, m, km")
                unidade_origem = input("Digite a unidade de medida original: ")
                unidade_destino = input("Digite a unidade de medida desejada: ")
                converte_comprimento(valor, unidade_origem, unidade_destino)
            case 2:
                print("Unidades de massa: mg, g, kg, t")
                unidade_origem = input("Digite a unidade de medida original: ")
                unidade_destino = input("Digite a unidade de medida desejada: ")
                converte_massa(valor, unidade_origem, unidade_destino)
            case 3:
                print("Unidades de capacidade: ml, cl, dl, l")
                unidade_origem = input("Digite a unidade de medida original: ")
                unidade_destino = input("Digite a unidade de medida desejada: ")
                converte_capacidade(valor, unidade_origem, unidade_destino)
            case 4:
                print("Unidades de superfície: mm², cm², m², km²")
                unidade_origem = input("Digite a unidade de medida original: ")
                unidade_destino = input("Digite a unidade de medida desejada: ")
                converte_superficie(valor, unidade_origem, unidade_destino)
            case 5:
                print("Unidades de volume: mm³, cm³, m³, km³")
                unidade_origem = input("Digite a unidade de medida original: ")
                unidade_destino = input("Digite a unidade de medida desejada: ")
                converte_volume(valor, unidade_origem, unidade_destino)
    else:          
        print("Opção inválida. Digite um número entre 1 e 5.")
        continue