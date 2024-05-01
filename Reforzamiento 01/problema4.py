"""declaramos la entrada y definimos la constante pi"""
radio = float(input('Ingrese un número: '))

pi = 3.14159
"""creamos una variable que realice la operacion"""
volumen = 4/3 * pi * pow(radio,3)

"""imprimiendo"""

print("El volumen de la esféra es: {} ".format(f"{volumen:.4f}"))
