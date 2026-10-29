try:
    alumnos = ["Ana", "Luis", "Pedro", "María", "José"]
    calificaciones = [9, 8, 10, 7, 9]
    print(alumnos[2], ":", calificaciones[2])
    print(alumnos[4], ":", calificaciones[4])

except IndexError:
    print("Ocurrió un error")