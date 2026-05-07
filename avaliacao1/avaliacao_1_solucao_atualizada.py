"""Solução atualizada"""

def valida_categoria(cat):
    categoria_formatada = cat.upper()
    return categoria_formatada in categorias


def agrupar_por_categoria(lista_compras):
    # Fazer puxando da própria lista de categorias
    agrupado_categoria = {
        'ALIMENTO': 0.0,
        'LIMPEZA': 0.0,
        'HIGIENE': 0.0
    }
    
    # Values retonar tupla com (categoria - 0, preco - 1)
    for valor in lista_compras.values():
        agrupado_categoria[valor[0]] += valor[1]
    
    print(agrupado_categoria)

def calcular_gasto_total(lista_compras):
    total = 0

    for valor in lista_compras.values():
        total += valor[1]
    
    return total


def verificar_produto_mais_caro_por_categoria(lista_compras):
    mais_caro_por_categoria = {}
    maior = 0


    for produto, (categoria, valor) in lista_compras.items():
        maior = 0
        if valor >= maior:
            maior = valor
            mais_caro_por_categoria[categoria] = {produto, maior}
    return mais_caro_por_categoria


categorias = ['ALIMENTO', 'HIGIENE', 'LIMPEZA']
loja: dict[str, str, float] = {}

menu = """
Loja de Produtos

1- Cadastrar novo produto(nome, categoria, preco)
2- Relatório total por categoria (alimento, limpeza, higiene)
3- Produto mais caro por categoria
4- Gasto total
0- Sair
"""

while True:
    print('=' * 40)
    print(menu)
    print('=' * 40)
    print(loja)
    opcao = int(input('Informe a opcao desejada: '))
    match opcao:
        case 1:
            produto = input('Informe o produto: ')
            cat = input('Informe uma categoria: ')
            categoria_validada = valida_categoria(cat)
            while categoria_validada is False:
                cat = input('Informe uma categoria válida: ')
                categoria_validada = valida_categoria(cat)
            valor = float(input('Informe o valor do produto: '))

            loja[produto] = (cat.upper(), valor)

            for chave, valor in loja.items():
                print(chave, valor)
            
            print(loja)
        case 2:
            print('Relatório total por categoria')
            agrupar_por_categoria(loja)
        case 3:
            print('Produto mais caro')
            print(verificar_produto_mais_caro_por_categoria(loja))
        case 4:
            print('Relatório total')
            print(f'A soma de todos os itens é R$ {calcular_gasto_total(loja):.2f}')
        case 0:
            print('Sair')
            break
        case _:
            print('Opção inválida')