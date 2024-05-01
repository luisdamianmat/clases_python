"""Usando las propiedades de cadenas o string"""

"""
Requisitos:

- Ingresar tu nombre y apellido por consola (cada valor 
tiene que estar en una variable disintinta)
- Concatener ambos valores en una sola variable
- Obtener y mostrar el tamaño del nombre completo
- Imprimir el resultado final todo en mayúsculas
- Indicar mediante condicionales si el tamaño del nombre es 
mayor o no al del apellido (ingresar solo para este caso el 
apellido paterno)

"""
nom=input("Ingrese su nombre: ")
apel=input("Ingrese su apellido: ")

nom_apel="nombre completo es:" + nom + " " + apel
print(nom_apel)
tam_nom="tamaño del nombre completo es: {}".format(len(nom+apel))
print(tam_nom)
print("el nombre completo en mayusculas es: {}".format(nom.upper()+" "+apel.upper()))

if len(nom)>len(apel):
    print("el tamaño del nombre es menor que el apellido")
elif len(nom) == len(apel):
    print("el nombre y apellido tienen el mismo tamaño")
else: print("el tamaño del apellido es mayor que el nombre")