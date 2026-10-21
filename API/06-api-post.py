import requests
nueva_producto={
    "title": "audifonos LITIID43",
    "price":123.45,
    "category":"electronics"
}
url="https://dummyjson.com/products/add"
respuesta=requests.post(url, json=nueva_producto)
print ("codigo de respuesta:"+ str(respuesta.status_code))
print (respuesta.json())