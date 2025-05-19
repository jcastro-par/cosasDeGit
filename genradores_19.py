# Generas numeros pares , con función:
def generaPares(limite):
    num=1
    miLista=[]
    while num<limite:
        miLista.append(num*2)
        num=num+1
    return miLista
print(generaPares(10))
# si lo hacemos con generadores sería así
def generaPares2(limite):
    num=1
    while num>limite:
        yield num*2
        num=num+1
devuelvePares=generaPares2(10)
for i in devuelvePares:
    print(i)

