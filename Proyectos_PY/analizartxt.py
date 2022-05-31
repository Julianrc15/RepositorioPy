texto=input("Por favor ingrese el texto que desea analizar: ").lower()
listaletras=[]
listaletras.append(input("ingrese la primera letra: ").lower())
listaletras.append(input("ingrese la segunda letra: ").lower())
listaletras.append(input("ingrese la tercera letra: ").lower())

cantidadLetras2=texto.count(listaletras[1])
cantidadLetras1=texto.count(listaletras[0])
cantidadLetras3=texto.count(listaletras[2])

print("\n")

listatexto=list(texto.split(" "))
palabrasTotal=len(listatexto)


textoinverso=listatexto[::-1]
primeraLetra=listatexto[0][0]
ultimaLetra=listatexto[-1][-1]

if ("python" in listatexto):
    pythonWord=texto.count("python")
else:
    pythonWord=0

print(f"Hemos encontrado la letra {listaletras[0]} repetida {cantidadLetras1} veces")
print(f"Hemos encontrado la letra {listaletras[1]} repetida {cantidadLetras2} veces")
print(f"Hemos encontrado la letra {listaletras[2]} repetida {cantidadLetras3} veces")

print("\n")

print(f"El total de palabras en el texto es de: {palabrasTotal}")
print("\n")
print(f"La primera letra del texto es de: {primeraLetra}, la última letra del texto es: {ultimaLetra},")
print("\n")
print(f"El texto se leería de manera invertida así:{textoinverso}")
print("\n")
print(f"La cantidad de veces que aparece la palabra Python en el texto es de: {pythonWord}")
print("\n")
