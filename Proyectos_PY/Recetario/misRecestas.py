import os
from pathlib import Path    
from os import system

mi_ruta=Path(Path.home(),"Recetas")

def contar_recetas(ruta):
    contador=0
    for txt in Path(ruta).glob("**/*.txt"):
        contador +=1

    return contador

def inicio():
    system("cls")
    print('*'*50)
    print('*'*5+" Bienvenido al administrador de recetas "+'*'*5)
    print('*'*50)
    print('\n')
    print(f"Las recetas se encuentran en {mi_ruta}")
    print(f"Total de recetas: {contar_recetas(mi_ruta)} ")

    eleccion ='x'
    while not eleccion.isnumeric() or int(eleccion) not in range(1,7):
        print("Elige una opcion")
        print('''
        [1] - leer receta
        [2] - Crear receta nueva
        [3] - Crear categoria nueva
        [4] - Eliminar receta
        [5] - Eliminar categoria
        [6] - Salir del programa
        ''')
        eleccion = input()

    return int(eleccion)


def mostrar_categorias(ruta):
    print("Categorias")
    ruta_categorias=Path(ruta)
    lista_categorias=[]
    contador=1

    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] - {carpeta_str}")
        lista_categorias.append(carpeta)
        contador += 1

    return lista_categorias

def elegir_categoria(lista):
    elecion_correcta='x'
    while not elecion_correcta.isnumeric() or int(elecion_correcta)not in range(1,len(lista )+1):
        elecion_correcta = input("\nElije una categoria: ")
    return lista[int(elecion_correcta)-1]

def mostrar_recetas(ruta):
    print("Recetas:")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1

    for receta in ruta_recetas.glob("*.txt"):
        receta_str = str(receta.name)
        print(f"[{contador}] - {receta_str}")
        lista_recetas.append(receta)
        contador+=1
    return (lista_recetas)

def elegir_receta(lista):
    elecion_correcta='x'
    while not elecion_correcta.isnumeric() or int(elecion_correcta)not in range(1,len(lista )+1):
        elecion_correcta = input("\nElije una receta: ")
    return lista[int(elecion_correcta)-1]

def leer_receta(receta):
    print(Path.read_text(receta))

def crear_receta(ruta):
    existe= False

    while not existe:
        print("Escribe el nombre de la receta: ")
        nombre_receta=input() +'.txt'
        print("Escribe tu nueva receta:")
        contenido_receta=input()
        ruta_nueva= Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f"Tu receta {nombre_receta} ha sido creada")
            existe= True
        else:
            print("Esta receta ya existe")

def crear_categoria(ruta):
    existe= False

    while not existe:
        print("Escribe el nombre de la categoria: ")
        nombre_categoria=input() +'.txt'
        
        ruta_nueva= Path(ruta, nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva,)
            print(f"Tu Categoria {nombre_categoria} ha sido creada")
            existe= True
        else:
            print("Esta categoria ya existe")

def eliminar_receta(receta):
    Path(receta).unlink()
    print(f"la receta {receta} ha sido eliminada")

def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f"la receta {categoria} ha sido eliminada")

def volver_inicio():
    eleccion_regresar="x"

    while eleccion_regresar.lower() != 'v':
        eleccion_regresar = input("\n Presione Vpara volver al menú: ")

finalizar_programa= False

while not finalizar_programa:

    menu=inicio()

    if menu ==1:
        mis_Categorias=mostrar_categorias(mi_ruta)
        mi_categoria=elegir_categoria(mis_Categorias)
        mis_recetas=mostrar_recetas(mi_categoria)
        mi_receta= elegir_receta(mis_recetas)
        leer_receta(mi_receta)
        volver_inicio()
    
    elif menu==2:
        mis_Categorias=mostrar_categorias(mi_ruta)
        mi_categoria=elegir_categoria(mis_Categorias)
        crear_receta(mi_categoria)
        volver_inicio()
    
    elif menu ==3:
        crear_categoria(mi_ruta)
        volver_inicio()
        
    elif menu ==4:
        mis_Categorias=mostrar_categorias(mi_ruta)
        mi_categoria=elegir_categoria(mis_Categorias)
        mis_recetas=mostrar_recetas(mi_categoria)
        mi_receta= elegir_receta(mis_recetas)
        eliminar_receta(mi_receta)
        volver_inicio()
    
    elif menu == 5:
        mis_Categorias=mostrar_categorias(mi_ruta)
        mi_categoria=elegir_categoria(mis_Categorias)
        eliminar_categoria(mi_categoria)
        volver_inicio()
    
    elif menu == 6:
        system("cls")
        finalizar_programa = True
    
