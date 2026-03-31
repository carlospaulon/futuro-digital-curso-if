def imprimi_lista(lista):
    for item in lista:
        print(item)


frutas = ['Maça', 'Pera', 'Kiwi', 'Uva', 'Abacaxi']

# passo 1
print('Lista padrão')
imprimi_lista(frutas)

# passo 2
frutas.sort()
print('\nLista ordenada')
imprimi_lista(frutas)

# passo 3
print(f'\nTerceiro elemento da lista ordenada: {frutas[2]}')

# passo 4
frutas[1] = 'Banana'
print(f'\nAlterando o segundo elemento: {frutas[1]}')
imprimi_lista(frutas)

# passo 5
frutas.append('Abacate')

print(f'\nAdicionando: {frutas[-1]} ao final da lista')
imprimi_lista(frutas)

# passo 6
terceiro_item = frutas[2]
frutas.remove(terceiro_item)
print(f'\nRemovendo {terceiro_item}')
imprimi_lista(frutas)

# passo 7
last_item = frutas[-1]
frutas.pop(-1)
print(f'\nRemovendo o último item: {last_item}')
imprimi_lista(frutas)

# passo 8
print(f'\nTamanho da lista: {len(frutas)} items')

# passo 9
frutas.sort(reverse=True)
print(f'\nLista ordenada ao contrário')
imprimi_lista(frutas)

# passo 10
has_banana = 'Banana' in frutas
print(f'\nImprimindo a lista, menos Banana')
if has_banana:
    for fruta in frutas:
        if fruta != 'Banana':
            print(fruta)
else:
    print(f'\nImprimindo a lista')
    imprimi_lista(frutas)


print("\nSolução 2 passo 10 - Imprimindo a lista de frutas sem mostrar a banana:")
for fruta in frutas:
    if fruta == "Banana":
        continue
    else:
        print("Fruta: [", fruta, "]")