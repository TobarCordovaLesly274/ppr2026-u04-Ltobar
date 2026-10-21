import requests

respuesta=requests.get("https://dummyjson.com/recipes/")
datos=respuesta.json()
#imprimir el total de recetas
print(f"Total de recetas: {datos['total']}")
#total de elementos de la lista actual
print(len(datos['recipes']))
#imprimir la lista de recetas
#print(datos['recipes'])
#imprimir lista de receta con parametros
parametro={"limit":5, "select":"name,rating"}
respuestafiltrada=requests.get("https://dummyjson.com/recipes", params=parametro)
print(respuestafiltrada.json())
for item in respuestafiltrada:
    print(item)