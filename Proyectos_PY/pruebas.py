def suma_cuadrados(*args):
    suma=0
    for i in args:
        suma+=pow(i, 2)

    return (suma)
    
print (suma_cuadrados(1,2,3))