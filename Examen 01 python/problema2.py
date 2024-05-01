"""Reglas:
- Crear una lista con 10 valores random o aleatorios (Pista: Usar el método
append y for)
- Llenar otra lista con sus cubos.
- Llenar una lista nueva con sus cuadrados.
- Mostrar de manera inversa la suma de ambas listas creadas."""
lista=[]
lista_2=[]
lista_3=[]
i=1
while i<11:
    dato=int(input("Ingrese un dato: "))
    lista.append(dato)
    i=i+1
print("mi lista de datos digitados aleatoriamente: {}".format(lista))

for i in lista:
    cua=pow(i,2)
    lista_2.append(cua)
print("lista nueva con sus cuadrados: {}".format(lista_2))

for i in lista:
    cubo=pow(i,3)
    lista_3.append(cubo)
print("lista nueva con sus cubos: {}".format(lista_3))

suma_de_listas=lista_2+lista_3

suma_de_listas.reverse()

print("La suma de las dos ultimas listas pero invertida es: {}".format(suma_de_listas))