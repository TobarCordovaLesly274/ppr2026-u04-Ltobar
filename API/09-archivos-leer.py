import os
directorio=os.path.dirname(os.path.abspath(__file__))
archivo=os.path.join(directorio,"lista_estudiantes_reprobados.txt")  
#para leer todo el archivo
with open(archivo,"r") as lista: #la r es el permiso en este caso r=leer y w para ecribir
    contenido=lista.read()
    print(contenido)


