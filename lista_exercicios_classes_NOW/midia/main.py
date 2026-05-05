from editora import Editora
from livro import Livro
from audiobook import AudioLivro

def main():
    # editora
    editora = Editora("Editora Tech", "123456789")

    #criando livro
    livro = Livro("Python Básico", 2023, "João Silva", "ISBN001", editora)
    print(livro.reproduzir())

    # criando audiobook
    audio = AudioLivro(
        "Python Avançado",
        2024,
        "Maria Souza",
        "ISBN002",
        editora,
        320,
        "Carlos",
        "Masculino"
    )

    print(audio.reproduzir())
    print(audio.reproduzir(2))


if __name__ == "__main__":
    main()