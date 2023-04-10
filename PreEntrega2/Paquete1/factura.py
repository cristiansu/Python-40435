import datetime
import pandas as pd
import numpy as np
import openpyxl
import os


class Factura():


    def __init__(self):
        self.clave=int(input('Ingresar del número de la factura : '))
        self.monto=float(input('Ingresar el monto de la factura : '))
        self.fecha=datetime.datetime.now()
        self.path='./bd'
        self.file='facturas.xlsx'
        Factura.facturacion(self)

    def facturacion(self):
        factura={'NumFactura':self.clave,'Monto':self.monto,'Fecha':self.fecha}
        Factura.ingresar(self,factura)

    def __str__(self):
        msj=f'La factura número {self.clave} ha sido ingresada\nMonto = {self.monto}\nFecha = {self.fecha}'
        return msj

    def ingresar(self,factura):

        filepath=os.path.join(self.path,self.file)
        temp=pd.read_excel(filepath)
        df=pd.DataFrame(factura,index=[0])
        bd=pd.concat([temp,df],axis=0)

        writer=pd.ExcelWriter(filepath,mode='a',engine='openpyxl',if_sheet_exists='overlay')
        bd.to_excel(writer, sheet_name='base',index=False)
        writer.save()
        writer.close()
    
def reporte():
    path='./bd'
    file='facturas.xlsx'
    filepath=os.path.join(path,file) 
    base=pd.read_excel(filepath)
    print('-----Base de facturas registrados ------')
    print(base)