import os, time

num1 = 0
num2 = 0
result = 0



while True:
    try:
        num1 = int(input("Introduce el primer número: "))
        num2 = int(input("Introduce el segundo número: "))
        if num2 < 0 or num1 < 0:
            print("El número debe ser positivo.")
            continue
    except ValueError:
        print("Entrada no válida. Por favor, introduce números enteros.")
        continue
    else:
        break

while True:
    print("--------M E N U --------")
    print("[1] - sumar")
    print("[2] - restar")
    print("[3] - multiplicar")
    print("[4] - dividir")
    print("[5] - salir")
    try:
        opcion = int(input("Elige una opción: "))
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número del 1 al 5.")
        break
    print("-------------------------")

    if opcion == "1":
        print("El resultado de la suma es: ", num1 + num2)
    elif opcion == "2":
        print("El resultado de la resta es: ", num1 - num2)
    elif opcion == "3":
        print("El resultado de la multiplicación es: ", num1 * num2)
    elif opcion == "4":
        print("El resultado de la división es: ", num1 / num2)
    elif opcion == "5":
        print("saliendo del programa...")
        time.sleep(1)
        print("Byee ;)\n")
        break
    else:
        print("Opción no válida, intenta una opcion del 1 al 5.")
        time.sleep(1)
        os.system("cls")