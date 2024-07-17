''' Cubilla Damian - 1H
12. Crea un diccionario que represente una lista de las compras. 
Cada clave del diccionario debe ser el nombre de un producto y 
cada valor debe ser su cantidad. Pedir al usuario que ingrese el 
nombre del producto e imprimir la cantidad
'''
dict_productos = {"harina":1200, "leche":800, "fideos":1000}
producto_ingresado = input("Ingrese producto: ")
for elemento in dict_productos.keys():
    if(elemento == producto_ingresado):
        print(f"El precio de {producto_ingresado} es: {dict_productos[elemento]}")