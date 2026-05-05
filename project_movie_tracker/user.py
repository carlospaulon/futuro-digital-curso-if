from dataclasses import dataclass
from email_validator import validate_email, EmailNotValidError

@dataclass
class Usuario:
    nome: str
    email: str

    def __post_init__(self):
        try:
            valid = validate_email(self.email)
            self.email = valid.email  # normalizado
        except EmailNotValidError as e:
            raise ValueError(f"Email inválido: {e}")

if __name__ == '__main__':
    usuario1 = Usuario(nome="João", email="joaAoO@email.com")
    print(usuario1)
    # usuario2 = Usuario(nome="João", email="joao@errado")

