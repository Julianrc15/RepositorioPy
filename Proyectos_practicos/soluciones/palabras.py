
def palabras(palabra):
    lista=list(palabra.lower())
    lista.sort()
    unicos=set(lista)

    return unicos

r=palabras("entretenido")
print (r)