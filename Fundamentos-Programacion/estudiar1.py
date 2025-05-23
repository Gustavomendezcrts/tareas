#se importan las librerias a utilizar
import random, os, time 

#se definen las variables a utilizar y se les asigna el metodo de entrada para el usuario
nombre_cliente = input("¿Cuál es su nombre? \n").capitalize()

tipo_cliente = input("¿Qué tipo de cliente es? (Normal, Frecuente, Premium, Empresarial, Adulto Mayor) \n").capitalize()
if tipo_cliente == "Normal" or tipo_cliente == "Frecuente" or tipo_cliente == "Premium" or tipo_cliente == "Empresarial" or tipo_cliente == "Adulto Mayor" or tipo_cliente == "Adulto mayor":
    print("")
else:
    print("Tipo de cliente no válido")
    exit()

monto_compra = 0    
monto_compra = int(input("¿Cuál es el monto de su compra? \n"))
if monto_compra < 0:
    print("Monto de compra no válido")
    exit()
metodo_pago = input("¿Qué método de pago usó? (Efectivo, Débito, Crédito) \n").capitalize()

if metodo_pago == "Efectivo" or metodo_pago == "Débito" or metodo_pago == "Debito" or metodo_pago == "Crédito" or metodo_pago == "Credito":
    print("")
else:
        print("Método de pago no válido")
        exit()
recargo = 0
descuento = 0

#se obtiene el numero de la suerte del cliente
num_suerte = random.randint(1, 10)


#revisar tipo de cliente y asignar descuento
if tipo_cliente == "Normal" and monto_compra >= 100000:
      descuento += 5
elif tipo_cliente == "Frecuente" and monto_compra >= 80000:
      descuento += 10
elif tipo_cliente == "Premium" and monto_compra >= 50000:
      descuento += 15
elif tipo_cliente == "Empresarial" and monto_compra >= 200000:
      descuento += 20
elif tipo_cliente == "Adulto Mayor" and monto_compra >= 30000:
      descuento += 8


if metodo_pago == "Efectivo" and monto_compra > 50000:
    descuento += 3
elif metodo_pago == "Credito" or metodo_pago == "Crédito" and monto_compra < 20000:
    recargo += 5

if nombre_cliente.find("a") != -1 or nombre_cliente.find ("e") != -1 or nombre_cliente.find ("o") != -1:
    descuento += 2

if num_suerte == 7 or num_suerte == 9:
    descuento += 5
elif num_suerte == 1 or num_suerte == 2:
     recargo += 3
elif num_suerte == 5:
     print("Ganaste un cupon para tu proxima compra")


recargo_porcentaje = (recargo / 100)
descuento_porcentaje = (descuento / 100)

precio_recargo = monto_compra * recargo_porcentaje
precio_descuento = monto_compra * descuento_porcentaje

monto_final = (monto_compra + precio_recargo) - precio_descuento


os.system("cls")
print("BOLETA")
print(f"|Nombre cliente: {nombre_cliente}")
print(f"|Tipo de cliente: {tipo_cliente}")
print(f"|Monto de compra: {monto_compra}")
print("---------------------------------")
print(f"|Método de pago: {metodo_pago}")
print(f"|Monto total: {monto_compra}")
print(f"|Descuentos: {descuento}%")
print(f"|Recargos: {recargo}%")
print("|--------------------------------")
print(f"|Monto Final: {monto_compra}")


