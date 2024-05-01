var1=input("Ingrese su nombre: ")
var2=input("Ingrese su apellido: ")

name_completo="mi nombre completo es:" + var1 +" "+ var2
print(name_completo)
print("tamaño del nombre completo es:{}".format(len(var1+var2)))
print("nombre completo en mayusculas es:{}".format(var1.upper()+" "+var2.upper()))

if len(var1)>len(var2):
    print("el tamaño del nombre es mayor que el apellido")
else: print("el tamaño del apellido es mayor que el nombre")