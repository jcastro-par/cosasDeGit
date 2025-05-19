import math
print("Programa de cálculo de raíz cuadrada.")
numero=int(input("Dime un número, para calcular la raíz cuadrada?"))
print("Tu numero es :" + str (numero))
while numero< 0:
    print("No se puede realizar  este cálculo  para números negativos")

    numero=int(input("Dime un número, para calacular la raíz cuadrada.?"))
solucion=math.sqrt(numero)
print("La solucion es: " + str(solucion))
    
