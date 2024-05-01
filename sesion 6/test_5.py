"""manejo de error"""
"""
-crear un funcion aplicando excepciones donde el bloque de except va a considerar
a los errors de division entre 0 y el tipo de error
-los valores deben ser ingresados en consola"""
a = int(input("Introduzca un numero: "))
b = int(input("Introduzca un numero: "))
def division(a,b):

    try:
        result = a/b
        return print("El resultado es ", result)
    except (ZeroDivisionError,TypeError):
        print("Vuelva a intentarlo")

division(a,b)
