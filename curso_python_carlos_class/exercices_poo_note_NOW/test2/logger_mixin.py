from datetime import datetime

class LoggerMixin:
    def log(self, mensagem):
        print(f"[LOG - {datetime.now()}]: {mensagem}")