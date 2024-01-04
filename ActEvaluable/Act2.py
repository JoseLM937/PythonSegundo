
def suma(num1, num2):
    return num1+num2

def doblar(lista):
    for valor in range(len(lista)):
        lista[valor] *= 2

def copiar(lista):
    copiaLista = lista.copy()
    for valor in range(len(copiaLista)):
        copiaLista[valor] *= 2
    return copiaLista

#Bloque principal
resultado = suma(5, 7)
print("Resultado de la suma:", resultado)

# Doblar los valores de una lista
lista = [1, 2, 3, 4]
print("Lista original antes de la modificación:", lista)
doblar(lista)
print("Lista original después de la modificación:", lista)

# Copia de la lista doblando sus valores
lista = [1, 2, 3, 4]
listaModificada = copiar(lista)
print("Lista original:", lista)
print("Copia modificada:", listaModificada)
