class Veiculo:
    reino = 'Máquinas' # atributo da classe (toda classe vai ter esse reino=Máquinas)

    # Construtor
    def __init__(self, marca, modelo, cor):
        self.marca = marca # Cria e intancia os atributos
        self.modelo = modelo
        self.cor = cor
    
    def descrever(self): # Self puxa as coisas da classe, e as funções possuem 'sempre' o self
        return f'\n{self.marca=}\n{self.modelo=}\n{self.cor=}'
    
    def __eq__(self, value):

        # Se o objeto para verificação, não for do tipo Veiculo, já retornamos False (não são iguais)
        if not isinstance(value, Veiculo): # aqui também poderia fazer se for isntancia, realiza a verificação
            return False
        
        # Compara os 2 objetos
        return self.marca == value.marca and self.modelo == value.modelo and self.cor == value.cor