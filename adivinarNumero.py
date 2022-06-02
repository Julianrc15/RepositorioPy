from random import *

intentos=8
turnosfinal=0

aleatorio=randint(1,101)
print(aleatorio)

print("Bienvenido existe un numero entre 1 y 100 que debe adivinar en 8 turnos.")
print("\n")

print(f"Usted tiene {intentos} para adivinar, empecemos:")
print("********************************************************")
print("\n")

while intentos <= 8 and intentos >0 :

   
    numeroUsuario=int(input("Ingrese un numero: "))
    
    if numeroUsuario not in range(1,101):
        print ("Recuerde el rango permitido es de 1 - 100")
        print("\n")
    elif numeroUsuario > aleatorio:
            turnosfinal+=1
            intentos -= 1
            print ("El numero ingresado es mayor, intente de nuevo")
            print(f"Quedan {intentos} intentos para adivinar")
            print("\n")
    elif numeroUsuario < aleatorio:
            turnosfinal+=1
            intentos -= 1
            print ("El numero ingresado es menor, intente de nuevo")
            print(f"Quedan {intentos} intentos para adivinar")
            print("\n")
    else:
        print ("Felicitaciones adivinó el número")
        turnosfinal+=1
        
        print(f"Le tomo {turnosfinal} intentos para adivinar")
        intentos=0
        break;

if numeroUsuario != aleatorio:
    print(f"Lo siento, se han agotado los intentos. El numero secreto era {aleatorio}")




