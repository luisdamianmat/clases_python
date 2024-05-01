"""creando diccionario"""
nombre= str(input("Ingresa su nombre: "))
sueldo=float(input("Ingrese su sueldo: $"))
edad= int(input("Ingrese su edad: "))
mi_diccionario= {"nombre":nombre, "sueldo":sueldo, "edad":edad}

print("mi diccionario era: {}".format(mi_diccionario))

mi_diccionario["DNI"]=72812812

print("mi nuevo diccionario es: {}".format(mi_diccionario))