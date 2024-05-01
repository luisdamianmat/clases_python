"""Programación funcional en Python"""

"""
Requisitos:
- Solicitar al usuario 4 números por consola
-  Crear una función que devuelve cuál es el número mayor de 
los 4 ingresados por el usuario
- Finalmente elevar al cubo el resultado y mostrarlo 
por consola
"""


def mayor(num1,num2,num3,num4):
    if num1 > num2 and num1 > num3 and num1 > num4:
        return num1
    elif num2 > num1 and num2 > num3 and num2 > num4:
        return num2
    elif num3 > num1 and num3 > num2 and num3 > num4:
        return num3
    else: return num4

num1=float(input("Ingrese un numero: "))
num2=float(input("Ingrese un numero: "))
num3=float(input("Ingrese un numero: "))
num4=float(input("Ingrese un numero: "))

print("El mayor numero es:{}".format(mayor(num1,num2,num3,num4)))

cubo=pow(mayor(num1,num2,num3,num4),3)
print("El cubo es:{}".format(cubo))

