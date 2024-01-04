



def menorMayor(numero):
    if numero > 49 and numero < 1:
        return True
    
lista = int(input("Introduce los 6 numeros de la loteria separados por espacios: ").split(" ")) 
lista1 = []
lista1 = lista
lista1.sort()
for i in range (len(lista)):
    if menorMayor(lista[i]) == True:
        print("La lista no es valida")
    else:
        print(lista1)
   
