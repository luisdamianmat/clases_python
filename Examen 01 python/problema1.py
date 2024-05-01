"""Reglas:
- Pedir por consola nombre, apellido y edad de un usuario. Mostrar en consola el
nombre completo del trabajador
- Edad tiene que ser tipo entero, para esto apoyarse de la conversión de datos
- Identificar los tipos de datos ingresados y mostrarlos en pantalla.
- Pedir los nombres y edades para dos trabajadores y finalmente
agregarlos a una lista. Mostrar la suma de las edades de los
trabajadores localizándolos por la posición en la lista."""
#CORREGIDO
lista_trabajadores=[]
nombre=input("Ingrese el nombre del trabajador: ")
apellido=input("Ingrese el apellido: ")
edad=int(input("Ingrese el edad: "))

completo="El nombre completo del trabajador es: "+nombre + " " +apellido
print(completo)
print("tipos de datos ingresados es: {} {} {}".format(type(nombre),type(apellido),type(edad)))
i=0
sum=0
while i<2:
    nombre1=input("Ingrese el nombre del trabajador nuevo: ")
    edad1=int(input("Ingrese el edad: "))
    lista_trabajadores.append([nombre1])
    lista_trabajadores.append([edad1])
    sum=sum+edad1
    i+=1

print("mi lista de trabajadores nuevos es: {}".format(lista_trabajadores))
#print("la suma de edades de los nuevos trabajadores: {}".format(sum))
"""solo falta definir como sumar las edades que se encuentran en mi lista de trabajadores."""







