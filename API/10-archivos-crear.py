import os
directorio=os.path.dirname(os.path.abspath(__file__))

with open("frutas.txt","w") as archivo:
    archivo.write("naranja\n")
    archivo.write("sandia\n")
    archivo.write("fresa\n")


archivo_frutas=os.path.join(directorio,"frutas.txt")
with open(archivo_frutas,"r") as frutas:
    contenido=frutas.read()
    print(contenido)