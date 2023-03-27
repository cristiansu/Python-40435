# Actividad 1

def biciesto(agno):
    if type(agno)==int:
        if (agno % 4 == 0) and (agno % 100 != 0) or (agno % 400 == 0):   
            print(f'El año {agno} es biciesto')  
        else: 
            print(f'El año {agno} NO es biciesto')  
    else:
        print(f'Error!!! Ud ingresó {agno}. Debe ingresar un numero entero')                       

biciesto(2012)
biciesto(2010)
biciesto(2000)
biciesto(1900)
biciesto('A012')