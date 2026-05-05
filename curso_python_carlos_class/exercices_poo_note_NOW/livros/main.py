from editora import Editora
from livro import Livro
from audio_livro import AudioLivro
from midia import Midia

if __name__ == "__main__":
    print("=" * 65)
    print("TESTE - Exercício 14: Mídia, Livro e AudioLivro")
    print("=" * 65)
 
    # Cria Editoras (existência independente — agregação)
    editora1 = Editora("Companhia das Letras", "60.872.695/0001-84")
    editora2 = Editora("Intrínseca", "07.629.610/0001-00")
    print(editora1)
 
    # Cria Livros (agregação: Editora passada pronta)
    print("\n--- Livros ---")
    livro1 = Livro(
        "O Senhor dos Anéis", 1954,
        "J.R.R. Tolkien",
        "978-85-325-2781-7",
        editora1                                # Editora passada externamente (AGREGAÇÃO)
    )
    livro2 = Livro(
        "A Revolução dos Bichos", 1945,
        "George Orwell",
        "978-85-325-3141-8",
        editora2
    )
 
    print(livro1)
    print(livro2)
 
    # Reproduz os livros (polimorfismo)
    print(f"\n{livro1.reproduzir()}")           # "O livro está sendo lido."
    print(f"{livro2.reproduzir()}")
 
    # Cria AudioLivros (composição: Narrador criado internamente)
    print("\n--- AudioLivros ---")
    audio1 = AudioLivro(
        "O Senhor dos Anéis - Audio", 2021,
        "J.R.R. Tolkien",
        "978-85-325-2781-8-audio",
        editora1,
        tempo_leitura=3600,                     # 3600 minutos de narração
        nome_narrador="Ricardo Juarez",         # Narrador criado internamente (COMPOSIÇÃO)
        sexo_narrador="M"
    )
    audio2 = AudioLivro(
        "Sapiens - Audio", 2020,
        "Yuval Noah Harari",
        "978-85-8057-729-9-audio",
        editora2,
        tempo_leitura=960,
        nome_narrador="Ana Clara",
        sexo_narrador="F"
    )
 
    print(audio1)
    print(audio2)
 
    # Reproduz com velocidades diferentes (polimorfismo com parâmetro)
    print(f"\n{audio1.reproduzir()}")           # Velocidade padrão (1)
    print(f"{audio1.reproduzir(2)}")            # Velocidade 2x
    print(f"{audio2.reproduzir(3)}")            # Velocidade 3x
 
    # Polimorfismo: lista mista de Midias
    print("\n--- Polimorfismo: reprodução de todas as mídias ---")
    midias: list[Midia] = [livro1, livro2, audio1, audio2]
    for midia in midias:
        nome = type(midia).__name__
        print(f"[{nome}] '{midia.get_titulo()}': {midia.reproduzir()}")
 
    # Testa igualdade por ISBN
    livro1_copia = Livro("O Senhor dos Anéis Ed. Especial", 2005,
                         "J.R.R. Tolkien", "978-85-325-2781-7", editora1)
    print(f"\nlivro1 == livro1_copia (mesmo ISBN)? {livro1 == livro1_copia}")   # True
 
    # Teste de exceção
    print("\n--- Teste de validação ---")
    try:
        audio1.reproduzir(0)                    # Velocidade zero (inválida)
    except ValueError as e:
        print(f"Erro esperado: {e}")
 
    try:
        AudioLivro("Teste", 2020, "Autor", "isbn-x", editora1,
                   tempo_leitura=-5,            # Tempo negativo (inválido)
                   nome_narrador="X", sexo_narrador="M")
    except ValueError as e:
        print(f"Erro esperado: {e}")