import random

def iniciar_jogo():
    # 1. Configuração inicial
    numero_secreto = random.randint(1, 100)
    palpites = [] # usando uma lista para armazenar os palpites do usuário
    
    print("========================================")
    print("🎮 BEM-VINDO AO JOGO DE ADIVINHAÇÃO!")
    print("Estou pensando num número entre 1 e 100.")
    print("========================================\n")

    # 2. Ciclo principal (Simulando um Do-While)
    while True:
        # Pedir o palpite ao jogador
        entrada = int(input(f"Tentativa {len(palpites) + 1} - Qual é o seu palpite? "))
        
        # Validar se a entrada é numérica
        if not isinstance(entrada, int):
            print("⚠️ Por favor, digite um número inteiro válido.")
            continue #volta para o início do loop para pedir um novo palpite

        #Validar se o número está dentro do intervalo permitido
        if entrada<1 or entrada>100:
            print("⚠️ O número deve ser entre 1 e 100. Tente novamente.")
            continue #volta para o início do loop para pedir um novo palpite1
        
        palpite = int(entrada)
        
        # Guardar o palpite no histórico
        palpites.append(palpite)

        # 3. Lógica de Verificação
        if palpite == numero_secreto:
            print(f"\n🎉 PARABÉNS! Acertou no número {numero_secreto}!")
            break # Sai do ciclo pois o jogo terminou
        
        elif palpite < numero_secreto:
            print("🔼 Mais alto! Tente novamente.")
        else:
            print("🔽 Mais baixo! Tente novamente.")
                

    # 4. Exibição das Estatísticas Finais
    print("📊 RESUMO DA PARTIDA")
    print(f"Total de tentativas: {len(palpites)}")
    print(f"Números tentados: {palpites}")


if __name__ == "__main__":
    iniciar_jogo()