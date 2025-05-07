import random

rango_inferior = int(input("Ingrese el rango inferior de la busqueda: "))
rango_superior = int(input("Ingrese el rango superior de la busqueda: "))

zona = random.randint(rango_inferior, rango_superior)

busqueda = int(input("ingrese el sector de su busqueda: "))
intento = 0
#intento 1

if busqueda == zona:
    print("¡Tesoro encontrado! ¡Felicidades, pirata!")
else:
    print("siga buscando")
    intento += 1
    busqueda = int(input("ingrese el sector de su busqueda: "))
#intento 2

if intento == 1:
    if busqueda == zona:
        print("¡Tesoro encontrado! ¡Felicidades, pirata!")
    else:
        if intento == 1:
            distancia = abs(busqueda - zona)
            if distancia >= 3 or distancia <= 3:
                print("muy cerca")
                intento += 1
            else:
                print("muy lejos")
                intento += 1
            busqueda = int(input("ingrese el sector de su busqueda: "))

#intento 3
if intento == 2:
    if busqueda == zona:
        print("¡Tesoro encontrado! ¡Felicidades, pirata!")
    else:
        print("El tesoro seguira perdido para siempre")

