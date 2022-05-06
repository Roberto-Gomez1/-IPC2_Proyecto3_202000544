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



def genrarGRAFPRango(fechaS,FechaF,empresa):
    try: 
        eje_x = []
        eje_y= []

        fechaInicio = LecturafechaEntrada(fechaS)
        fechaInicio = fechaInicio.replace(" ","")
        fechaFinal = LecturafechaEntrada(FechaF)
        fechaFinal = fechaFinal.replace(" ","")
        empresa = empresa.replace(" ","")

        diaIncio = int(fechaInicio[0: 2])
        mesInicio = int(fechaInicio[3: 5])
        yearInicio = int(fechaInicio[6: 10])
    
        diaFinal = int(fechaFinal[0: 2])
        mesFinal = int(fechaFinal[3: 5])
        yearFinal = int(fechaFinal[6: 10])
        df = ""
        first_date = datetime.date(yearInicio, mesInicio, diaIncio)
        finish_date = datetime.date(yearFinal, mesFinal, diaFinal)
        cadena = "Resumen por fechas y empresa: "+empresa 
        
        df += cadena + "\n"
        temp = 0
        total_positivo = 0
        total_negativo = 0
        total_neutro = 0

        for i in LD.cantidad_servicio:
            diaTemp = int(i.fecha[0: 2])
            mesTemp = int(i.fecha[3: 5])
            yearTemp = int(i.fecha[6: 10])
            now_date = datetime.date(yearTemp, mesTemp, diaTemp)
            if now_date >= first_date and now_date <= finish_date:
                #eje_x.append(i.fecha)
                if empresa == i.empre:
                    temp += i.total
                    total_positivo += i.t_positivo
                    total_negativo += i.t_negativo
                    total_neutro += i.t_neutro                   
                elif empresa == 'todas':
                    for x in LD.cantidad_servicio:
                        diaTemp1 = int(x.fecha[0: 2])
                        mesTemp1 = int(x.fecha[3: 5])
                        yearTemp1 = int(x.fecha[6: 10])
                        now_date1 = datetime.date(yearTemp1, mesTemp1, diaTemp1)
                        if now_date1 >= first_date and now_date1 <= finish_date:
                            temp += x.total
                            total_positivo += x.t_positivo
                            total_negativo += x.t_negativo
                            total_neutro += x.t_neutro
                #eje_y.append([temp,total_positivo,total_negativo,total_neutro])
                break
        eje_x = ['Total:','Total Positivo','Total Negativo','Total Neutro']
        eje_y = [temp,total_positivo,total_negativo,total_neutro]           
        plt.bar(eje_x, eje_y)
        plt.ylabel('Cantidad de Mensajes')
        plt.xlabel('Estado')
        

        plt.title('Resumen  por rango de: ' + fechaInicio + " a " + fechaFinal + " opcion: " + empresa)
        plt.savefig('ResumenRango.png')
        plt.close()
        html = ""
        escribir = "<center><h6 class=\"titulos\" ><b> Reporte de resumen de cuentas </b></h6> <br> <img src='ResumenRango.png'>"
        html += htmlInicial + escribir + htmlFinal

   
        
        FileHTML=open("./ResumenRango.HTML","w") 
        FileHTML.write(html) 
        FileHTML.close() 
        path = 'ResumenRango.HTML'
        webbrowser.open_new(path)
      

    except:
        print("La creación del Reporte falló")
    else:
         print("Se ha creado el Reporte Token" )


def genrarPDFRango(fechaS,FechaF,empresa):
    fechaInicio = LecturafechaEntrada(fechaS)
    fechaInicio = fechaInicio.replace(" ","")
    fechaFinal = LecturafechaEntrada(FechaF)
    fechaFinal = fechaFinal.replace(" ","")
    empresa = empresa.replace(" ","")
    
    diaIncio = int(fechaInicio[0: 2])
    mesInicio = int(fechaInicio[3: 5])
    yearInicio = int(fechaInicio[6: 10])
    first_date = datetime.date(yearInicio, mesInicio, diaIncio)
    diaFinal = int(fechaFinal[0: 2])
    mesFinal = int(fechaFinal[3: 5])
    yearFinal = int(fechaFinal[6: 10])
    finish_date = datetime.date(yearFinal, mesFinal, diaFinal)
    data = []
    df = ""
    
    cadena = "Resumen por fechas y empresa: "+empresa 
    
    df += cadena + "\n"
    Encabezados= []
    Data = []
    Data1 = []
    Data2 = []
    Data3 = []
    aux_empre =[]
    temp = 0
    total_positivo = 0
    total_negativo = 0
    total_neutro = 0
    aux_empre.append("Empresa: "+empresa)
    for i in LD.cantidad_servicio:
        diaTemp = int(i.fecha[0: 2])
        mesTemp = int(i.fecha[3: 5])
        yearTemp = int(i.fecha[6: 10])
        now_date = datetime.date(yearTemp, mesTemp, diaTemp)
        if now_date >= first_date and now_date <= finish_date:
            Encabezados.append("Fecha: "+i.fecha )
            if empresa == i.empre:
                temp += i.total
                total_positivo += i.t_positivo
                total_negativo += i.t_negativo
                total_neutro += i.t_neutro                   
            elif empresa == 'todas':
                for x in LD.cantidad_servicio:
                    diaTemp1 = int(x.fecha[0: 2])
                    mesTemp1 = int(x.fecha[3: 5])
                    yearTemp1 = int(x.fecha[6: 10])
                    now_date1 = datetime.date(yearTemp1, mesTemp1, diaTemp1)
                    if now_date1 >= first_date and now_date1 <= finish_date:
                        temp += x.total
                        total_positivo += x.t_positivo
                        total_negativo += x.t_negativo
                        total_neutro += x.t_neutro
                                
            Data.append(("Total de Mensajes: " + str(temp)))
            Data1.append(("Mensajes positivos: " + str(total_positivo)))
            Data2.append(("Mensajes negativos: " + str(total_negativo)))
            Data3.append(("Mensajes neutros: " + str(total_neutro)))
            temp = 0
            total_positivo = 0
            total_negativo = 0
            total_neutro = 0
            break
    data.append(aux_empre)
    data.append(Encabezados)
    data.append(Data)
    data.append(Data1)
    data.append(Data2)
    data.append(Data3)
                      
    
    tablas(data,'ResumenPorRangos.pdf')
    path = 'ResumenPorRangos.pdf'
    webbrowser.open_new(path)

def ResumenPorRango(fechaS,FechaF,empresa):
    fechaInicio = LecturafechaEntrada(fechaS)
    fechaInicio = fechaInicio.replace(" ","")
    fechaFinal = LecturafechaEntrada(FechaF)
    fechaFinal = fechaFinal.replace(" ","")
    empresa = empresa.replace(" ","")
    validacion = False
    diaIncio = int(fechaInicio[0: 2])
    mesInicio = int(fechaInicio[3: 5])
    yearInicio = int(fechaInicio[6: 10])
   
    diaFinal = int(fechaFinal[0: 2])
    mesFinal = int(fechaFinal[3: 5])
    yearFinal = int(fechaFinal[6: 10])
    first_date = datetime.date(yearInicio, mesInicio, diaIncio)
    finish_date = datetime.date(yearFinal, mesFinal, diaFinal)

    df = ""
    
    cadena = "Resumen por fechas y empresa: "+empresa 
    
    df += cadena + "\n"
    temp = 0
    total_positivo = 0
    total_negativo = 0
    total_neutro = 0
    for i in LD.cantidad_servicio:
        diaTemp = int(i.fecha[0: 2])
        mesTemp = int(i.fecha[3: 5])
        yearTemp = int(i.fecha[6: 10])
        now_date = datetime.date(yearTemp, mesTemp, diaTemp)
        if now_date >= first_date and now_date <= finish_date:
            df += "Fecha: "+i.fecha + ":\n"
            if empresa == i.empre:
                temp += i.total
                total_positivo += i.t_positivo
                total_negativo += i.t_negativo
                total_neutro += i.t_neutro                   
            elif empresa == 'todas':
                for x in LD.cantidad_servicio:
                    diaTemp1 = int(x.fecha[0: 2])
                    mesTemp1 = int(x.fecha[3: 5])
                    yearTemp1 = int(x.fecha[6: 10])
                    now_date1 = datetime.date(yearTemp1, mesTemp1, diaTemp1)
                    if now_date1 >= first_date and now_date1 <= finish_date:
                        temp += x.total
                        total_positivo += x.t_positivo
                        total_negativo += x.t_negativo
                        total_neutro += x.t_neutro
            df += str("Total de mensajes: "+str(temp)) + "\n"
            df += str("Mensajes positivos: "+str(total_positivo)) + "\n"
            df += str("Mensajes negativos: "+str(total_negativo)) + "\n"
            df += str("Mensajes neutros: "+str(total_neutro)) + "\n"
            temp = 0
            total_positivo = 0
            total_negativo = 0
            total_neutro = 0
            break      
    return df

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
        plt.savefig('ResumenEmpresaFecha.png')
        plt.close()
        escribir = "<center><h6 class=\"titulos\" ><b> Reporte de resumen de cuentas </b></h6> <br> <img src='ResumenEmpresaFecha.png'>"
        html += htmlInicial + escribir + htmlFinal

    
        
        FileHTML=open("./ResumenEmpresaFecha.html","w") 
        FileHTML.write(html) 
        FileHTML.close() 
        path = 'ResumenEmpresaFecha.html'
        webbrowser.open_new(path)
      

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


htmlInicial = """<!DOCTYPE html>
<html>

<!--Encabezado-->
<head>
<meta charset="iso-8859-1">
<meta name="name" content="Reporte">
<meta name="description" content="name">
<meta name="keywods" content="python,dos,tres">
<meta name="robots" content="Index, Follow">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" type="text/css" href="css/styles.css"/>
<title>Reporte</title>
</head>
<!----Curerpo--->
<body>
   """

htmlFinal = """<br><footer style="background-color:white;"> Roberto Carlos Gómez Donis - 202000544</footer>
</center></body>
</html>"""