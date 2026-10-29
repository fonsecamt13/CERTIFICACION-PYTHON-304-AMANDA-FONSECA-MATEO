#CREANDO UNA TUPLA
coordenadas = (10,5,20.3,30.5,10.5)#DUPLA NUMERICA 
nombres = ("Luis,Ana,Angel")#TUPLA DE CADENA DE TEXTO
coordenadas[0]=10.9
for indice,coordenada in enumerate(coordenadas):
    print(f"[{indice}]coordenada[{coordenada}]")
