def imprime_lista(lista):
    for item in lista:
        print(item)
        
lista_frutas = ['pera', 'uva', 'maçã', 'kiwi', 'abacaxi']
print('Lista original')
imprime_lista(lista_frutas)
lista_frutas.sort()
print('\nLista ordenada')
imprime_lista(lista_frutas)
print('\nTerceiro elemento da lista = ' + lista_frutas[2])
lista_frutas[1] = 'banana'
print('\nLista com substituição = ')
imprime_lista(lista_frutas)
lista_frutas.append('abacate')
print('\nLista com adição = ')
imprime_lista(lista_frutas)
lista_frutas.remove('maçã')
print('\nLista com remoção = ')
imprime_lista(lista_frutas)
fruta = lista_frutas.pop(-1)
print('\nFruta removida: ' + fruta)
print('\nLista com remoção do último elemento = ')
imprime_lista(lista_frutas)
print ('\nTamanho da lista =  ' + str(len(lista_frutas)))
lista_frutas.sort(reverse=True)
print('\nLista ordenada em ordem decrescente = ')
imprime_lista(lista_frutas)

#Solução 1
print('\nLista sem banana: Solução 1')
for item in lista_frutas:
   if (item != 'banana'):
        print(item) 

#Solução 2
print('\nLista sem banana: Solução 2')
existe = 'banana' in lista_frutas 
if (existe == False):
    imprime_lista(lista_frutas)
else:
    for item in lista_frutas:
        if (item != 'banana'):
            print(item)

#Solução 3
print('\nLista sem banana: Solução 3')
for fruta in lista_frutas:
    if fruta == "banana":
        continue # Skipa o indice que tem o valor == "banana"
    print("Fruta: [", fruta, "]")
