
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





            print("Cuantos cursos desea registrar")
            try:
                cantidadCursos = int(input())
            except ValueError:
                print("Dato incorrecto")
                continue

            for i in range(cantidadCursos):
                print(f"\n Ingrese el dato de curso {i+1}")
                codigoCurso = input("Codigo curso: ")
                nombreCurso = input("Nombre del curso: ")
                notaDeTarea= input("nota de la  tarea: ")
                notaDeParcial= input("nota de parcial ")
                notaDeProyecto= input("nota de proyecto")

                estudiantes[carnet] ={
                    "nombre": nombre,
                    "edad": edad,
                    "carrera": carrera,
                    "codigoCurso": {
                        "nombreCurso": nombreCurso,
                        "notaDeTarea": notaDeTarea,
                        "notaDeParcial": notaDeParcial,
                        "notaDeProyecto": notaDeProyecto,

                    }
                }

    if seleccion == "2":
        print("Mostar todos los estudiantes y cursos")
        for carnet, datos in estudiantes.items():
            print(f"carnet: {carnet}")
            print(f"nombre: {datos["nombre"]}")
            print(f"carrera: {datos["carrera"]}")
            for curso in datos["codigoCurso"]["nombreCurso"]:
                print(f"codigo del curso: {datos['codigoCurso']['nombreCurso']}")
                print(f"nota de tarea: {datos['codigoCurso']['notaDeTarea']}")
                print(f"nora de parcial: {datos['codigoCurso']['notaDeParcial']}")
                print(f"nota de proyecto: {datos['codigoCurso']['notaDeProyecto']}")



    elif seleccion == "3":
        print("Ingrese el carnet del estudiante")
        buscar = input()
        if buscar in estudiantes:
            print(f"carnet: {buscar}")
            print(f"nombre: {datos['nombre']}")
            print(f"edad: {datos['edad']}")
            print(f"carrera: {datos['carrera']}")
            print("cursos")
            for curso in datos["cursos"]:
                print(f"codigo del curso: {curso['codigoCurso']}")
                print(f"nombre del curso: {curso['nombreCurso']}")
                print(f"nota de tarea: {curso['notaDeTarea']}")
                print(f"nora de parcial: {curso['notaDeParcial']}")
                print(f"nota del proyecto: {curso['notaDeProyecto']}")

            else:
                print("No se encontr<UNK> el estudiante")


















































