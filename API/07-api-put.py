#ACTUALIZAR EL PRODUCTO
import requests

producto_modificado={
    "price":123.43
}

url="https://dummyjson.com/products/1"
respuesta=requests.put(url, json=producto_modificado)
print(respuesta.status_code)
print (respuesta.json())