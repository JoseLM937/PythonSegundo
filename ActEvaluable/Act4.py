
def opis():
    a = [1,2,3]
    b = [1,2,3]
    c = a

    print(a is b)
    #Sera falso porque aunque tengan los mismos valores las listas son diferentes
    print(a is c)
    #Sera verdadero ya que c hace referencia a a asi que es lo mismo

def opnot():
    condicion = True

    if not condicion:
        print("La condicion es false")
    else:
        print("La condicion es verdadera")

    #Lo que hace not es cambiar la condicion si es true la pasa a ser false y viceversa

def opin():
    lista = [1,2,3,4,5]

    print(3 in lista)
    #En este caso el 3 si que se encuentra en la lista
    print(8 in lista)
    #En este caso sera falso ya que el 8 no se encuentra en la lista


#Bloque principal

opis()
opnot()
opin()
