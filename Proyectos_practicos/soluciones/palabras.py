
def palabras(palabra):
    unicos=set()
    
    for letra in palabra:
        unicos.add(letra)
    
    lista=list(unicos)
    lista.sort()

    return lista

r=palabras("entretenido")
print (r)