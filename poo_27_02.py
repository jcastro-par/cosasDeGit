class Coche():
    #propiedades-atributos
    def __init__(self):
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False
    
    #comportamiento -métodos
    def arrancar(self, arrancamos):
        self.__enmarcha=arrancamos
        if self.__enmarcha:
            return ("El coche esta en marcha.")
        else:
            return ("El coche está parado. ")
    def estado(self):
        print("El coche tiene ", self.__ruedas, "ruedas. Un ancho de chasis de :", self.__anchoChasis, " y un " \
        "largo de chásis de ", self.__largoChasis)

# Vamos a construir un objeto de esa clase

miCoche=Coche() #instanciamos una clase
print("SALIDA DEL PROGRAMA")
print(miCoche.arrancar(True))

miCoche.estado()
# a continuación el video rueda
print("A continuación creamos el segundo objeto")
print("*****************************************")
#Creamos la segunda instancia de coche
miCoche2=Coche()

print (" Aquí va el  compartmaniento de arrancar del segundo coche")

print (miCoche2.arrancar(False))

miCoche2.ruedas=2

miCoche2.estado()