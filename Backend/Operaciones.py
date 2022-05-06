import Lectura as LD
import re
import pandas as pd
from tabla import tablas
import webbrowser
import datetime

import matplotlib.pyplot as plt

def limpiar():
    LD.ob_men[:]=[]
    LD.cantidad_empresa[:]=[]
    LD.cantidad_mensaje[:]=[]
    LD.cantidad_servicio[:]=[]
    LD.mensaje_corto[:]=[]
    print(LD.ob_men,"Arreglo1")
    print(LD.cantidad_empresa,"Arreglo2")
    print(LD.cantidad_mensaje,"Arreglo2")
    print(LD.cantidad_servicio,"Arreglo3")
    print(LD.mensaje_corto,"Arreglo4")

def limpiar1():
    LD.mensaje_corto[:]=[]
    print(LD.mensaje_corto,"Arreglo4")




def GenerarGrafo(fecha,empresa):
    try: 
        global htmlInicial
        global htmlFinal

        html = ""
        fechaNew = LecturafechaEntrada(fecha)
        fechaNew = fechaNew.replace(" ","")
        empresa = empresa.replace(" ","").lower()

        total_empresa= 0
        total_positivo = 0
        total_negativo = 0
        total_neutro = 0

        validacion = False
        
        for i in LD.cantidad_servicio:
            if i.fecha == fechaNew:
                if empresa == i.empre:
                    total_empresa += i.total
                    total_positivo += i.t_positivo
                    total_negativo += i.t_negativo
                    total_neutro += i.t_neutro
                    validacion = True
                elif empresa == 'todas':
                    for x in LD.cantidad_servicio:
                        if x.fecha == fechaNew:
                            total_empresa += x.total
                            total_positivo += x.t_positivo
                            total_negativo += x.t_negativo
                            total_neutro += x.t_neutro
                    validacion = True
                break
        
    
        eje_x = ['Total:','Total Positivo','Total Negativo','Total Neutro']
        eje_y = [total_empresa,total_positivo,total_negativo,total_neutro]
            

        plt.bar(eje_x, eje_y)
        

        plt.ylabel('Cantidad de Mensajes')
        
    
        plt.xlabel('Empresa ' + str(empresa))
        

        plt.title('Resumen de fechas del: ' + fechaNew )
        plt.savefig('./documentacion/ResumenEmpresaFecha.png')
        plt.close()
        '''escribir = "<center><h6 class=\"titulos\" ><b> Reporte de resumen de cuentas </b></h6> <br> <img src='ResumenEmpresaFecha.png'>"
        html += htmlInicial + escribir + htmlFinal

    
        
        FileHTML=open("ResumenEmpresaFecha.html","w") 
        FileHTML.write(html) 
        FileHTML.close() 
        path = 'ResumenEmpresaFecha.html'
        webbrowser.open_new(path)'''
      

    except:
        print("La creación del Reporte falló")
    else:
         print("Se ha creado el Reporte Token" )


def genrarPDFechaEmpresa(fecha,empresa):
    fechaNew = LecturafechaEntrada(fecha)
    fechaNew = fechaNew.replace(" ","")
    empresa = empresa.replace(" ","")

    total_empresa= 0
    total_positivo = 0
    total_negativo = 0
    total_neutro = 0

    validacion = False
    
    for i in LD.cantidad_servicio:
        if i.fecha == fechaNew:
            if empresa == i.empre:
                total_empresa += i.total
                total_positivo += i.t_positivo
                total_negativo += i.t_negativo
                total_neutro += i.t_neutro
                validacion = True
            elif empresa == 'todas':
                for x in LD.cantidad_servicio:
                    if x.fecha == fechaNew:
                        total_empresa += x.total
                        total_positivo += x.t_positivo
                        total_negativo += x.t_negativo
                        total_neutro += x.t_neutro
                        validacion = True
            break
    data = []
    Fecha = []
    Empresa = []
    valores = []
    if validacion:
        Fecha.append("Fecha: " + fechaNew)
        Empresa.append("Empresa: " + str(empresa))
        valores.append("Total de Mensajes: " + str(total_empresa))
        valores.append("Mensajes positivos: " + str(total_positivo))
        valores.append("Mensajes negativos: " + str(total_negativo))
        valores.append("Mensajes neutros: " + str(total_neutro))
        
    else:
        valores.append("No se encontro Fecha o Empresa indicada")
    
    data.append(Fecha)
    data.append(Empresa)
    data.append(valores)
    tablas(data,'ResumenPorFecha_Empresa.pdf')
    path = 'ResumenPorFecha_Empresa.pdf'
    webbrowser.open_new(path)

def ResumenEmpresafecha(fecha,empresa):
    fechaNew = LecturafechaEntrada(fecha)
    fechaNew = fechaNew.replace(" ","")
    empresa = empresa.replace(" ","")

    total_empresa= 0
    total_positivo = 0
    total_negativo = 0
    total_neutro = 0

    validacion = False
    
    for i in LD.cantidad_servicio:
        if i.fecha == fechaNew:
            if empresa == i.empre:
                total_empresa += i.total
                total_positivo += i.t_positivo
                total_negativo += i.t_negativo
                total_neutro += i.t_neutro
                validacion = True
            elif empresa == 'todas':
                for x in LD.cantidad_servicio:
                    if x.fecha == fechaNew:
                        total_empresa += x.total
                        total_positivo += x.t_positivo
                        total_negativo += x.t_negativo
                        total_neutro += x.t_neutro
                        validacion = True
            break
            
    
    if validacion:
        text = "Fecha: " + str(fechaNew) + "\nEmpresa: " + str(empresa) + "\nTotal Empresa: " + str(total_empresa)+ "\nMensajes Positivos: " + str(total_positivo)+ "\nMensajes Negativos: " + str(total_negativo)+ "\nMensajes Neutros: " + str(total_neutro)
    else:
        text = "No se encontro Fecha o Empresa indicada"
    
   
    return text


def LecturafechaEntrada(fecha):

    try:
        fechas = ""
        arreglo = fecha.split("-")
        arreglo.reverse()
        for i in arreglo:
            fechas += i
            if len(i) == 4:
               pass
            else:
                fechas += "/"
        return fechas
        
    except:
        return 'NoSeEncontro'