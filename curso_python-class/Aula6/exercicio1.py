def imprimir_dicionario(dicionario: dict[str, float]):
    for key, value in dicionario.items():
        print(f'{key}: R${value:.2f}')

#definição da estrutura de dados para armazenar os produtos e seus preços
lista_produtos: dict[str, float] = {}

#Preenchendo o dicionário com os produtos e seus preços
lista_produtos['leite'] = 4.00
lista_produtos['ovos'] = 12.50
lista_produtos['pão'] = 2.50
#Ou assim:
#lista_produtos = {'leite': 4.00, 'ovos': 12.50, 'pão': 2.50}

#Exibindo os produtos e seus preços
imprimir_dicionario(lista_produtos)

lista_produtos['leite'] = 3.50

#Exibindo os produtos e seus preços atualizados
print("\nProdutos e preços atualizados:")
imprimir_dicionario(lista_produtos)

#Tem banana no dicionário? Se não, retorna 'Produto não encontrado'
item = lista_produtos.get('banana', 'Produto não encontrado')
print(f'\n{item}')

#Alteramos o preço da banana e exibimos o dicionário atualizado
lista_produtos['banana'] = 1.50
imprimir_dicionario(lista_produtos)

#Excluimos o pão e exibimos o dicionário atualizado
del lista_produtos['pão']
imprimir_dicionario(lista_produtos)
