lista=[]
i=1
sum=0
j=0
while i<=10:
    dato=int(input("Digite un valor : "))
    lista.append(dato)
    i=i+1
while j<10:
    sum = lista[j] + sum
    j=j+1
media_valor=sum/len(lista)

print("mi lista con los datos digitados es: {}".format(lista))
print("La suma de los datos de la lista es: {}".format(sum))
print("La media de la lista es: {}".format(float(media_valor)))
