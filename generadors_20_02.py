def devuelveCiudades(*ciudades):
    for elemento in ciudades:
        for subElemento in elemento:
            yield subElemento
ciudades_devueltas=devuelveCiudades("Madrid", "Barcelona", "Jaén","Córdoba")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))