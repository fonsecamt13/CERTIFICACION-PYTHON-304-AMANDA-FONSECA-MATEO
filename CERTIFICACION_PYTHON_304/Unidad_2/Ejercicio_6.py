tabla = [
    ["Nomnre", "Edad", "Calificacion"],
    ["Amanda", 16, 9.2],
    ["Sofia", 16, 6.0],
    ["Pedro", 17, 8.8],
    ["Ivonne", 16, 9.0],
    ["Ivan", 16, 7.6],
    ["Litzy", 15, 9.2],
    ["Cecilia", 15, 6.7],
    ["Sherlyn", 16, 9.2],
    ["Eusebia", 15, 6.0],
    ["Jimena", 16, 10.0]
]

nombre = input("Nombre a buscar: ")

for i in range(11):
    if tabla[i][0] == nombre:
        for j in range(3):
            print(f"[{i}][{j}]={tabla[i][j]}")
