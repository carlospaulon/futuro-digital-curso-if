from admin import Admin

# 4. Execução e Tratamento
try:
    admin = Admin("Carlos", "carlos@empresa.com")
    if admin.verificar_senha("senha_errada"):
        print(admin.obter_permissoes())
except PermissionError as e:
    print(f"Alerta de Segurança: {e}")
finally:
    print("Processo de autenticação encerrado.")