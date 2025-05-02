import random

print("¡Bienvenido a la Isla Aleatoria!")

inicio = int(input("Ingrese el límite inferior del rango de zonas: "))
fin = int(input("Ingrese el límite superior del rango de zonas: "))


while inicio >= fin:
    print("El límite inferior debe ser menor que el límite superior. Intente nuevamente.")
    inicio = int(input("Ingrese el límite inferior del rango de zonas: "))
    fin = int(input("Ingrese el límite superior del rango de zonas: "))

intentos_max = int(input("¿Cuántos intentos desea tener?: "))

zona_tesoro = random.randint(inicio, fin)
intento = 1
acertado = False

print(zona_tesoro)

while intento <= intentos_max:
    eleccion = int(input(f"Intento {intento} - Elige una zona entre {inicio} y {fin}: "))
    
    if eleccion == zona_tesoro:
        print(f"¡Felicidades! Has encontrado el tesoro en la zona {zona_tesoro}.")
        acertado = True
        break
    else:
        if intento == 2:
            distancia = abs(eleccion - zona_tesoro)
            if distancia <= 2 or distancia >= 2:
                print("¡Estás muy cerca del tesoro!")
            elif distancia <= 1 or distancia >= 1:
                print("¡Estás muy, muy cerca del tesoro!")
            elif distancia <= 5 or distancia >= 5:
                print("Estás cerca, pero no tanto...")
            elif distancia <= 10 or distancia >= 10:
                print("Estás un poco lejos del tesoro.")
            elif distancia <= 25 or distancia >= 25:
                print("Estás lejos pero cerca del tesoro.")
        else:
            print("Estás lejos del tesoro.")

        intento += 1

if acertado == False:
    print("El tesoro seguirá perdido por siempre...")