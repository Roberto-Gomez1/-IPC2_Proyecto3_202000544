from flask import Flask, Response, request,jsonify
from flask_cors import CORS
from Lectura import LecturaDatos,ArchivoSalida,data,LecturaMensaje,ArchivoSalida2,GenrarSalidaPDF
from Operaciones import limpiar,limpiar1,GenerarGrafo,genrarPDFechaEmpresa,ResumenEmpresafecha,genrarGRAFPRango,genrarPDFRango,ResumenPorRango
import xml.etree.ElementTree as ET
import json
import pdfkit
import webbrowser
app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origin": "*"}})
#CORS (app)

@app.route('/Resumen_Fecha/eventsCleaner/', methods=['GET'])
def eventsCleaner3():
    #limpiar1()
    return Response(response='Limpiar')

@app.route ("/resume_FechaGrafo/", methods=['POST'])
def resume_FechaGrafo():
    fecha = request.json['date']
    empresa = request.json['empresa']
    GenerarGrafo(fecha,empresa)
    response =  "Se genero Grafo"
    respuesta = jsonify ({"error": False, "mensaje": response})
    return (respuesta)


@app.route ("/resume_FechaPDF/", methods=['POST'])
def resume_FechaPDF():
    fecha = request.json['date']
    empresa = request.json['empresa']
    genrarPDFechaEmpresa(fecha,empresa)
    response =  "Se genero PDF"
    respuesta = jsonify ({"error": False, "mensaje": response})
    return (respuesta)

@app.route ("/resume_Fecha/", methods=['POST'])
def resume_Fecha():
    fecha = request.json['date']
    empresa = request.json['empresa']
    response =  ResumenEmpresafecha(fecha,empresa)
    respuesta = jsonify ({"error": False, "mensaje": response})
    return (respuesta)

@app.route('/Rango/eventsCleaner/', methods=['GET'])
def eventsCleaner4():
    #limpiar1()
    return Response(response='Limpiar')


@app.route ("/resume_rango_FechaGrafoPDF/", methods=['POST'])
def resume_rango_FechaGrafoPDF():
    pdfkit.from_file('ResumenRango.html', 'sample.pdf') 
    path = 'ResumenRango.pdf'
    webbrowser.open_new(path)

    response =  "Se genero PDF del grafo"
    respuesta = jsonify ({"error": False, "mensaje": response})
    return (respuesta)

@app.route ("/resume_rango_FechaGrafo/", methods=['POST'])
def resume_rango_FechaGrafo():
    fechaS = request.json['dateInicio']
    fechaF = request.json['dateFin']
    empresa = request.json['empresa'] 
    genrarGRAFPRango(fechaS,fechaF,empresa)
    response =  "Se genero Grafo"
    respuesta = jsonify ({"error": False, "mensaje": response})
    return (respuesta)

@app.route ("/resume_rango_FechaPDF/", methods=['POST'])
def resume_rango_FechaPDF():
    fechaS = request.json['dateInicio']
    fechaF = request.json['dateFin']
    empresa = request.json['empresa'] 
    genrarPDFRango(fechaS,fechaF,empresa)
    response =  "Se genero PDF"
    respuesta = jsonify ({"error": False, "mensaje": response})
    return (respuesta)

@app.route ("/resume_rango_Fecha/", methods=['POST'])
def resume_rango_Fecha():
    fechaS = request.json['dateInicio']
    fechaF = request.json['dateFin']
    empresa = request.json['empresa'] 
    
    response =  ResumenPorRango(fechaS,fechaF,empresa)

    respuesta = jsonify ({"error": False, "mensaje": response})
    return (respuesta)




@app.route('/eventsCleaner/', methods=['GET'])
def eventsCleaner():
    limpiar()
    return Response(response='Limpiar')


@app.route('/events/', methods=['POST'])
def post_events():
    dataRquestesd = request.data.decode('iso-8859-1')
    
    data = open('data.xml', 'w+')
    data.write(dataRquestesd)
    data.close()
    
    LecturaDatos()

    return Response(response='Confirmado xml entrada')


@app.route('/events/', methods=['GET'])
def get_events():
    data()
    dataa = ArchivoSalida()
    return Response(response=dataa)

    

@app.route('/eventsPDF/', methods=['GET'])
def get_eventsPDF():
    
    data = ArchivoSalida()
    GenrarSalidaPDF(data)
    return Response(response='Se genero PDF')   

@app.route('/shorty/eventsPDF/', methods=['GET'])
def get_eventsPDF1():
    
    data = ArchivoSalida2()
    GenrarSalidaPDF(data)
    return Response(response='Se genero PDF')   

@app.route('/shorty/events/', methods=['POST'])
def post_events1():
    dataRquestesd1 = request.data.decode('iso-8859-1')
    
    data1 = open('mensaje.xml', 'w+')
    data1.write(dataRquestesd1)
    data1.close()
    LecturaMensaje()

    return Response(response='Confirmado xml mensaje')

@app.route('/shorty/eventsCleaner/', methods=['GET'])
def eventsCleaner1():
    limpiar1()
    return Response(response='Limpiar')

@app.route('/shorty/events/', methods=['GET'])
def get_events2():
    dataa1 = ArchivoSalida2()
    return Response(response=dataa1)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
