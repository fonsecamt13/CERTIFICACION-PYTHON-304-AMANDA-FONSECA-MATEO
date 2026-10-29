#CREANDO UN DICCIONARIO 
persona={
    "Nombre":"Amanda",
    "Edad":41,
    "Profecion":"Programador",
    "Estudiante":False
}
print(persona)
#ACCEDIENDO A UN VALOR EN ESPECIFICO
print(persona["Nombre"])
#SE PUEDE USAR EL METODO GET()
#EES UTIL POR QUE MARCA ERROR SI NO EXISTE
print(persona.get("Profecion"))
#MODIFICAR UN VALOR EXISTENTE
persona["Estudiante"]=False 
print(persona["Estudiante"])