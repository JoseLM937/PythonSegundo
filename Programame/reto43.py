def esPalindromo(texto):
    texto = texto.replace(" ","").lower()

    return texto == texto[::-1]


