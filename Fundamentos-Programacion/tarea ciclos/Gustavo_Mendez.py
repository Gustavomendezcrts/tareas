
##Se le pregunta al usuario la cantidad de boletos a vender
while True:
    try:
        cantidad = int(input("Ingrese la cantidad de boletos vendidos: "))
        break
    except ValueError:
        print("Error: Debe ingresar un número entero.")
        exit()
##iniciar variable totalIngresos
totalIngresos = 0

##se valida que el boleto sea valor numerico entero y se suma si es correcto
if cantidad == 0:
    print("Error: No pueden vender 0 boletos.")
    exit()
else:
    for i in range(1, cantidad+1):
        try:
            totalIngresos += int(input(f"Ingrese el valor del boleto {i}: $"))
        except ValueError:
            print("Error: Debe ingresar un número entero.")
            break

##se imprime el total de ingresos
print(f"El valor total de los boletos vendidos es: ${totalIngresos}")