

def asignar_perfumeria():
    for n in range(1,100):
        yield f"P - {n}"

def asignar_drogueria():
    for n in range(1,100):
        yield f"D - {n}"

def asignar_costmeticos():
    for n in range(1,100):
        yield f"C - {n}"

p= asignar_perfumeria()
d= asignar_drogueria()
c= asignar_costmeticos()



def elegir_area():
    area = int(input(""" Por favor elija un area:
    [1] - Perfumeria
    [2] - Drogueria 
    [3] - Cosmetica
    [4] - Salir
    """))
    return area

def asignar_turno(area):

    print("\n" + "*" * 23)
    print("Su número es:")
    if area == 1:
       print(next(p))

    elif area == 2:

        print(next(d))

    elif area == 3:

        print(next(c))

    elif area == 4:

        pass

    print("Aguarde y será atendido")
    print("*" * 23 + "\n")


        


