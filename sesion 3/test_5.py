lista=[1,2,3,4,5,6]
suma=0
for numero in lista:
    suma=numero+suma
    #print(suma)---> presentaria la suma encadena de cada elemento: 1+0,1+2,1+2+3,...,1+2+3+4+5+6.
print("mi lista :{}".format(lista))
print("la suma de mi lista es: {}".format(suma))