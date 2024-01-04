def suma(*args):
    total = 0
    for num in args:
        total += num
    return total

suma1 = suma(1,2,3,4,5)
suma2 = suma(10,20,30)

print("Primera suma: ", suma1)
print("Segunda suma: ", suma2)
