class Narrador:
    """
    Representa o narrador de um audiolivro.
    CONCEITO: Composição - Narrador é criado e gerenciado pelo AudioLivro.
    Sua existência está atrelada ao AudioLivro que o contém.
    CONCEITO: Encapsulamento - atributos privados com getters.
    """
 
    def __init__(self, nome: str, sexo: str):
        """Inicializa o narrador com nome e sexo."""
        self.__nome: str = nome                 # Nome do narrador
        self.__sexo: str = sexo                 # "M" ou "F"
 
    def get_nome(self) -> str:
        return self.__nome
 
    def get_sexo(self) -> str:
        return self.__sexo
 
    def __str__(self) -> str:
        genero = "Narrador" if self.__sexo.upper() == "M" else "Narradora"
        return f"{genero}: {self.__nome}"