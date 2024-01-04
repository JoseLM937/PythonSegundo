#Nos va a devolver la longitud de la cadena para poder saber cual es mas larga
def largo(cadena):
    return len(cadena)


# bloque principal

nombre1=input("Ingrese primer nombre:")
nombre2=input("Ingrese segundo nombre:")
la1=largo(nombre1)
la2=largo(nombre2)
#En esta parte sencillamente miramos cual es el mas largo o si son iguales
if la1==la2:
    print("Los nombres:",nombre1,nombre2,"tienen la misma cantidad de caracteres")
else:
    if la1>la2:
        print(nombre1,"es mas largo")
    else:
        print(nombre2,"es mas largo")
