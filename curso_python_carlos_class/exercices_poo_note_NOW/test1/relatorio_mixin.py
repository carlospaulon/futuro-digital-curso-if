class RelatorioMixin:
    def gerar_resumo(self):
        print("-" * 30)
        print(f"RESUMO DA CONTA: {self.nome.upper()}")
        print(f"Plano Atual: {self._plano.nome_plano}")
        print("-" * 30)