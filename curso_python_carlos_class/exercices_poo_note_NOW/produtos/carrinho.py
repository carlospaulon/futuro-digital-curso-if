from produto import Produto

class Carrinho:
    def __init__(self):
        self.itens = [] # Agregação de objetos Produto

    def adicionar(self, produto: Produto):
        self.itens.append(produto)

    def calcular_total(self):
        return sum(item.preco for item in self.itens)
