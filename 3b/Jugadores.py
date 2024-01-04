"""
Escribe un programa en Python llamado Jugadores.py que defina una clase llamada Jugador , con
atributos dorsal (numérico) y nombre (texto). Define el constructor para darles valor y un método que
muestre la información de un jugador con el formato dorsal. Nombre. . Por ejemplo:
16. Pau Gasol . En el programa principal, crea un par de jugadores con sus datos, y muestra su
información por pantalla.

"""

class Jugador:
    def __init__(self,dorsal,nombre):
        self.__nombre = nombre
        self.__dorsal = dorsal

    def mostrar(self):
        print(self.__dorsal,". ",self.__nombre)


j1 = Jugador(16, "Pau Gasol")
j2 = Jugador(18, "Makapaka")
j1.mostrar()
j2.mostrar()