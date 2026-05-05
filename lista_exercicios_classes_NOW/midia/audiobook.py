from livro import Livro
from narrador import Narrador

class AudioLivro(Livro):
    def __init__(self, titulo: str, ano: int, autor: str, isbn: str, editora,
                tempoLeitura: int, narrador_nome: str, narrador_sexo: str):
        
        super().__init__(titulo, ano, autor, isbn, editora)
        self.tempoLeitura = tempoLeitura

        # composição
        self.narrador = Narrador(narrador_nome, narrador_sexo)

    def reproduzir(self, velocidade: int = 1):
        return f"O livro está sendo lido na velocidade {velocidade}"