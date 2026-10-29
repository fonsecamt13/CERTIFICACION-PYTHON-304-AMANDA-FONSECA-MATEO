#REALIZAR UN PROGRAMA QUE CALCULE 
#LA COMPRA TOTAL DE 4 PRODUCTOS, SI LA COMPRA TOTAL 
#ES MAYOR A 2000 PESOS ME HAGA UN DESCUENTO 
#DEL 10%
#DATOS DE ENTRDA
presio1=float(input("Introduce el precio del producto 1:"))
presio2=float(input("Introduce el precio del producto 2:"))
presio3=float(input("Introduce el precio del producto 3:"))
presio4=float(input("Introduce el precio del producto 4:"))
#PRESIO 
total=presio1+presio2+presio3+presio4
if total>2000:
    total=(total-(total*.10))
    #total=(3000-(3000*.10)) total=2700
    print(total)
else:
    print("N0 TIENES DECUENTO")