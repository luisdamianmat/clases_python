"""creando diccionario"""
nombre= str(input("Ingresa su nombre: "))
sueldo=float(input("Ingrese su sueldo: $"))
edad= int(input("Ingrese su edad: "))
mi_diccionario= {"nombre":nombre, "sueldo":sueldo, "edad":edad}
lista_diccionario=list(mi_diccionario)
print("mi diccionario convertido en lista es: {}".format(lista_diccionario))
