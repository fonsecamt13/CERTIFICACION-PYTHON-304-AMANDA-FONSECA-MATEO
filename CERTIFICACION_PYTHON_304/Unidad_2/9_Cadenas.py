#CADENAS Y CANCATENACION CON (+)
Cadena1 = 'Hola'
Cadena2 = 'Mundo'
multilinea = """Esto es una cadena 
de varias lineas"""
print(Cadena1 + Cadena2 + multilinea)#print(f"{cadena1})
#CADENAS Y REPETICION 
eco = "ja"*3
print(eco)
#CAMBIAR UNA CADENA DE MINUSCULA A MAYUSCULA 
tu_nombre = 'Amanda'
print(tu_nombre.upper())
#CAMBIAR UNA CADENA DE MAYUSCULA  A MINUSCULA
print(tu_nombre.lower())
#REMPLAZAR TEXTO DE UNA CADENA 
frase = "Me gusta programacion"
print(frase.replace("programacion","matematicas"))
#FORMATO DE CADENAS (F-STRING)
edad = 17
nombre = 'Amanda'
mensaje = f"Hola, me llamo {nombre} y tengo {edad} años"
print(mensaje)
#CONTAR LOS CARACTERES DE UNA CADENA
texto = "¡FELICIDADES POR AUN CONTINUAR EN EL CECY!!!"
cantidad_caracteres=len(texto)
print(cantidad_caracteres)
#COMPROBAR SI UN TEXTO TIENE UNA PALABRA 
oracion = "APRENDER PYTHON ES DIVERTIDO"
if "python" in oracion:
    print("Encontrado")
else:
    print("No esta")
#VALIDAR EL CONTENIDO DE UNA CADENA 
nlista = "iiiii"
print(nlista.isalpha())
print(nlista.isdugit())