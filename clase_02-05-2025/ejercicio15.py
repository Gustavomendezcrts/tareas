nombre = input("Escribe tu nombre completo: ")
palabras = nombre.split()
iniciales = palabras[0][0] + palabras[1][0] + palabras[2][0] + palabras[3][0]
print("Identificador único:", iniciales.upper())
