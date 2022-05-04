import xml.etree.ElementTree as ET
import unicodedata
import re
from objetos import palabras_b,vicio
prueba = []
dic_neg = []
empre = []
ser =[]

def LecturaDatos():
    try:
        global dic_pos
        global dic_neg
        global empre
        global ser
        ruta = 'data.xml' 
        gestion = ET.parse(ruta)
        root = gestion.getroot()
        for Solicitud in root:

            for diccionario in Solicitud.iter('diccionario'):


                for positivos in diccionario.iter('sentimientos_positivos'):
                    for palabras in positivos.iter('palabra'):
                        po = str(palabras.text).replace(' ','').lower()
                        po = elimina_tildes(po)
                        prueba.append(palabras_b('p',po))
                
                for negativos in diccionario.iter('sentimientos_negativos'):
                    for palabras in negativos.iter('palabra'):
                        neg = str(palabras.text).replace(' ','').lower()
                        neg = elimina_tildes(neg)
                        prueba.append(palabras_b('n',neg))
                print(repr(prueba))

                for analizar in diccionario.iter('empresas_analizar'):
                    for empresa in analizar.iter('empresa'):
                        m = str(empresa[0].text).replace(' ','').lower()
                        m= elimina_tildes(m)
                        empre.append(m)
                        j=1
                        for servicio in empresa.iter('servicio'):
                            servi = str(empresa[j].attrib['nombre']).replace(' ','').lower()
                            servi = elimina_tildes(servi)
                            print(servi)
                            #aux =[]
                            for alias in servicio.iter('alias'):
                                al = str(alias.text).replace(' ','').lower()
                                al = elimina_tildes(al)
                                print(al)
                                ser.append(vicio(servi,al))
                                #print(aux)
                            j+=1
                            

                    print(empre)
                    print(repr(ser))
            for lista in Solicitud.iter('lista_mensajes'):
                for mensaje in lista.iter('mensaje'):
                    aux_mensaje = str(mensaje.text).lower()
                    lista_mensaje = aux_mensaje.split(':')
                    aux_mensaje = lista_mensaje[4]
                    aux_mensaje=elimina_tildes(aux_mensaje)
                    print(aux_mensaje)
                    fecha=Lecturafecha(str(mensaje.text))
                    for x in range(len(empre)):

                        hola = re.findall(empre[x],aux_mensaje) 
                        
                        for k in hola:
                            print('Empresa:',empre[x])
                    for x in range(len(ser)):
                        efe = re.findall(ser[x].alias,aux_mensaje)
                        for z in efe:
                            aux = str(z)
                            #print(aux)
                            if aux is False:
                                print("prueba",z)
                            print('Servicio:',ser[x].servicio,'Alias:',ser[x].alias)
    except:
        print("Error")

def elimina_tildes(cadena):
    s = ''.join((c for c in unicodedata.normalize('NFD',cadena) if unicodedata.category(c) != 'Mn'))
    return s

def Lecturafecha(fecha):
    try:
        fecha  = re.search(r'\d{2}(\/)\d{2}(\/)\d{4}',fecha)
        return fecha.group()
        
    except:
        return 'NoSeEncontro'

LecturaDatos()