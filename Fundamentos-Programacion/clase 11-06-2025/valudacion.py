def validar_numero_entero_positivo(mensaje_input:str) -> int:
    while True:
        try:
            numero = int(input(mensaje_input))
            if numero < 0:
                print("solo se permiten numeros positivos")
                continue
        except ValueError:
            print("Error: Debe ingresar un número entero positivo.")
            continue
        return numero
    

edad = validar_numero_entero_positivo("Ingrese su edad: ")
print(f"Su edad es: {edad}")

id_producto = validar_numero_entero_positivo("Ingrese el ID del producto: ")
print(f"El ID del producto es: {id_producto}")