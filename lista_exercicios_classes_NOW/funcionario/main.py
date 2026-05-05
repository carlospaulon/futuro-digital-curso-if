from employee import Employee
from months_enum import Months

class TestaFuncionario:
    funcionario = Employee ('Matheus', 'matheus@blablabla.com.br', 50, Months)
    funcionario.registrar_horas(Months.JANEIRO.name, 300)
    funcionario.registrar_horas(Months.FEVEREIRO.name, 200)
    salario = funcionario.calcular_salario(Months.JANEIRO.name)
    print(funcionario) # to
    print(funcionario.__dict__)
    print(f"Salário de Jan: R${salario:.2f}")
    print(funcionario.emitir_relatorio())