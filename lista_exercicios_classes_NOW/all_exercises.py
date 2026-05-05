"""
===========================================================
EXERCÍCIOS DE PROGRAMAÇÃO ORIENTADA A OBJETOS (COMPLETO)
===========================================================

Este arquivo contém as soluções completas dos exercícios:
9, 10, 11 e 12.

Cada exercício foi implementado com:
- Encapsulamento
- Herança
- Polimorfismo
- Classes abstratas
- Interfaces
- Validações reais
- Testes no final

===========================================================
"""

# =========================
# IMPORTS NECESSÁRIOS
# =========================

from abc import ABC, abstractmethod
import math
from datetime import date


# =========================================================
# ===================== EXERCÍCIO 9 =======================
# =========================================================

"""
a) RELACIONAMENTOS:

✔ GENERALIZAÇÃO (HERANÇA)
Cliente -> ClienteComum / ClienteEspecial

✔ COMPOSIÇÃO
NotaFiscal -> Cliente + Carro
(Nota fiscal não existe sem cliente e carro)

✔ AGREGAÇÃO
Locadora -> Carros
(Carros podem existir fora da locadora)

"""

# =========================
# CLASSE CARRO
# =========================

class Carro:
    def __init__(self, placa, tipo, modelo, ano, cor, chassi, km, valor_km):
        self.__placa = placa
        self.__tipo = tipo
        self.__modelo = modelo
        self.__ano = ano
        self.__cor = cor
        self.__chassi = chassi
        self.__km = km
        self.__valor_km = valor_km

    def get_valor_km(self):
        return self.__valor_km

    def __str__(self):
        return f"{self.__modelo} ({self.__placa})"


# =========================
# CLASSE CLIENTE (BASE)
# =========================

class Cliente:
    def __init__(self, codigo, nome, cpf, telefone, endereco):
        self.codigo = codigo
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco

    def calcular_desconto(self, valor):
        return valor  # cliente comum não tem desconto


# =========================
# CLIENTE ESPECIAL (HERANÇA)
# =========================

class ClienteEspecial(Cliente):
    def __init__(self, codigo, nome, cpf, telefone, endereco, desconto, km_extra):
        super().__init__(codigo, nome, cpf, telefone, endereco)
        self.desconto = desconto
        self.km_extra = km_extra

    def calcular_desconto(self, valor):
        return valor * (1 - self.desconto)


# =========================
# NOTA FISCAL (COMPOSIÇÃO)
# =========================

class NotaFiscal:
    def __init__(self, cliente, carro, km_percorrida):
        self.cliente = cliente
        self.carro = carro
        self.km_percorrida = km_percorrida

    def calcular_valor(self):
        valor_base = self.km_percorrida * self.carro.get_valor_km()
        return self.cliente.calcular_desconto(valor_base)

    def __str__(self):
        return f"Cliente: {self.cliente.nome} | Carro: {self.carro}"


# =========================
# TESTE EXERCÍCIO 9
# =========================

def teste_exercicio_9():
    print("\n===== TESTE EXERCÍCIO 9 =====")

    carro = Carro("ABC123", "luxo", "BMW", 2022, "preto", "XYZ", 0, 5)

    cliente = ClienteEspecial(1, "João", "123", "999", "Rua A", 0.1, 50)

    nota = NotaFiscal(cliente, carro, 100)

    print(nota)
    print("Valor final:", nota.calcular_valor())


# =========================================================
# ===================== EXERCÍCIO 10 ======================
# =========================================================

# =========================
# CLASSE ABSTRATA
# =========================

class FiguraGeometrica(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass


# =========================
# CÍRCULO
# =========================

class Circulo(FiguraGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * self.raio ** 2

    def perimetro(self):
        return 2 * math.pi * self.raio


# =========================
# RETÂNGULO
# =========================

class Retangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


# =========================
# TRIÂNGULO
# =========================

class Triangulo(FiguraGeometrica):
    def __init__(self, a, b, c):
        if not self.valido(a, b, c):
            raise ValueError("Não forma um triângulo")
        self.a = a
        self.b = b
        self.c = c

    def valido(self, a, b, c):
        return a < b + c and b < a + c and c < a + b

    def tipo(self):
        if self.a == self.b == self.c:
            return "Equilátero"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return "Isósceles"
        else:
            return "Escaleno"

    def perimetro(self):
        return self.a + self.b + self.c

    def area(self):
        p = self.perimetro() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


# =========================
# TESTE EXERCÍCIO 10
# =========================

def teste_exercicio_10():
    print("\n===== TESTE EXERCÍCIO 10 =====")

    c = Circulo(5)
    print("Área círculo:", c.area())

    r = Retangulo(4, 6)
    print("Área retângulo:", r.area())

    t = Triangulo(3, 4, 5)
    print("Área triângulo:", t.area())
    print("Tipo:", t.tipo())


# =========================================================
# ===================== EXERCÍCIO 11 ======================
# =========================================================

# =========================
# INTERFACE TRIBUTÁVEL
# =========================

class Tributavel(ABC):

    @abstractmethod
    def calcular_tributo(self):
        pass


# =========================
# CLASSE CONTA
# =========================

class Conta:
    def __init__(self, numero, agencia):
        self.numero = numero
        self.agencia = agencia
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        raise NotImplementedError


# =========================
# CONTA CORRENTE
# =========================

class ContaCorrente(Conta, Tributavel):
    def __init__(self, numero, agencia, limite):
        super().__init__(numero, agencia)
        self.limite = limite
        self.total_debitos = 0

    def sacar(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.total_debitos += valor
        else:
            raise ValueError("Saldo insuficiente")

    def calcular_tributo(self):
        return self.total_debitos * 0.0038


# =========================
# POUPANÇA
# =========================

class Poupanca(Conta):
    def __init__(self, numero, agencia, dia_rendimento):
        super().__init__(numero, agencia)
        self.dia_rendimento = dia_rendimento

    def sacar(self, valor):
        hoje = date.today().day
        if hoje == self.dia_rendimento:
            self.saldo -= valor
        else:
            raise ValueError("Só pode sacar no dia de rendimento")


# =========================
# APLICAÇÃO
# =========================

class Aplicacao(Conta, Tributavel):
    def __init__(self, numero, agencia):
        super().__init__(numero, agencia)
        self.data_inicio = date.today()

    def calcular_tributo(self):
        dias = (date.today() - self.data_inicio).days

        if dias <= 180:
            return self.saldo * 0.225
        elif dias <= 360:
            return self.saldo * 0.20
        elif dias <= 720:
            return self.saldo * 0.175
        else:
            return self.saldo * 0.15


# =========================
# TESTE EXERCÍCIO 11
# =========================

def teste_exercicio_11():
    print("\n===== TESTE EXERCÍCIO 11 =====")

    cc = ContaCorrente("1", "001", 500)
    cc.depositar(100)
    cc.sacar(200)

    print("Tributo CC:", cc.calcular_tributo())

    ap = Aplicacao("2", "001")
    ap.depositar(1000)

    print("Tributo aplicação:", ap.calcular_tributo())


# =========================================================
# ===================== EXERCÍCIO 12 ======================
# =========================================================

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def getNomeCompleto(self):
        return f"{self.nome} {self.sobrenome}"

    def __eq__(self, other):
        return isinstance(other, Pessoa) and self.getNomeCompleto() == other.getNomeCompleto()

    def __str__(self):
        return self.getNomeCompleto()


# =========================
# FUNCIONÁRIO
# =========================

class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, matricula, salario):
        super().__init__(nome, sobrenome)
        if salario < 0:
            raise ValueError("Salário não pode ser negativo")
        self.matricula = matricula
        self.salario = salario

    def getSalarioPrimeiraParcela(self):
        return self.salario * 0.6

    def getSalarioSegundaParcela(self):
        return self.salario * 0.4


# =========================
# PROFESSOR (HERANÇA)
# =========================

class Professor(Funcionario):

    def getSalarioPrimeiraParcela(self):
        return self.salario

    def getSalarioSegundaParcela(self):
        return 0


# =========================
# TESTE EXERCÍCIO 12
# =========================

def teste_exercicio_12():
    print("\n===== TESTE EXERCÍCIO 12 =====")

    f = Funcionario("Ana", "Silva", 1, 1000)
    print("Primeira parcela:", f.getSalarioPrimeiraParcela())
    print("Segunda parcela:", f.getSalarioSegundaParcela())

    p = Professor("Carlos", "Souza", 2, 2000)
    print("Professor recebe:", p.getSalarioPrimeiraParcela())


# =========================================================
# ========================= MAIN ==========================
# =========================================================

if __name__ == "__main__":
    teste_exercicio_9()
    teste_exercicio_10()
    teste_exercicio_11()
    teste_exercicio_12()