import xml.etree.ElementTree as ET
import unicodedata
import re
from objetos import palabras_b,vicio,Men,fech,men_empr,Nose,men_servi
prueba = []
empre = []
ser =[]
ob_men=[]
list_fecha=[]
sinrepe=[]
aux_c_servicios=[]
cantidad_mensaje=[]
cantidad_empresa=[]
cantidad_servicio=[]
nose=[]
apex=[]
def LecturaDatos():
    try:
        global apex
        global prueba
        global empre
        global ser
        global nose
        global ob_men
        global list_fecha
        global sinrepe
        global cantidad_mensaje
        global cantidad_empresa
        global cantidad_servicio
        global aux_c_servicios
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
                #print(repr(prueba))

                for analizar in diccionario.iter('empresas_analizar'):
                    for empresa in analizar.iter('empresa'):
                        m = str(empresa[0].text).replace(' ','').lower()
                        m= elimina_tildes(m)
                        empre.append(m)
                        j=1
                        for servicio in empresa.iter('servicio'):
                            servi = str(empresa[j].attrib['nombre']).replace(' ','').lower()
                            servi = elimina_tildes(servi)
                            ser.append(vicio(servi,servi))
                            apex.append(servi)
                            #print(servi)
                            #aux =[]
                            for alias in servicio.iter('alias'):
                                al = str(alias.text).replace(' ','').lower()
                                al = elimina_tildes(al)
                                #print(al)
                                ser.append(vicio(servi,al))
                                #print(aux)
                            j+=1
                    #print(apex)        
                    #print(empre)
                    #print(repr(ser))
            for lista in Solicitud.iter('lista_mensajes'):
                for mensaje in lista.iter('mensaje'):
                    aux_mensaje = str(mensaje.text).lower()
                    lista_mensaje = aux_mensaje.split(':')
                    aux_mensaje = lista_mensaje[4]
                    aux_mensaje=elimina_tildes(aux_mensaje)
                    print(aux_mensaje)
                    fecha=Lecturafecha(str(mensaje.text))
                    fecha = fecha.replace(' ','')
                    list_fecha.append(fecha)
                    for x in range(len(empre)):

                        hola = re.findall(empre[x],aux_mensaje) 
                        
                        for k in hola:
                            aux_empresa = empre[x]
                            #print('Empresa:',empre[x])
                    for x in range(len(ser)):
                        efe = re.findall(ser[x].alias,aux_mensaje)
                        for z in efe:
                            aux_servicio =ser[x].servicio
                            #print('Servicio:',ser[x].servicio,'Alias:',ser[x].alias)
                        efe = re.findall(ser[x].servicio,aux_mensaje)
                        for z in efe:
                            aux_servicio =ser[x].servicio
                            #print('Servicio:',ser[x].servicio,'Alias:',ser[x].alias)
                    positivo = 0
                    negativo = 0
                    for x in range(len(prueba)):
                        
                        hola = re.findall(prueba[x].palabra,aux_mensaje) 
                        for k in hola:
                            if prueba[x].tipo == 'p':
                                positivo += 1
                            if prueba[x].tipo == 'n':
                                negativo += 1
                    if positivo<negativo:
                        estado = "negativo"
                    elif positivo>negativo:
                        estado = "positivo"
                    elif positivo == negativo:
                        estado = "neutro"
                    ob_men.append(Men(fecha,aux_empresa,aux_servicio,estado))
                print(repr(ob_men))
                    #print(estado)
                    
    except:
        print("Error")
    

def data():
    for bb in list_fecha:
        if bb not in sinrepe:
            sinrepe.append(bb)

    for bb in apex:
        if bb not in nose:
            nose.append(bb)
    print(nose)
    aaa = len(empre)
    aaa2=len(nose)
    for i in range(len(sinrepe)):
        total_fecha=0
        total_positivo = 0
        total_negativo = 0
        total_neutro = 0
        for k in range(len(empre)):
            e_total_fecha=0
            e_total_positivo = 0
            e_total_negativo = 0
            e_total_neutro = 0
            for l in range(len(nose)):
                s_total_fecha=0
                s_total_positivo = 0
                s_total_negativo = 0
                s_total_neutro = 0
                for j in range(len(ob_men)):
                    if ob_men[j].fecha == sinrepe[i]:
                        total_fecha += 1
                        if ob_men[j].estado == 'positivo':
                            total_positivo+=1
                        if ob_men[j].estado == 'negativo':
                            total_negativo+=1
                        if ob_men[j].estado == 'neutro':
                            total_neutro+=1
                    
                        if ob_men[j].empresa == empre[k]:
                            e_total_fecha+=1
                            if ob_men[j].estado == 'positivo':
                                e_total_positivo+=1
                            if ob_men[j].estado == 'negativo':
                                e_total_negativo+=1
                            if ob_men[j].estado == 'neutro':
                                e_total_neutro+=1
                            if ob_men[j].servicio == nose[l]:
                                    s_total_fecha += 1
                                    if ob_men[j].estado == "positivo":
                                        s_total_positivo += 1
                                    if ob_men[j].estado == "negativo":
                                        s_total_negativo += 1
                                    if ob_men[j].estado == "neutro":
                                        s_total_neutro += 1
                if s_total_fecha>0:
                    cantidad_servicio.append(men_servi(sinrepe[i],empre[k],nose[l],s_total_fecha,s_total_positivo,s_total_negativo,s_total_neutro))
                    
            if e_total_fecha>0:      
                cantidad_empresa.append(men_empr(sinrepe[i],empre[k],int(e_total_fecha/aaa2),int(e_total_positivo/aaa2),int(e_total_negativo/aaa2),int(e_total_neutro/aaa2)))
        
        cantidad_mensaje.append(fech(sinrepe[i],int(total_fecha/(aaa*aaa2)),int(total_positivo/(aaa*aaa2)),int(total_negativo/(aaa*aaa2)),int(total_neutro/(aaa*aaa2))))    
    
    
    print(repr(cantidad_servicio))
    print(repr(cantidad_empresa))
    print(repr(cantidad_mensaje))


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
data()