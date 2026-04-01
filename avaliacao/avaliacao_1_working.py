def valida_categoria(cat):
    categoria_formatada = cat.upper()
    return categoria_formatada in categorias


# No
def agrupar_por_categoria(lista_compras):
    agrupado_categoria = {}

    for produto, (categoria, valor) in lista_compras.items():
        if categoria not in agrupado_categoria:
            agrupado_categoria[categoria] = 0

        agrupado_categoria[categoria] += valor

    print(agrupado_categoria)

def calcular_gasto_total(lista_compras):
    total = 0

    for valor in lista_compras.values():
        total += valor[1]
    
    return total


# No
def verificar_produto_mais_caro_por_categoria(lista_compras):
    mais_caro_por_categoria = {}

    for produto, (categoria, valor) in lista_compras.items():
        if categoria not in mais_caro_por_categoria:
            mais_caro_por_categoria[categoria] = valor
        else:
            if valor > mais_caro_por_categoria[categoria]:
                mais_caro_por_categoria[categoria] = valor

    return mais_caro_por_categoria


categorias = ['ALIMENTO', 'HIGIENE', 'LIMPEZA']
contador = 0
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

            contador += 1
            loja[produto] = (cat, valor)

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