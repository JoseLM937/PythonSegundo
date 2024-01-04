#Funcion para gestionar el orden de salida por pantalla de los datos
def calcular_sueldo(nombre,costohora,cantidadhoras):
    sueldo=costohora*cantidadhoras
    print(nombre,"trabajo",cantidadhoras,"y cobra un sueldo de",sueldo)


# bloque principal
#No importa la posicion en la que pongamos los datos ya que nos podemos referir a el igualando la variable
calcular_sueldo("juan",10,120)
calcular_sueldo(costohora=12,cantidadhoras=40,nombre="ana")
calcular_sueldo(cantidadhoras=90,nombre="luis",costohora=7)
