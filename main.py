
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









