estudiante={
    "nombre": "juan",
    "edad":20,
    "grupo":"LITIID43",
    "promedio":9.3
    
}
#modificar elemento
estudiante["promedio"]=7.2

#agregando indice al diccionario
estudiante["matricula"]="25390010"

#imprimir un elemento de diccionario
print("="*50)
print("matricula:"+ estudiante["matricula"])
print("nombre del estudiante:" + estudiante["nombre"])
print("grupo:"+estudiante["grupo"])
print("promedio:"+ str(estudiante["promedio"]))
print("="*50)

#mostrar todo el contenido del diciionario
for clave, valor in estudiante.items():
    print(f"{clave}:{valor}")