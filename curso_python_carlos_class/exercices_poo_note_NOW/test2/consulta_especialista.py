from consulta import Consulta

class ConsultaEspecialista(Consulta):
    def calcular_honorarios(self):
        return 350.00 * 1.2