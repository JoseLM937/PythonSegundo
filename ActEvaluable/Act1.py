import copy
"""
Shallow copy: Crea una nueva lista, pero los elementos son referencias
a los mismos objetos que estan en la lista original

Depp Copy: Crea una nueva lista y copia recursivamente los objetos interinos tambien
"""
#Clonar una lista de las dos formas(Shallow y Deep Copy)
def clonar_lista(original_lista):
    shallow_copia = original_lista.copy()
    deep_copia = copy.deepcopy(original_lista)
    return shallow_copia, deep_copia

#Agregar elemento a una lista
def agregar(lista, elemento):
    lista.append(elemento)
    return lista

#Eliminar elemento de una lista
def eliminar(lista, elemento):
    lista.remove(elemento)
    return lista

#Hacer una lista con los ultimos cuatro numeros de otra
def cuatroNumeros(original_lista):
    return original_lista[-4:]

#Convertir las palabras de una cadena a una lista
def listaCadena(cadena):
    listaCadenas = cadena.split()
    return listaCadenas

original_lista = [1, 2, 3, 4, 5]
print("Original Lista:", original_lista)

# Clonar Lista
shallow, deep = clonar_lista(original_lista)
print("Shallow Copy:", shallow)
print("Deep Copy:", deep)

# Agregar un Elemento
nueva_lista = agregar(original_lista, 6)
print("Lista con Elemento Agregado:", nueva_lista)

# Quitar un Elemento
lista_sin_elemento = eliminar(original_lista, 3)
print("Lista sin Elemento:", lista_sin_elemento)

# Obtener los Últimos Cuatro Elementos
ultimos_cuatro = cuatroNumeros(original_lista)
print("Últimos Cuatro Elementos:", ultimos_cuatro)

# Convertir Cadena a Lista
cadena = "Hola mundo Python"
lista_palabras = listaCadena(cadena)
print("Cadena a Lista:", lista_palabras)

