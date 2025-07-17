
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

            print("Cuantos cursos desea registar")
            try:
                canridadCursos=int(input())
            except ValueError:
                print("Dato incorrecto")
                continue

            for c in range (canridadCursos):
                print(f"\n Ingrese el dato de curso {c+1}")
                nombreCurso =input("Nombre Del curso: ")
                notaDetarea =input("Nota del curso: ")
                notaDeParcial= int("Nota del parcial: ")
                notaDeProyecto= int("Nota del proyecto: ")

            estudiantes[nombreCurso] = {
                "notaDetarea": notaDetarea,
                "notaDeParcial": notaDeParcial,
                "notaDeProyecto": notaDeProyecto,
            }

















