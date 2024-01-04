def cargar_empleados():
    empleados=[]
    for x in range(5):
        nombre=input("Ingrese el nombre del empleado")
        su1=int(input("Ingrese primer sueldo"))
        su2=int(input("Ingrese segundo sueldo"))
        su3=int(input("Ingrese tercer sueldo"))
        empleados.append([nombre(su1,su2,su3)])
    return empleados

def ganancias(empleados):
    print("Monto total ganado por empleado en los ultimos 3 meses")
    for x in range(5):
        total=empleados[x][1][0]+empleados[x][1][1]+empleados[x][1][2]
        print(empleados[x][0], total)

def ganancias_superior10000(empleados):
    print("Empleados con ingresos superiores a 10000 en los ultimos 3 meses")
    for x in range(5):
        total=empleados[x][1][0]+empleados[x][1][1]+empleados[x][1][2]
        if total>10000:
            print(empleados[x][0], total)


#Bloque principal
empleados=cargar_empleados()
ganancias(empleados)
ganancias_superior10000(empleados)
