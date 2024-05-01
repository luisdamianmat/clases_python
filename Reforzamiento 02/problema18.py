"""num=1
i=3
col_numeros = []
while num<16:
    if num%2 == 1:
        col_numeros.append(num)

    num = num + 1
print("lista: {}".format(col_numeros))
while 2<i<6:
    col_numeros.insert(i,3.0)
    i = i + 1

print("lista actualizada: {}".format(col_numeros))
del col_numeros[8]
print("lista nuevamente actualizada: {}".format(col_numeros))"""

lista=[]
for i in range(1,16):
    if i % 2 == 1:
        lista.append(i)
print(lista)
for i in range(2,5):
    lista.insert(i,3.0)
print(lista)

lista.insert(2,"mascota")
print(lista)







