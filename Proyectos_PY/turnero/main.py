"""
Este programa debe de asignar turnos para diferentes areas de una farmacia
-Perfumeria
-Drogueria
-Cosmetica
"""





from numeros import numeros


def saludo():
    print("Bienvenido a la farmacia Python")

    numeros.asignar_turno(numeros.elegir_area())

        
def inicio():

    while True:
        saludo()
        try:
                otro_turno = input("Quieres sacar otro turno? [S] [N]: ").upper()
                ["S", "N"].index(otro_turno)
        except ValueError:
                print("Esa noes una opción válida")
        else:
            if otro_turno == "N":
                print("Gracias por su visita")
                break

inicio()
            