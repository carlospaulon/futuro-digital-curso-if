class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco # Esse init está chamando o método setter abaixo
    
    @property
    def preco(self):
        print('Acessando valor do produto')
        return self._preco

    @preco.setter
    def preco(self, valor):
        if valor < 0:
            print('Erro: o preço não pode ser negativo')
            self._preco = 0 # underline, indica que estamos usando o atributo preco, e não o método setter (evita recursão infinita)
        else:
            print(f'Definindo valor para {valor}')
            self._preco = valor
    

if __name__ == '__main__':
    produto1 = Produto('Cadeira', 50)
    print(produto1.preco)
    produto1.preco = 100
    print(produto1.preco)