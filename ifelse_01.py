anyos=input ("Introduce tu edad")
def mayor_edad(edad):
    resultado="No es mayor de edad"
    if edad>=18:
        resultado="Sí es mayor de edad.Pasa"
    else:
        resultado="No eres mayor de edad"
    return resultado
print (mayor_edad(int(anyos)))

