lista = [
    [150,80],
    [180,20],
    [170,30],
    [140,40],
    [180,80],
]

def keyFunction(elemento):
    return(-elemento[0],-elemento[1])


listaOrdenada = sorted(lista, key=keyFunction)

for elemento in listaOrdenada:
    print(f"Tamaño: {elemento[0]}, peso: {elemento[1]}")


"""
La Key Function en este caso nos sirve para determinar el orden de los elementos
ya que hemos podido ordenarlo mediante los numeros del principio y en caso de ser
el mismo numero diferenciaarlos con los segundos
"""
