from months_enum import Months

class Employee:
    def __init__(self, nome, email, valor_hora, meses):
        self.nome = nome
        self.email = email
        self.valor_hora = valor_hora
        self.horas: dict [str, int] = {} #mes e horas trabalhadas - uso do dicionario
        self.meses = meses

    def registrar_horas(self, mes, horas_trabalhadas):
        self.horas[mes] = horas_trabalhadas


    def calcular_salario(self, mes):
        if mes in self.horas:
            return self.horas[mes] * self.valor_hora
        else:
            return 0        
        
    def emitir_relatorio(self):
        relatorio = f"Relatório de Horas para {self.nome}:\n"
        for mes, horas in self.horas.items():
            salario = self.calcular_salario(mes)
            relatorio += f"Mês: {mes}, Horas Trabalhadas: {horas}, Salário: R${salario:.2f}\n"
        return relatorio

    def __str__(self):
        return f"Funcionario: {self.nome}, Email: {self.email}, Valor Hora: {self.valor_hora}"
