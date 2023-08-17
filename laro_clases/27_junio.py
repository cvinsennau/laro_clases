## 27 de junio
students = []

def addStudents(name):
    students.append(name)
    return

def showStudents(students):
    print(students)
    

while True:
    i = input("Menu Principal\n\n Opciones:\n 1 - Mostrar Alumnos\n 2 - Agregar Alumnos \n S - Salir\n\n Opción elegida: ")
    match(i):
        case "1":
            showStudents()
        case "2":
            name = input('Nombre del alumno: ')
            addStudents(name)
    if i == "s":
        print("Peace out")
        break
