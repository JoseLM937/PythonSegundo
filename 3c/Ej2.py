import os.path

imagen = input("Escribe el nombre de la imagen: ")
alto = 1
ancho=1

if os.path.isfile( imagen):
    print("Existe")
    while alto!=0 and ancho!=0:
        print("Si tecleas un 0 en cualquier de las opciones el programa acabara")
        ancho = int(input("Introduce el ancho de la foto"))
        alto = int(input("Introduce el alto de la foto"))
        tamano = (ancho, alto)
        redi = imagen.resize(tamano)
else:
    print("No existe")