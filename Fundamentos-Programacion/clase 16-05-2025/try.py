import os
error = False
intento = 0

while True:
    try:
        edad = int(input("edad? "))
    except ValueError as e:
        os.system("cls")
        print(e)
        print("❗Error, solo ingresar numeros enteros❗")
        intento += 1
        print(f"❗Error Numero {intento}❗")
    else:
        os.system("cls")
        print(f"su edad es {edad}")

    if intento == 5:
        os.system("cls")
        print("muchos intentos fallidos")
        break