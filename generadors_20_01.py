def devuelveCiudades(*ciudades):
    for elemento in ciudades:
        yield elemento
ciudades_devueltas=devuelveCiudades("Madrid", "Barcelona", "Jaén", "Córdoba")
print(next(ciudades_devueltas))
                                
print(next(ciudades_devueltas))
                                  