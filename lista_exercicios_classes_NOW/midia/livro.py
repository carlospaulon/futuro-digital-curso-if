from midia import Midia
from editora import Editora

class Livro(Midia):
    def __init__(self, titulo: str, ano: int, autor: str, isbn: str, editora: Editora):
        super().__init__(titulo, ano)
        self.autor = autor
        self.isbn = isbn
        self.editora = editora  # agregação

    def reproduzir(self):
        return "O livro está sendo lido"