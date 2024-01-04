def factorial(num):
    if 0 <= num <= 10:
        resul = 1
        for valor in range(1, num+1):
            resul *= valor
        return resul
    else:
        return("El numero no esta entre el rango 0 y 10")


