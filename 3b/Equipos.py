"""
Ejercicio 2: Escribe una nueva versión del ejercicio anterior en un programa llamado Equipos.py donde,
además de la clase Jugador haya una segunda clase llamada Equipo , cuyo único atributo será el
nombre del equipo (texto), junto con un constructor para darle valor . Haz que cada jugador pueda
pertenecer a un equipo añadiendo un atributo Equipo a la clase Jugador. En el programa principal, crea
un jugador y un equipo, y asigna el equipo al jugador. Muestra por pantalla la información del jugador,
incluyendo el equipo
"""
class Equipo:
    def __init__(self, nombre):
        self.__nombre = nombre

    #Getter
    @property
    def nombre(self):
        return self.__nombre

class Jugador:
    e1: Equipo
    def __init__(self,dorsal,nombre,e):
        self.__nombre = nombre
        self.__dorsal = dorsal
        self.e1 = e

    def mostrar(self):
        print(self.__dorsal,". ",self.__nombre, ". ", Equipo(self.e1))


    
    



        
e1 = Equipo("Torrent")
e2 = Equipo("Valencia")
j1 = Jugador(16, "Pau Gasol", e1)
j2 = Jugador(18, "Makapaka", e2)
j1.mostrar()
j2.mostrar()