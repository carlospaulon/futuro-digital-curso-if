import abc
from log_mixin import LogMixin

# 2. Classe Abstrata de Usuário
class BaseUsuario(abc.ABC, LogMixin):
    def __init__(self, nome, email):
        self.nome = nome
        self._email = email
        self.__senha = "123456" # Privado

    @abc.abstractmethod
    def obter_permissoes(self):
        pass

    def verificar_senha(self, tentativa):
        if self.__senha == tentativa:
            self.registrar_log(f"Sucesso no acesso de {self.nome}")
            return True
        self.registrar_log(f"Falha de senha para {self.nome}")
        raise PermissionError("Senha incorreta.")