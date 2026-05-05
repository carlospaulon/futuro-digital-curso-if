from editora import Editora
from livro import Livro
from narrador import Narrador

class AudioLivro(Livro):
    """
    Representa um audiolivro (livro narrado em áudio).
    CONCEITO: Herança - AudioLivro "é um" Livro com funcionalidades extras.
    CONCEITO: Composição - AudioLivro cria o Narrador internamente.
    O Narrador desta narração não existe fora do AudioLivro.
    """
 
    VELOCIDADE_PADRAO: int = 1                  # Velocidade padrão de leitura
 
    def __init__(self, titulo: str, ano: int, autor: str, isbn: str,
                 editora: Editora, tempo_leitura: int,
                 nome_narrador: str, sexo_narrador: str):
        """
        Respeita a COMPOSIÇÃO com Narrador:
        o Narrador é criado INTERNAMENTE a partir dos dados fornecidos.
        CONCEITO: Composição - Narrador criado dentro de AudioLivro (sem existência própria).
        CONCEITO: Herança - super().__init__() inicializa Livro (que inicializa Midia).
        """
        super().__init__(titulo, ano, autor, isbn, editora)  # Inicializa Livro
 
        if tempo_leitura <= 0:                  # Validação do tempo de leitura
            raise ValueError(f"Tempo de leitura deve ser positivo: {tempo_leitura}")
 
        self.__tempo_leitura: int = tempo_leitura           # Duração da narração em minutos
        self.__narrador: Narrador = Narrador(               # COMPOSIÇÃO: criado aqui dentro
            nome_narrador, sexo_narrador
        )
 
    def get_tempo_leitura(self) -> int:
        return self.__tempo_leitura
 
    def get_narrador(self) -> Narrador:
        return self.__narrador
 
    def reproduzir(self, velocidade: int = VELOCIDADE_PADRAO) -> str:
        """
        Sobrescreve reproduzir() de Livro com parâmetro de velocidade.
        CONCEITO: Polimorfismo - comportamento especializado com parâmetro extra.
        O parâmetro tem valor padrão (velocidade=1), mantendo compatibilidade.
        CONCEITO: Tratamento de exceções - velocidade inválida levanta ValueError.
        """
        if velocidade <= 0:                     # Velocidade deve ser positiva
            raise ValueError(f"Velocidade deve ser positiva: {velocidade}")
        return f"O livro está sendo lido na velocidade {velocidade}."
 
    def __str__(self) -> str:
        return (
            f"{super().__str__()} | "
            f"Tempo: {self.__tempo_leitura}min | "
            f"{self.__narrador}"
        )