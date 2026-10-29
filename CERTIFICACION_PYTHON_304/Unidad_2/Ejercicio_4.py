#El mapa del tesoro
mapa=[
    [".",".",".","."],
    [".",".","X","."],
    [".",".",".","."],
    [".",".",".","."]
]
filas=len(mapa)
columnas=len(mapa)
#Recorriemdo la matriz con ciclos anidados
#Ciclos axterno para manrjar filas(i)
for i in range(filas):
    #Ciclos extrorno para manejar culimnas(j)
    for j in range(columnas):
        #Verificamos si entramos el tesoro
        if mapa[i][j]=="X":
            print(f"Mapa encontraron en la posicion [{i}][{j}]")