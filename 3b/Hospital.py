"""
En un hospital hay diferentes tipos de personal: médicos, enfermeros y administrativos. De todos
guardamos su información básica (dni, nombre, dirección y teléfono), de los médicos almacenamos
también su especialidad, y de los enfermeros la planta en la que trabajan.
Al hospital acuden pacientes. De todos ellos se guarda un historial con su dni, nombre, dirección,
teléfono, y un conjunto de pruebas y consultas que hayan hecho en el hospital. De cada prueba o
consulta guardamos la fecha en que se hizo, y el médico que le atendió
Define las clases necesarias para el enunciado propuesto en un programa llamado Hospital.py. Define
un programa principal que cree un array de personal de hospital con varios médicos y enfermeros.
Define un paciente con sus datos, y dale de alta diversas pruebas realizadas por varios médicos.
Finalmente, trata de mostrar por pantalla los datos completos del paciente, incluyendo su historial de
pruebas.

"""

class Persona:
    def __init__(self, dni, nombre, direccion, telefono):
        self.dni = dni
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
    
class Medico(Persona):
    def __init__(self, dni, nombre, direccion, telefono, especialidad):
        super().__init__(dni, nombre, direccion, telefono)
        self.__especialidad = especialidad
        

class Enfermero(Persona):
    def __init__(self, dni, nombre, direccion, telefono, planta):
        super().__init__(dni, nombre, direccion, telefono)
        self.__planta = planta
        
class Administrativo(Persona):
    def __init__(self, dni, nombre, direccion, telefono):
        super().__init__(dni, nombre, direccion, telefono)

class Paciente(Persona):
    def __init__(self, dni, nombre, direccion, telefono):
        super().__init__(dni, nombre, direccion, telefono)
        self.historial = []

    def agregar_prueba(self, fecha, medico):
        self.historial.append({'fecha': fecha, 'medico': medico})


m1 = Medico("12345678A", "Pablo Garcia", "sfafaf", "6372890219", "Cardiologo")
e1 = Enfermero("12345678B", "Makapaka", "ddkkd", "6372937483", "Segunda planta")


p1 = Paciente("12345678C")
        
        