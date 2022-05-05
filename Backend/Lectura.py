import xml.etree.ElementTree as ET
import unicodedata
import re
from objetos import palabras_b,vicio,Men,fech,men_empr,men_servi,corto
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
ob_fecha=[]
mensaje_corto=[]

def LecturaDatos():
    try:
        global apex,mensaje_corto
        global prueba
        global ob_fecha
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
    
def LecturaMensaje():
    try:
        ruta = 'mensaje.xml' 
        gestion = ET.parse(ruta)
        root = gestion.getroot()
        for mensaje in root.iter('mensaje'):
            aux_mensaje = str(mensaje.text).lower()
            lista_mensaje = aux_mensaje.split(':')
            nombre = lista_mensaje[3]
            nombre = nombre.split(' ')
            nombre = nombre[1]
            social = lista_mensaje[4]
            social = social.split(' ')
            social = social[1]
            aux_mensaje = lista_mensaje[4]
            aux_mensaje=elimina_tildes(aux_mensaje)
            for i in range(len(empre)):
                hola = re.findall(empre[i],aux_mensaje)
                for k in hola:
                    tipo_empresa =empre[i]
            print(aux_mensaje)
            fecha=Lecturafecha(str(mensaje.text))
            fecha = fecha.replace(' ','')
            positivo = 0
            negativo = 0
            total=0
            for x in range(len(ser)):
                efe = re.findall(ser[x].alias,aux_mensaje)
                for z in efe:
                    tipo_servicio =ser[x].servicio
                efe = re.findall(ser[x].servicio,aux_mensaje)
                for z in efe:
                    tipo_servicio =ser[x].servicio
            for x in range(len(prueba)):
                hola = re.findall(prueba[x].palabra,aux_mensaje) 
                for k in hola:
                    #print(k)
                    total+=1
                    if prueba[x].tipo == 'p':
                        positivo += 1
                    if prueba[x].tipo == 'n':
                        negativo += 1 
            sentimiento_positivo = str(int((positivo*100)/total))
            sentimiento_negativo = str(int((negativo*100)/total))
            if sentimiento_positivo<sentimiento_negativo:
                estado = "negativo"
            elif sentimiento_positivo>sentimiento_negativo:
                estado = "positivo"
            elif sentimiento_positivo == sentimiento_negativo:
                estado = "neutro"
        

            mensaje_corto.append(corto(fecha,social,nombre,tipo_empresa,tipo_servicio,positivo,negativo,(sentimiento_positivo+'%'),(sentimiento_negativo+'%'),estado))
            ob_fecha.append(fecha)
        print(repr(mensaje_corto))
    except:
        print("Error")


def data():
    for bb in list_fecha:
        if bb not in sinrepe:
            sinrepe.append(bb)

    for bb in apex:
        if bb not in nose:
            nose.append(bb)
    #print(nose)
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

def ArchivoSalida2():
    root = ET.Element("respuesta")
    mensaje = ET.SubElement(root,"mensaje")
    for i in mensaje_corto:
        ET.SubElement(mensaje, "fecha").text = str(i.fecha)
        ET.SubElement(mensaje, "fecha").text = str(i.red_social)
        ET.SubElement(mensaje, "fecha").text = str(i.usuario)
        empresaaa = ET.SubElement(mensaje,"empresas")
        ET.SubElement(empresaaa,"empresa").attrib = {"nombre":i.empresa}
        ET.SubElement(empresaaa,"servicio").text = str(i.servicio)
        ET.SubElement(root,"palabras_positivas").text = str(i.t_positivo)
        ET.SubElement(root,"palabras_negativas").text = str(i.t_negativo)
        ET.SubElement(root,"sentimiento_positivo").text = str(i.s_positivo)
        ET.SubElement(root,"sentimiento_negativo").text = str(i.s_positivo)
        ET.SubElement(root,"sentimiento_analizado").text = str(i.s_analizado)
    def Bonito(elemento, identificador='  '):
        validar = [(0, elemento)]  

        while validar:
            level, elemento = validar.pop(0)
            children = [(level + 1, child) for child in list(elemento)]
            if children:
                elemento.text = '\n' + identificador * (level+1)  
            if validar:
                elemento.tail = '\n' + identificador * validar[0][0]  
            else:
                elemento.tail = '\n' + identificador * (level-1)  
            validar[0:0] = children 

    Bonito(root)
    archio = ET.ElementTree(root) 
    archio.write("./corto.xml", encoding='UTF-8')
    xml_str = ElementTree.tostring(root).decode()
    return xml_str 
        
def ArchivoSalida():
    global ob_men, cantidad_mensaje, cantidad_empresa, cantidad_servicio
    root = ET.Element("lista_respuesta")
    Respuesta = ET.SubElement(root,"respuesta")
    for i in cantidad_mensaje:
        ET.SubElement(Respuesta, "fecha").text = str(i.fecha)
        Mensajes = ET.SubElement(Respuesta,"mensajes")
        ET.SubElement(Mensajes,"total").text = str(i.total)
        ET.SubElement(Mensajes,"positivos").text = str(i.t_positivo)
        ET.SubElement(Mensajes,"negativos").text = str(i.t_negativo)
        ET.SubElement(Mensajes,"neutro").text = str(i.t_neutro)
        Analisis = ET.SubElement(Respuesta,"analisis")
        for j in range(len(cantidad_empresa)):
            if str(i.fecha) == str(cantidad_empresa[j].fecha):
                ET.SubElement(Analisis,"empresa").attrib = {"nombre":cantidad_empresa[j].empresa}
                Mensajes = ET.SubElement(Analisis,"mensajes")
                ET.SubElement(Mensajes,"total").text = str(cantidad_empresa[j].total)
                ET.SubElement(Mensajes,"positivos").text = str(cantidad_empresa[j].t_positivo)
                ET.SubElement(Mensajes,"negativos").text = str(cantidad_empresa[j].t_negativo)
                ET.SubElement(Mensajes,"neutro").text = str(cantidad_empresa[j].t_neutro)
                Servicios = ET.SubElement(Analisis,"servicios")
                for k in range(len(cantidad_servicio)):
                    if str(i.fecha) == str(cantidad_servicio[k].fecha) and str(cantidad_empresa[j].empresa) == str(cantidad_servicio[k].empre):
                        ET.SubElement(Servicios,"servicio").attrib = {"nombre":cantidad_servicio[k].servicio}
                        Mensajes = ET.SubElement(Servicios,"mensajes")
                        ET.SubElement(Mensajes,"total").text = str(cantidad_servicio[k].total)
                        ET.SubElement(Mensajes,"positivos").text = str(cantidad_servicio[k].t_positivo)
                        ET.SubElement(Mensajes,"negativos").text = str(cantidad_servicio[k].t_negativo)
                        ET.SubElement(Mensajes,"neutro").text = str(cantidad_servicio[k].t_neutro)
                    else:
                        None

    def Bonito(elemento, identificador='  '):
        validar = [(0, elemento)]  

        while validar:
            level, elemento = validar.pop(0)
            children = [(level + 1, child) for child in list(elemento)]
            if children:
                elemento.text = '\n' + identificador * (level+1)  
            if validar:
                elemento.tail = '\n' + identificador * validar[0][0]  
            else:
                elemento.tail = '\n' + identificador * (level-1)  
            validar[0:0] = children 

    Bonito(root)
    archio = ET.ElementTree(root) 
    archio.write("./respuesta.xml", encoding='UTF-8')
    xml_str = ElementTree.tostring(root).decode()
    return xml_str 
from xml.etree import ElementTree    


def elimina_tildes(cadena):
    s = ''.join((c for c in unicodedata.normalize('NFD',cadena) if unicodedata.category(c) != 'Mn'))
    return s

def Lecturafecha(fecha):
    try:
        fecha  = re.search(r'\d{2}(\/)\d{2}(\/)\d{4}',fecha)
        return fecha.group()
        
    except:
        return 'NoSeEncontro'
#LecturaDatos()
#data()
#ArchivoSalida()
#LecturaMensaje()
#ArchivoSalida2()