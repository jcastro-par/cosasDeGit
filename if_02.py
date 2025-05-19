print("Programa de evaluación de notas de alumnos")
nota_alumno=input("Introduce un valor numérico")
def evaluacion(nota):
    valoracion="aprobado"
    if nota < 5:
        valoracion="suspenso"

    return valoracion
print(evaluacion(int(nota_alumno)))
