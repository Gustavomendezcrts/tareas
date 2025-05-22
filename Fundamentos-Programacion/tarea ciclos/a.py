venta = 0

try:
    venta += int(input("Ingrese el valor del boleto: "))
except ValueError:
    print("Error: Debe ingresar un número entero.")
else:
    if venta < 0:
        print("Error: El valor del boleto no puede ser negativo.")
    else:
        print(f"El valor total de los boletos vendidos es: {venta}")
