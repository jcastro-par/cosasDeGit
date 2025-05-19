miLista=["María", "Pepe", "Marta", "Antonio"]
print(miLista[:])

miLista2=["María", "Pepe", "Marta", "Antonio"]
print(miLista[2])
print(miLista[-1])
print(miLista2[0:3])
print(miLista2[3:])
print(miLista2[2:])
#Añadir elementos a una lista
miLista2.append("Sandra")
print(miLista2[:]) #Imprime toda la lista

miLista2.insert(2,"Luis")
print(miLista2[:])
miLista2.extend(["Lucas","Alfonso","Martina"])
print(miLista2[:])
print(miLista2.index("Alfonso"))
print("Pepea" in miLista2)
# Eliminar elementos de una lista
miLista2.remove("Alfonso")
print(miLista2[:])
miLista2.pop()
print(miLista2[:])
# Unir dos listas
milista3=["A", "B", "C"]
miLista4=["a","b"]
miLista5=milista3+miLista4
print(miLista5[:])
# Operador repetición de lista
miLista4=["a","b"] * 5
print(miLista4[:]) 

