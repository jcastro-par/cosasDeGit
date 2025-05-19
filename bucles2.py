print("Programa de bucles.")
nombre=input("Dime tu nombre: ")
letra=0
for i in nombre:
    letra=letra+1
print(len(nombre))
print ("El nombre tiene " + str(letra))

# contar los caracteres excluyendo los espacios en blanco
contador=0
for i in nombre:
    if i== " ":
        continue
    contador=contador+1
print ("Nº de letras:", contador)