import math

def area_triangulo(base: float, altura: float):

    if ((base > 0)&(altura>0)):
        area = base * altura / 2
        print(f"El area del triangulo es: {area}")
    else:
        print("La base y la altura deben ser mayores de 0")

def area_circulo(radio: float):

    if (radio > 0):
        area = math.pi*(radio**2)
        print(f"El area del circulo es: {area}")
    else:
        print("El radio debe ser mayor 0")

area_triangulo(4,3)
area_circulo(4)

