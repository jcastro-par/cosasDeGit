miTupla=("Jose", 12, 1)
miLista=list(miTupla)
print(miLista)
print(miTupla)

#Convertir una lista en tupla
miLista1=["Juan", "Pedro", 1]
miTupla1=tuple(miLista1)
print(miTupla1)
# Comprobar si un elemento esta dentro de una tupla
print ("Juan" in miTupla1)
# cuantos elementos hay dentro de una tupla
miLista2=[1,2,3,2,1,5,5]
print(miLista2)
miTupla2=tuple(miLista2)
print(miTupla2)

print(miTupla2.count(5))
#Cuantos elementos hay en una tupla
print(len(miTupla2))
# tupla con un unico elemento
miTupla3=("Jose",)
print(len(miTupla3))

#empaquetado de una tupla
miTupla4="alfonso", 8,8,1978
print(miTupla4)

#desempaquetado de uan tupla
miTupla5=("Perico", 12,5,2001)
miTupla5.append("apco")
print(miTupla5)
nombre, dia, mes, anyo=miTupla5
print(nombre)
print(anyo)
print(mes)
print(dia)
