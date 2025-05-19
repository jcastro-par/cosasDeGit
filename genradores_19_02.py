
# si lo hacemos con generadores sería así
def generaPares2(limite):
    num=1
    while num<limite:
        yield num*2
        num=num+1
devuelvePares=generaPares2(10)
# print(next(devuelvePares))
print(next (devuelvePares))
print("Aquí va más código")
print(next (devuelvePares))
print("Aquí va más código")
print(next (devuelvePares))
print("Aquí va más código")
