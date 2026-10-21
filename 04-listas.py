#crear listas de datos
estudiantes=["juan","pedro","luis","maria","sofia"]

#mostrar un elemento de la lista
print(estudiantes [1])
print(estudiantes [4])

#agregar un elemento a la lista
estudiantes.append("ana")
print(estudiantes [5])

#eliminar a un elemnto
estudiantes.remove("luis")
estudiantes.remove("pedro")

#mostrar el tamaño de la lista
print(len(estudiantes))

#mostrar todos los elemntos de la lista
print("Lista de estudiantes")
for estudiante in estudiantes:
    print(estudiante)