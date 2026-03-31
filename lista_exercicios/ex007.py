print("EXERCÍCIO 7 - Controle de Acesso por Portas")
 
print("\n[BÁSICA]")
 
porta = int(input("Por qual porta deseja entrar (1, 2 ou 3)? "))
codigo = int(input("Digite seu código de usuário: "))
 
match porta:
    case 1:
        if (1000 <= codigo <= 2000) or (3000 <= codigo <= 5000):
            print("Acesso liberado")
        else:
            print("Acesso negado")
    case 2:
        if 150 <= codigo <= 350:
            print("Acesso liberado")
        else:
            print("Acesso negado")
    case 3:
        if (10000 <= codigo <= 11000) or (20000 <= codigo <= 30000):
            print("Acesso liberado")
        else:
            print("Acesso negado")
    case _:
        print("Porta inexistente")
