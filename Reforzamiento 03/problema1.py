"""Pedir dos números positivos mediante terminal al usuario. Mostrar
como salida el número cuya sumatoria de dígitos es el mayor y los
números cuya sumatoria de dígitos es menor que 10. Utilizar una o
más funciones, según sea conveniente."""


def sum_dig(numero):
    suma = 0
    while numero != 0:
        digito = numero % 10
        suma = suma + digito
        numero = numero // 10
    return suma

mayor = 0
numero1 = int(input("digite un número positivo: "))
numero2= int(input("ingrese otro número positivo: "))

while numero1 < 0 or numero2 < 0:
    print("digite nuevamente los numeros")
    numero1 = int(input("digite: "))
    numero2 = int(input("digite: "))

if numero1 >= 0 and numero2 >= 0:
    suma = sum_dig(numero1)
    suma1 = sum_dig(numero2)
    if suma > suma1:
        mayor = suma
        num_mayorsuma = numero1
    if suma < suma1:
        mayor = suma1
        num_mayorsuma = numero2
    if suma < 10 or suma1 <10:
        if suma<10:
            cantidad_veces=1
        if suma1<10:
            cantidad_veces=1
        if suma<10 and suma1<10:
            cantidad_veces=2

        print("Cantidad con sumatoria menor a 10: {} ".format(cantidad_veces))
    else:print("Ambas sumatorias de digitos son mayores que 10")


print("Sumatoria de dígitos de {} que es: {} es la mayor" .format(num_mayorsuma, mayor))


