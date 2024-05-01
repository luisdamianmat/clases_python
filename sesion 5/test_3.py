"""Programación funcional en Python"""

"""
Requisitos:
- Un usuario ingresará 2 números por consola
- En una función obtener si el segundo número 
ingresado es múltiplo del primo o viceversa
- Retornar quién fue múltiplo de quién
"""

a=int(input("digite un numero: "))
b=int(input("digite un numero: "))

def multiplo(x,y):
    if x%y==0:
        return print(f"{x} es multiplo de {y}")
    elif y%x==0:
        return print(f"{y} es multiplo de {x}")
    else: return print(f"{x} y {y} no son multiplos")

print(multiplo(a,b))
