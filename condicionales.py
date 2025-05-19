edad=99
if 0<edad<100:
    print("Edad correcta")
else:
    print("Edad incorecta")

#Evaluación de un salario
salario_presidente=int(input("Salario del presidente"))
print("Salario del Presidente "+ str( salario_presidente))

salario_director=int(input("Salario del director"))
print ("Salario del Director :"+ str(salario_director))

salario_jefe_area=int(input("Salario del Jefe de area"))
print("Salario del Jefe de Area:" + str (salario_jefe_area))

salario_administrativo=int(input("salario del Administrativo"))
print("Salario del Administartivo"+ str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
    print("Todo los salarios son correctos")
else:
    print("Algo falla")
