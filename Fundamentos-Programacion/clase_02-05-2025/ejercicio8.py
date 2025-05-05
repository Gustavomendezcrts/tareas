text1 = input("Introduce el primer texto: ")
text2 = input("Introduce el segundo texto: ")

tamaño1 = len(text1)
tamaño2 = len(text2)

if tamaño1 > tamaño2:
    print("El primer texto es más largo")
    print(text1)
elif tamaño1 < tamaño2:
    print("El segundo texto es más largo")
    print(text2)
    