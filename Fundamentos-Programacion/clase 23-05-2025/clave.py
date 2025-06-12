print("tienes 5 intentos")

clave_valida = "gus1"

for i in range(5):
    clave = input("Introduce la clave: ")
    if clave == clave_valida:
        print("Clave correcta")
        break
    else:
        print("Clave incorrecta")
    if i == 4:
        print("Has agotado tus intentos")
        break