import hashlib

def generarHash(contra):
    return hashlib.sha256(contra.encode()).hexdigest()

def listas():
    lista = []
    valor = 0

    lista.append(["paco", generarHash("Amm23")])
    lista.append(["marcos", generarHash("All2")])
    lista.append(["patri", generarHash("Kslw2")])
    lista.append(["maria", generarHash("porque")])
    lista.append(["segismundo", generarHash("contrasena")])

    while valor!= 2:
        usuario = input("Introduce el usuario a buscar")
        for usu, contraHash in lista:
            if usu == usuario:
                print(f"Contraseña para {usu}: {contraHash}")

            else:
                print(f"No se encontro el usuario {usu}")
        valor = valor +1
    
def diccionarios():
    lista = {}
    valor = 0

    lista["paco"] = generarHash("Amm23")
    lista["marcos"] = generarHash("All2")
    lista["patri"] = generarHash("Kslw2")
    lista["maria"] = generarHash("porque")
    lista["segismundo"] = generarHash("contrasena")

    while valor!= 2:
        usuario = input("Introduce el usuario a buscar")
        if usuario in lista:
                contraHash = lista[usuario]
                print(f"Contraseña para {usuario}: {contraHash}")

        else:
                print(f"No se encontro el usuario {usuario}")
        valor = valor +1


#Bloque principal

print("Con listas")
listas()

print("Con diccionarios")
diccionarios()
