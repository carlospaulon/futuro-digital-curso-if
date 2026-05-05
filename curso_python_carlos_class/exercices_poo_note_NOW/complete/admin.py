from base_user import BaseUsuario

# 3. Herança e Especialização
class Admin(BaseUsuario):
    def obter_permissoes(self):
        return ["leitura", "escrita", "exclusao"]