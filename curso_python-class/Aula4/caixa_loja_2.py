def calcular_preco_final(valor_produto, taxa_desconto = 0.05):
    """
    Calcula o preço final de um produto após aplicar um desconto.

    :param valor_produto: O preço original do produto.
    :return: O preço final do produto após o desconto.
    """
    desconto = taxa_desconto * valor_produto  
    preco_final = valor_produto - desconto
    return preco_final

#-----------CODIGO PRINCIPAL -----------
valor = 0
cod = 1
quant = 0
passou = False
while (passou == False):
    cod = int(input("Digite o codigo do produto ou zero para sair: "))
    if (cod == 0):
        break
    elif (cod != 101 and cod != 102 and cod != 103 and cod != 104):
        print("Código inválido. Por favor, digite um código válido (101, 102, 103, 104) ou zero para sair.")
        passou=False
    else:
        quant = 0
        while (quant<=0):
            quant = float(input("Digite a quantidade do produto: "))
            if (quant <= 0):
                    print("Quantidade inválida. Por favor, digite um valor maior que zero.")
            else:
                match cod:
                    case 101: #Shampoo
                        valor += 10 * quant
                    case 102: #Condicionador
                        valor += 12 * quant
                    case 103: #Sabonete
                        valor += 3 * quant
                    case 104: #Creme Dental
                        valor += 15 * quant
if (valor == 0):
    print("Nenhum produto foi comprado.")
    exit()
else:
    print(f"O valor total da compra é: R$ {valor:.2f}")
    forma_pagamento = int(input("Digite a forma de pagamento (1 - à vista, 2 - pix, 3 - credito): "))
    if forma_pagamento == 1:
        preco_final = calcular_preco_final(valor_produto=valor)
    elif forma_pagamento == 2:  
        preco_final = calcular_preco_final(taxa_desconto=0.02, valor_produto=valor)
    else:    
        preco_final = valor
    print(f"O preço final da compra é: R$ {preco_final:.2f}")


