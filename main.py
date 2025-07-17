
estudiantes = {}

print("registro de estudiante")
seleccion = ""
while seleccion != "0":
    print("1. Registar estudiantes")
    print("2. Mostar todos los estudiantes y cursos")
    print("3. buscar estudiante por canet")
    seleccion =input()


    if seleccion == "1":
        print("Cuantos estudiantes desea registar")
        try:
            cantidad= int(input())
        except ValueError:
            print("Dato incorrecto")
            continue

        for i in range(cantidad):
            print(f"\n Ingrese el dato de estudiante {i+1}")
            while True:
                try:
                    carnet = float(input("Carnet: "))
                    break
                except ValueError:
                    print("Dato incorrecto")
            nombre = input("Nombre: ")
            while True:
                try:
                    edad = int(input("Edad: "))
                    break
                except ValueError:
                    print("el dato deber ser en numeros")
            carrera =input("Carrera: ")
            estudiantes[carnet] = {
                "nombre": nombre,
                "edad": edad,
                "carrera": carrera,

            }

            cursos ={}
            print("Cuantos cursos desea registrar")
            try:
                cantidadCursos = int(input())
            except ValueError:
                print("Dato incorrecto")
                continue

            for c in range(cantidadCursos):
                print(f"\nIngrese los datos del curso {c + 1}")
                codigoCurso = input("Codigo curso: ")
                nombreCurso = input("Nombre del curso: ")
                notaDetarea = input("Nota de tarea: ")

                while True:
                    try:
                        codigoDecurso = int(input("ingrese el codigo: "))
                        break
                    except ValueError:
                        print("Dato incorrecto")

                while True:
                    try:
                        notaDeParcial = int(input("Nota del parcial: "))
                        break
                    except ValueError:
                        print("Dato incorrecto")

                while True:
                    try:
                        notaDeProyecto = int(input("Nota del proyecto: "))
                        break
                    except ValueError:
                        print("Dato incorrecto")

                        cursos[codigoCurso] = {
                            "notaDeparcial":notaDeParcial,

                        }

































