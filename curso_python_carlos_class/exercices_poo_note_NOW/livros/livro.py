from editora import Editora
from midia import Midia

class Livro(Midia):
    """
    Representa um livro físico ou digital.
    CONCEITO: Herança - Livro herda de Midia e implementa reproduzir().
    CONCEITO: Agregação - Livro recebe uma Editora pronta (não a cria internamente).
    A Editora pode existir e publicar outros livros independentemente.
    """
 
    def __init__(self, titulo: str, ano: int, autor: str, isbn: str, editora: Editora):
        """
        Construtor respeita a AGREGAÇÃO com Editora:
        a Editora é passada pronta — não é criada internamente.
        CONCEITO: Objetos como parâmetros - Editora recebida como argumento.
        CONCEITO: Herança - super().__init__() inicializa Midia.
        """
        super().__init__(titulo, ano)           # Inicializa Midia com título e ano
        self.__autor: str = autor               # Autor do livro
        self.__isbn: str = isbn                 # ISBN único do livro
        self.__editora: Editora = editora       # Referência à Editora (AGREGAÇÃO)
 
    def get_autor(self) -> str: return self.__autor
    def get_isbn(self) -> str: return self.__isbn
    def get_editora(self) -> Editora: return self.__editora
 
    def reproduzir(self) -> str:
        """
        Define como um livro é 'reproduzido' (lido).
        CONCEITO: Polimorfismo - implementa o método abstrato de Midia.
        """
        return "O livro está sendo lido."       # Mensagem específica para leitura
 
    def __str__(self) -> str:
        return (
            f"{super().__str__()} | "
            f"Autor: {self.__autor} | "
            f"ISBN: {self.__isbn} | "
            f"{self.__editora}"
        )
 
    def __eq__(self, other) -> bool:
        """Dois livros são iguais se têm o mesmo ISBN (único por livro)."""
        if not isinstance(other, Livro):
            return False
        return self.__isbn == other.__isbn      # ISBN é o identificador único do livro