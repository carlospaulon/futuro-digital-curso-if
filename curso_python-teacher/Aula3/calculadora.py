def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        print("Erro: Divisão por zero não é permitida.")
        return None

#----------------Codigo Principal ------------------
n1 = float(input("Digite  um número:"))
n2 = float(input("Digite  outro número:"))
op = input("Digite a operação desejada (+, -, *, /):")
resultado = 0
match op:
    case "+":resultado = somar(n1, n2)
    case "-":resultado = subtrair(n1, n2)
    case "*":resultado = multiplicar(n1, n2)
    case "/": resultado = dividir(n1, n2)
    case _:print("Operação inválida")
if resultado != None:
    print("O resultado é:", resultado)