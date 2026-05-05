from relatorio_mixin import RelatorioMixin
from plano import Plano
from pagamento_exception import PagamentoRecusadoError

# Classe Principal (Interação e Encapsulamento)
class Usuario(RelatorioMixin):
    def __init__(self, nome, email, plano_inicial: Plano):
        self.nome = nome
        self.email = email
        self._plano = plano_inicial # Encapsulado
        self._saldo_conta = 100.0   # Simulação de saldo

    def alterar_plano(self, novo_plano: Plano):
        self._plano = novo_plano
        print(f"Usuário {self.nome} migrou para o plano {novo_plano.nome_plano}")

    def processar_assinatura(self):
        custo = self._plano.calcular_preco()
        try:
            if self._saldo_conta < custo:
                raise PagamentoRecusadoError(f"Saldo insuficiente para {self._plano.nome_plano}")
            self._saldo_conta -= custo
            print(f"Pagamento de R${custo} processado. Novo saldo: R${self._saldo_conta:.2f}")
        except PagamentoRecusadoError as e:
            print(f"Falha na Cobrança: {e}")