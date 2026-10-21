import requests
idreceta=input("Ingresa el ID de la receta")
respuesta=requests.get(f"https://dummyjson.com/recipes/{idreceta}")

if(respuesta.status_code==200):
    print(respuesta.status_code)#200
    #imprmir un diccionaro de python con la receta 1
    print(respuesta.json())
    receta=respuesta.json()
    print("="*50)
    print(receta['name'])
    print("ingredientes:")
    for item in receta['ingredients']:
        print("-"+ item)
    print("="*50)
else:
    print("La receta no existe")