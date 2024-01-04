"""
Crea un programa llamado Contar.py que reciba como parámetros del programa principal dos datos
(numéricos) y realice un conteo desde el primero hasta el segundo. Si no se reciben los dos datos
mostraremos un mensaje de error y finalizaremos.

"""

import sys
try:
    for i in range(sys.argv[1], sys.argv[2]):
        print(sys.argv[i])
except:
    print("Error con los datos añadidos")

