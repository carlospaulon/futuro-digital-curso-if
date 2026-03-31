def adicao(num1, num2):
    return num1 + num2  

def subtracao(num1, num2):
    return num1 - num2  

def multiplicacao(num1, num2):
    return num1 * num2              

def divisao(num1, num2):
    if num2 != 0:
        return num1 / num2  
    else:
        return "Erro: Divisão por zero não é permitida."        
    
#-----------CODIGO PRINCIPAL -----------

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
teste = False
while (teste == False):
    operacao = input("Escolha a operacao desejada (+, -, *, /): ")
    if operacao == '+':
        resultado = adicao(num1, num2) 
        teste = True 
    elif operacao == '-':               
        resultado = subtracao(num1, num2)
        teste = True
    elif operacao == '*':
        resultado = multiplicacao(num1, num2)
        teste = True
    elif operacao == '/':
        resultado = divisao(num1, num2)
        teste = True
    else:
        print("Operação inválida. Por favor, escolha uma operação válida.")

print(f"O resultado da operação é: {resultado}")    