def quantas_centenas(numero):
    return numero // 100    

def quantas_dezenas(numero):
    return numero  // 10


#------------- CODIGO PRINCIPAL -------------
# 
numero = int(input("Digite um numero inteiro: "))  

if (numero >= 0) and (numero<1000):
    centenas = quantas_centenas(numero)
    numero = numero - centenas * 100
    dezenas = quantas_dezenas(numero)
    numero = numero - dezenas * 10
    unidades = numero % 10
    print(f"Centenas: {centenas}")
    print(f"Dezenas: {dezenas}")
    print(f"Unidades: {unidades}")
else:
    print("Erro: Por favor, digite um número inteiro não negativ, menor que 1000.")
    
