num = int(input("Ingresa un numero entre 1 y 10: "))

# Primer bucle: Valida que el número esté en el rango correcto
while num < 1 or num > 10:
    print("Error, debe ser entre 1 y 10")
    num = int(input("Ingresa un numero entre 1 y 10: "))

# Segundo bucle: Genera la tabla de multiplicar usando WHILE
i = 1  
while i <= 10:  
    print(f"{num} x {i} = {num * i}")
    i = i + 1  
