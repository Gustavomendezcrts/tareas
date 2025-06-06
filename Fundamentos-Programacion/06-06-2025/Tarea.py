lista_estudiantes = {
    "estudiantes" : [
        {
            "id": 1,
            "nombre": "Gustavo",
            "apellido": "Mendez",
            "edad": 18,
            "carrera": "Informatica"
        },
        {
            "id": 2,
            "nombre": "Juanito",
            "apellido": "Perez",
            "edad": 20,
            "carrera": "Informatica"
        },
        {
            "id": 3,
            "nombre": "Pepito",
            "apellido": "Gomez",
            "edad": 22,
            "carrera": "Informatica"
        },
    ]
}

while True:

    print("[1] Agregar estudiante")
    print("[2] Listar estudiante")
    print("[3] Actualizar estudiante")
    print("[4] Eliminar estudiantes")
    print("[5] Salir")
    print("--------------------------------")

    try:
        opcion = int(input("Seleccione una opcion: "))
    except ValueError:
        print("Error: Ingrese un valor valido\n\n")
        input("Presione enter para continuar")
        continue

    if opcion == 1:
        while True:
            try:
                id = int(input("Ingrese el id del estudiante: "))
                id_existe = False
                for estudiante in lista_estudiantes["estudiantes"]:
                        if id == estudiante["id"]:
                            id_existe = True
                if id_existe == True:
                    print("❌ Error: El id ya existe\n")
                    input("Presione enter para continuar")
                else:
                    nombre = input("Ingrese el nombre del estudiante: ")
                    apellido = input("Ingrese el apellido del estudiante: ")
                    edad = int(input("Ingrese la edad del estudiante: "))
                    carrera = input("Ingrese la carrera del estudiante: ")
                    agregar_estudiante = {
                        "id": id,
                        "nombre": nombre,
                        "apellido": apellido,
                        "edad": edad,
                        "carrera": carrera
                    }
                    lista_estudiantes["estudiantes"].append(agregar_estudiante)
                    print("Estudiante agregado correctamente")
                    break
            except ValueError:
                print("Error: Ingrese un valor valido\n\n")
                input("Presione enter para continuar")

    elif opcion == 2:
        for i in lista_estudiantes["estudiantes"]:
            print(f"ID: {i['id']}\nNombre: {i['nombre']} Apellido: {i['apellido']} Edad: {i['edad']} Carrera: {i['carrera']}")
            print("-----------------------------------------------------------------------------------------")


    elif opcion == 3:
        try:
            id_alumno = int(input("Ingrese el id del estudiante a actualizar: "))
            for i in lista_estudiantes["estudiantes"]:
                if id_alumno == i["id"]:
                    nombre = input("Ingrese el nombre del estudiante: ")
                    apellido = input("Ingrese el apellido del estudiante: ")
                    edad = int(input("Ingrese la edad del estudiante: "))
                    carrera = input("Ingrese la carrera del estudiante: ")
                    actualizar_estudiante = {
                        "id": id_alumno,
                        "nombre": nombre,
                        "apellido": apellido,
                        "edad": edad,
                        "carrera": carrera
                    }
                    i["nombre"] = nombre
                    i["apellido"] = apellido
                    i["edad"] = edad
                    i["carrera"] = carrera
                    print("Estudiante actualizado correctamente")
                    input("Presione enter para continuar")
                    break

        except ValueError:
            print("Error: Ingrese un valor valido\n\n")
            input("Presione enter para continuar")
       
    elif opcion == 4:
        try:
            id_alumno = int(input("Ingrese el id del estudiante a eliminar: "))
            for i in lista_estudiantes["estudiantes"]:
                if id_alumno == i["id"]:
                    lista_estudiantes["estudiantes"].remove(i)
                    print("Estudiante eliminado correctamente")
                    input("Presione enter para continuar")
                    break
        except ValueError:
            print("Error: Ingrese un valor valido\n\n")
            input("Presione enter para continuar")
            
    elif opcion == 5:
        print("Gracias por usar el programa")
        break
    else:
        print("Error: Opcion no valida\n\n")
        input("Presione enter para continuar")
