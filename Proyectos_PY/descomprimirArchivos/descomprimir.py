import shutil

origen='D:\\dev-projects\\Python\\python-Udemy\\Proyectos_PY\\descomprimirArchivos\\Proyecto+Dia+9.zip'

destino= 'D:\\dev-projects\\Python\\python-Udemy\\Proyectos_PY\\descomprimirArchivos\\todoDescomprimido'

# shutil.make_archive(destino,'zip', origen)

shutil.unpack_archive(origen, destino, 'zip')