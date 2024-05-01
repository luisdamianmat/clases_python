sueldo=float(input("Ingrese el sueldo del empleado: "))

final = "El empleado no tiene bonificacion" if sueldo>3000  else "El empleado tiene bonificacion este año"
print(final)