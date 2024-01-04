import random

class Car:
    def __init__(self, matricula, color):
        self.matricula = matricula
        self.color = color

    def imprimir(self):
        print(f"Matrícula: {self.matricula}, Color: {self.color}")

    def metodo2(self):
        print("Metodo para probar")

    def metodo_adicional(self):
        print("Segundo metodo para probar")

# Programa principal
n = int(input("Ingrese el número de instancias a crear: "))
instancias_car = []
colores_disponibles = ["red", "white", "black", "pink", "blue"]

for i in range(1, n + 1):
    matricula = i
    color = random.choice(colores_disponibles)
    instancia = Car(matricula, color)
    instancias_car.append(instancia)

# Imprimir los valores de las instancias creadas
print("\nValores de las primeras 10 instancias:")
for car_instance in instancias_car:
    car_instance.imprimir()
