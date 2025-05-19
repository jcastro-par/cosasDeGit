class Coche():
    #propiedades-atributos
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False
    
    #comportamiento -métodos
    def arrancar(self):
        self.enmarcha=True
    def estado(self):
        if (self.enmarcha):
            return("El coche estáen marcha.")
        else:
            return ("El coche está parado")

    # Vamos a construir un objeto de esa clase
miCoche=Coche() #instanciamos una clase
print("El largo del coche es : ",miCoche.largoChasis)
print("El cohe tiene:", miCoche.ruedas, "ruedas")
miCoche.arrancar()
print(miCoche.estado())
# a continuación el video 27
print("A continuación creamos el segundo objeto")
print("*****************************************")
#Creamos la segunda instancia de coche
miCoche2=Coche()
print("El largo del coche es : ",miCoche2.largoChasis)
print("El cohe tiene:", miCoche2.ruedas, "ruedas")
print(miCoche2.estado())