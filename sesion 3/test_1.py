nombre=input('Ingrese el nombre del empleado: ')
apellido=input('Ingrese el apellido del empleado: ')
distrito=input('Ingrese el distrito del empleado: ')
sueldo=input('Ingrese el sueldo del empleado: ')

bono=(float(sueldo)*3)-(float(sueldo)*0.1)

lista_final=[nombre,apellido,distrito,sueldo]

nombre,apellido,distrito,sueldo=lista_final

print("Su nombre completo es {}, reside en el distrito de {} y percibe un sueldo de {} al mes por lo que recibe un bono final de {}".format(nombre,distrito,sueldo,bono))

