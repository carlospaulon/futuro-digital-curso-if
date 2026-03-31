n = int(input("Digite um nro de 1 a 5"))
match n:
    case 1:        print("Um")
    case 2:        print("Dois")
    case 3:        print("Tres")
    case 4:        print("Quatro")
    case 5:        print("Cinco")
    case _:        print("Valor invalido")