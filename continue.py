nombre=input ("Dime tu nombre: ")
for letra in nombre:
    if letra=="e":
        # Cuando letra es igual a "e", no la imprime y pasa al siguiente.
        continue 
print (letra)