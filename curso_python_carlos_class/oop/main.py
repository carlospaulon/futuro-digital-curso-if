from veiculo import Veiculo
import datetime

if __name__ == '__main__':
    carro1 = Veiculo('Renault', 'Oroch', 'Vermelho')
    carro2 = Veiculo('Honda', 'Civic', 'Branco')
    carro3 = Veiculo(marca='Toyota', modelo='Corolla', cor='Preto')
    carro4 = Veiculo('Renault', 'Oroch', 'Vermelho')

    print(f'Informações 1{carro1.descrever()} \nReino: {carro1.reino} \nID: {id(carro1)}')
    print(f'\nInformações 2{carro2.descrever()} \nReino: {carro2.reino} \nID: {id(carro2)}')
    print(f'\nInformações 3{carro3.descrever()} \nReino: {carro3.reino} \nID: {id(carro3)}')
    print('\n', carro1 is carro1)

    # cuidar ao realizar este tipo de referencia a outro objeto
    carro5 = carro1 # carro5 recebe o endereço do objeto carro1 (carro5 aponta para carro1)
    print(carro5.descrever())
    print(id(carro1), id(carro5))
    print('\n', carro1 is carro5)
    
    print('carro1 e 5 são iguais? ' + str(carro1 == carro5)) # is e ==, fazem a mesma coisa, verificação por endereço

    # Vamos escrever uma função (__eq__ = equal - função mágica) na classe Veiculo, para verificarmos igualdade de conteúdo entre 2 objetos
    print(carro1.__eq__(carro4))
