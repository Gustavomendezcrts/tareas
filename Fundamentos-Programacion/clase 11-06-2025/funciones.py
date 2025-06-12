# sin argumentos - sin retorno
def sumar():
    """Esta función imprime un mensaje que dice hooola."""
    print("hooooola")

# sumar()

#===========================================================
# con argumentos - sin retorno
def sumar(n1:int, n2:int, nombre:str = ""):
    """Esta función imprime la suma de dos números."""
    print("N1", n1, "\nN2", n2)
    print(n1 + n2)
# sumar(10,58)
# sumar(n2=40, n1=60, nombre="Juan")


#===========================================================
# sin argumentos - con retorno
def multiplicar() -> int:
    return 9 * 10

# print(multiplicar())

# resultado_multiplicar = multiplicar()
# print(resultado_multiplicar)

#===========================================================

# con argumentos - con retorno
def multiplicar(n1:int, n2:int) -> int:
    """Esta función retorna la multiplicación de dos números."""
    return n1 * n2

# print(multiplicar(5, 5))

def valida_texto(mensaje_input:str) -> str:
    while True:
        texto = input(mensaje_input)
        if len(texto.strip()) == 0:
            print("Error: El texto no puede estar vacío.")
        elif len(texto) > 1:
            print("el texto no puede tener mas de un caracter")
        else:
            return texto

opc = valida_texto("Ingrese a, b o c: ")