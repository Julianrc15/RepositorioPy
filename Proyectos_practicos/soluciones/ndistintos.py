
def devolver_distintos(n1,n2,n3):
    lista=[]
    lista.append(int(n1))
    lista.append(int(n2))
    lista.append(int(n3))
   
    suma= sum(lista)

    numeroMayor=max(lista)
    numeroMenor=min(lista)
    valor_medio=(sum(lista)-numeroMenor-numeroMayor)

    if suma in range(10,16):
        return(valor_medio)
    elif suma>15:
        return(numeroMayor)
    else:
        return(numeroMenor)

r= devolver_distintos(3,6,1)
print (r)

