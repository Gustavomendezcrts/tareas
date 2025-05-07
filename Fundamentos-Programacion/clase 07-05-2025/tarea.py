#ejercicio tipo prueba 3 (de chatgpt)
zona = int(input("ingrese su zona de residencia (Norte - 1, Centro - 2, Sur - 3) \n"))
#comprobar que la zona es correcta
if zona < 1 or zona > 3:
    print("Zona incorrecta")
    exit()

nota = float(input("ingrese su nota (entre 1.0 y 7.0) \n"))
#comrobar que la nota es correcta
if nota < 1.0 or nota > 7.0:
    print("Nota incorrecta")
    exit()



recargo = 0
#norte == 1
#centro == 2
#sur == 3

#----------- Zona Sur --------------
if zona == 3 and nota >= 6.5:
    recargo += 30
elif zona == 3 and nota >= 5.5 and nota < 6.5:
    recargo += 15
#----------- Zona Centro --------------
elif zona == 2 and nota >= 6.5:
    recargo += 20
elif zona == 2 and nota >= 5.0 and nota < 5.5:
    recargo += 10
#----------- Zona Norte --------------
if zona == 1:
    recargo += 10
if zona == 1 and nota >= 6.0:
    recargo += 7


