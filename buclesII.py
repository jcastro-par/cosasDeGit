for i in ["Juan",2]:
    print(i, end=" ")
for i in ("alfonso.par@gmail.com"):
    print("Hola", end=" ")
    #comprobar si una  direccion de email es correcta
    email=False
    for i in "alfonso.profgmail.com":
        if (i=="@"):
            email=True
        
print (email)
