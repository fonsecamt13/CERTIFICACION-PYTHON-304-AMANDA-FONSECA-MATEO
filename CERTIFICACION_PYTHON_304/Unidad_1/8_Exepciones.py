#Ejemplo 1 sin manejo de expresiones
try:
    numero1=float(input("Ingresar el primer numero:"))
    numero2=float(input("Ingresar el segundo numero:"))
    resultado=numero1/numero2
    print(resultado)
except ZeroDivisionError:
    print("Error:No se puede dividir entre cero")
except ValueError:
    print("Error:No puedes introducir una letra")