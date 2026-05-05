from conta_bancaria import ContaBancaria

conta = ContaBancaria("Alice", 1000.0)
conta.saldo = -50  # Dispara a validação do setter
print(f"Saldo atual de {conta.titular}: {conta.saldo}")