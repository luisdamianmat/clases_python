"""crear una funcion aplicando excepciones donde no se pueda realizar una suma de diferentes tipos de datos"""

def operaciones(a,b):
    try:
        resultado=a/b
        print(resultado)
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
    except TypeError:
        print("No se puede sumar un str con int")

operaciones(1,"hola")
operaciones(2,0)
operaciones(13.4,5)