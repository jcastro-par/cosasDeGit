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
            return("El cohe estáen marcha.")
        else:
            return ("El cohe está parado")

        




    # Vamos a construir un objeto de esa clase
miCoche=Coche() #instanciamos una clase
print("El largo del coche es : ",miCoche.largoChasis)
print("El cohe tiene:", miCoche.ruedas, "ruedas")
miCoche.arrancar()
print(miCoche.estado())