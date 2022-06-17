import re
import os
import time
import datetime
from pathlib import Path
import math

inicio = time.time()

ruta='D:\\dev-projects\\Python\\python-Udemy\\Proyectos_PY\\descomprimirArchivos\\todoDescomprimido\\Mi_Gran_Directorio'

mi_serie = r'N\D{3}-\d{5}'

hoy = datetime.date.today()

numerosEncontrados= []

archivosEncontrados=[]

def buscarNumero(archivo, serie):
    esteArchivo=open(archivo, 'r')
    texto= esteArchivo.read()
    if re.search(serie, texto):
        return re.search(serie, texto)
    else:
        return ''

def crearListas():
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for a in archivo:
            resultado= buscarNumero(Path(carpeta,a),mi_serie)
            if resultado != '':
                numerosEncontrados.append(resultado.group())
                archivosEncontrados.append(a.title())

def mostrar():
    i=0
    print('-' * 50)
    print(f'Fecha de Búsqueda: {hoy.day}/{hoy.month}/{hoy.year}')
    print('\n')
    print('ARCHIVO\t\t\tNRO. SERIE')
    print('-------\t\t\t----------')
    for a in archivosEncontrados    :
        print(f'{a}\t{numerosEncontrados[i]}')
        i += 1
    print('\n')
    print(f'Números encotrados: {len(numerosEncontrados)}')
    fin = time.time()
    duracion = fin - inicio
    print(f'Duración de la búsqueda: {math.ceil(duracion)} segundos')
    print('-' * 50)

crearListas()
mostrar()

