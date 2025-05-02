nota = float(input("Ingrese su nota de ingreso (1.0 a 7.0): "))
zona = input("Ingrese su zona de origen (Norte, Centro o Sur): ").lower()

bono_base = 2500000
descuento = 0

if zona == "norte":
    descuento = 12
    if nota >= 5.5:
        descuento += 5
elif zona == "centro":
    if nota > 6.0:
        descuento = 20
    elif 4.0 <= nota <= 5.0:
        descuento = 10
elif zona == "sur":
    if nota > 6.0:
        descuento = 25
    elif 5.0 <= nota <= 6.0:
        descuento = 15

monto_descuento = bono_base * (descuento / 100)
bono_final = bono_base - monto_descuento

print("Descuento aplicado:", descuento, "%")
print("Monto final del bono: ${:,.0f}".format(bono_final))
print("¡Beneficio procesado con éxito!")