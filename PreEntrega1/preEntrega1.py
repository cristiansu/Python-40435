import pandas as pd
import numpy as np
import openpyxl
import os
import sys

# ------ Pre Entrega 1 : Código para: regisgtro, almacenamiento de usuarios y claves, y login para iniciar sesión -----------

def main():
    menu()
    

def menu():
    print('Indica la acción a realizar :\n Escribe 1 para crear tu cuenta\n Escribe 2 para iniciar sesión\n Escribe 3 para ver usuarios registrados\n Escribe 4 para salir')
    accion=int(input('Ingresa el número de tu acción :'))
    if accion == 1:
        crear_cuenta()
    if accion == 2:
        sesion()
    if accion == 3:
        ver_users()
    if accion == 4:
        input('\tProceso terminado. Dar Enter para salir: ')
        sys.exit() 

def crear_cuenta():
    
    user=input('Ingrese un nombre de usuario :')
    password=input('Ingrese una contraseña alfanumerica :')

    us=[]
    pw=[]

    us.append(user)
    pw.append(password)

    datos={'User':us,'Password':pw}

    load(datos)

    print('******* Tu cuenta ha sido creada Exitosamente *******')

    menu()
    

def sesion():

    user=input('Ingresa tu nombre de usuario : ')
    passw=input('Ingresa tu contraseña : ')

    base=pd.read_excel('base_login.xlsx')

    if len(base)>0:
        msj=''
        for i in range(len(base)):
            
            if user == base['User'][i]:
                if passw == base['Password'][i]:
                    msj=f'------- Has iniciado sesión como : {user} ----------'
                    print(msj) 
                    print('-----Serás dirigido al menú ------')
                    menu() 
                             
        msj='Error!. Usuario y/o Contraseña incorrecto'
        print(msj)

def load(datos):
    temp=pd.read_excel('base_login.xlsx')
    df=pd.DataFrame(datos)
    bd=pd.concat([temp,df],axis=0)

    writer=pd.ExcelWriter('base_login.xlsx',mode='a',engine='openpyxl',if_sheet_exists='overlay')
    bd.to_excel(writer, sheet_name='base',index=False)
    writer.save()
    writer.close()

def ver_users():
    base=pd.read_excel('base_login.xlsx')
    print('-----Base de usuarios registrados ------')
    print(base)
    print('----Volviendo a menú ------')
    menu()

if __name__=='__main__':
    main()

