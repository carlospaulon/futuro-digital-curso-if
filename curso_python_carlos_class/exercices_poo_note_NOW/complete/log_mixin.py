# 1. Mixin para capacidade de Log
class LogMixin:
    def registrar_log(self, mensagem):
        print(f"[LOG - {self.__class__.__name__}]: {mensagem}")