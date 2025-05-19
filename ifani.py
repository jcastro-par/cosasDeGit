print("Calculo de notas")
nota_alumno=int(input("Introduce la nota del alumno"))
if nota_alumno<5:
    print("Induficiente")
elif nota_alumno< 6:
    print ("Suficiente")
elif nota_alumno<7:
    print("Bien")
elif nota_alumno<9:
    print("Notable")
else:
    print("Sobresaliente")
