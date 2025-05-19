#creación de un diccionario
miDiccionario={
"Alemania":"Berlin",
"Francia": "Paris",
"Reino Unido":"Londres",
"España":"Madrid"
}
print(miDiccionario["Francia"])

#Imprimir el diccionario completo
print(miDiccionario)

#agregar elementos al diccionario
miDiccionario["Italia"]="Lisboa"
#se que hay error
print (miDiccionario)
#sobreescribir u valor
miDiccionario["Italia"]="Roma"
print(miDiccionario)
del miDiccionario["Reino Unido"]
print(miDiccionario)
#elementos distintos en un diccionrio
miDiccionario2={
    "Alemania": "Berlin",
    23:"Jordan",
    "Mosqueteros":3
}
print(miDiccionario2)

#asignar valores de una tupla a un diccionario
miTupla=("España", "Reino Unido", "Francia", "Portugal")
miDiccionario3={
    miTupla[0]:"Madrid",
    miTupla[1]:"Londres",
    miTupla[2]:"Paris",
    miTupla[3]:"Lisboa"
}
print(miDiccionario3)
print(miDiccionario3["España"])

#asignar una tupla a una clave
miDiccionario4={
    23: "Jordan",
    "Equipo": "Chicago",
    "Nombre": "Micahel",
    "anillos":[1991,1992,1993,1996]
}
print(miDiccionario4)
print(miDiccionario4["anillos"])

#obtener las llaves de un diccinario
print(miDiccionario4.keys())
#obtener los valores de un diccionario
print(miDiccionario4.values())
#obtener el numero de elementos de un diccionario
print (len (miDiccionario4))


