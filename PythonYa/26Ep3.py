def multiplicar(lista, valor):
    for x in range(len(lista)):
        multi = lista[x] * valor
        print(multi)


#Bloque principal
lista=[3,7,8,10,2]
print("Lista original")
print(lista)
print("Lista multiplicada por 3")
multiplicar(lista,3)
