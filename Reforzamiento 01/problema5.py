"""declaramos nuestra entrada"""

numero=float(input(("Digite el sueldo que desea verificar : $ " )))

"""planteamos la condicional y utilizamos el modulo para la division"""

if numero%2==0:
    print("El sueldo es par")
else:
    print("El sueldo es es impar")