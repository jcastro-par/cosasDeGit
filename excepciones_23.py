def evaluaEdad(edad):
  
    if edad<0:
        raise TypeError ("La edad no puede ser negativa.")
  
    if edad < 20:
        return ("eres muy joven")
    elif edad<40:
        return("Eres simplemente joven")
    elif edad<65:
        return "Eres maduro"
    elif edad<100:
        return "Cuiadate.."
    
print (evaluaEdad(-20))
