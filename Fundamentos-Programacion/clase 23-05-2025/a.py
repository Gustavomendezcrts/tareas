for i in range(5):
    print(i)
    while True:
        try:
            edad = int(input("Introduce tu edad: "))
        except ValueError:
            print("Error: Debes ingresar un número válido.")
        continue
