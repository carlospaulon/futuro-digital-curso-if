from produto import Produto
from carrinho import Carrinho

p1 = Produto("Mouse Gamer", 150.0)
p2 = Produto("Teclado Mecânico", 350.0)
meu_carrinho = Carrinho()
meu_carrinho.adicionar(p1)
meu_carrinho.adicionar(p2)
print(f"Total do carrinho: R${meu_carrinho.calcular_total():.2f}")