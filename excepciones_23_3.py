#Cálculo de la raíz cuadrada de un número
import math
def calculaRaiz(num1):
    if num1<0:
        raise ValueError("Número no puede ser negativo")
    else:
        return(math.sqrt(num1))
op1=(int(input("Introduce un número: ")))
try:
    print(calculaRaiz(op1))
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)
print("Progarma terminado.")
