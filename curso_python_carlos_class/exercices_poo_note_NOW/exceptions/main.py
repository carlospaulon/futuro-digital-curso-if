from user_inative_exception import UsuarioInativoError

usuarios = {"admin": True, "dev_joao": False}

def realizar_login(username):
    if username not in usuarios:
        raise KeyError(f"Usuário {username} não encontrado.")
    if not usuarios[username]:
        raise UsuarioInativoError(f"A conta {username} está suspensa.")
    print(f"Login bem-sucedido para {username}!")

# Teste
try:
    realizar_login("dev_joao")
except UsuarioInativoError as e:
    print(f"Erro de Acesso: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")