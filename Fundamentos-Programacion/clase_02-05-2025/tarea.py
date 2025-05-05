recargo = 0
bono = 500000

zona = input("ingrese su zona de recidencia (Norte, Centro, Sur) \n").lower()
nota = float(input("ingrese su nota de empleado [desde 1.0 a 7.0]\n"))

if zona == "sur" and nota >= 6.0:
    recargo += 25
elif zona == "sur" and nota >= 5.0 and nota < 6.0:
    recargo += 15

if zona == "centro" and nota >= 6.0:
    recargo += 20
elif zona == "centro" and nota >= 4.0 and nota <= 5.0:
    recargo += 10

if zona == "norte":
    recargo += 12
if zona == "norte" and nota >= 5.5:
    recargo += 5

descontado = bono * (recargo / 100)
bono_final = bono - descontado

print(f"su bono es de {bono} \nsu recargo es de {recargo}% \nsu bono final es de {bono_final}")