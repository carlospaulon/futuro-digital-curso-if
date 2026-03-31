def calcular_desconto(valor_total):
    return valor_total - (valor_total * 0.05)

def processar_pagamento(produtos, total):
    pagamento = input('Pagamento à (v)ista ou (p)arcelado: ')

    while (pagamento.lower() != 'v' or 'p'):
        if (pagamento.lower() == 'v'):
            print('Produtos: ', produtos)
            valor_final = calcular_desconto(total)
            print(f'Valor total: {valor_final:.2f}')
            break
        elif (pagamento.lower() == 'p'):
            print('Produtos ', produtos)
            print(f'Valor total: {total:.2f}')
            break
        else:
            print('Método de pagamento inválido\nInforme um método válido')
            pagamento = input('Pagamento à (v)ista ou (p)arcelado: ')
    print('Encerrando o programa')

codigo = int(input('Informe o código: '))
total = 0
loja = {'101': ['Shampoo', 10.00], '102': ['Condicionador', 12.00], '103': ['Sabonete', 3.00], '104': ['Creme dental', 15.00]}

produtos = []

while True:
    if codigo == 0:
        processar_pagamento(produtos, total)
        break

    if str(codigo) in loja.keys():
        produto = loja[str(codigo)][0]
        valor_unitario = loja[str(codigo)][1]

        print(produto + '=' + str(valor_unitario))
        quantidade = int(input('Informe a quantidade: '))

        while quantidade <= 0:
            quantidade = int(input('Quantidade inválida! Informe uma quantidade maior que 0: '))
        
        produtos.append(loja[str(codigo)][0])
        total += valor_unitario * quantidade
    else:
        print('Código inválido! Informe um novo código')
    
    print('\nNovo produto a ser cadastrado')
    codigo = int(input('Informe o código: '))
