import requests

#palabra=input ("ingresa la palabra a buscar: ")
#url="https://dummyjson.com/products/search"
#respuesta=requests.get(url,params={"q":palabra})
#resultados=respuesta.json()['products']

#Imprimo los resultados 
#for item in resultados:
#    print(item["title"],"-", item["price"])

##lista de categorias
url_categoria="https://dummyjson.com/products/categories"
respuesta=requests.get(url_categoria)
categorias=respuesta.json()
print (categorias[:5])

#productos por categoria
url_categoria="https://dummyjson.com/products/categories"

respuesta= requests.get(url_categoria)
categorias= respuesta.json()
#print(categorias[:10])

for cat in categorias:
    print(cat["name"])


#PRODUCTOS POR CATEGORIAS

url_pruductos_categoria="https://dummyjson.com/products/category/laptops"
respuesta=requests.get(url_pruductos_categoria)
productos=respuesta.json()["products"]
print("="*50)
print ("lista de productos de la categoria laptops")
for item in productos:
    print(item["id"], "-",item["title"])