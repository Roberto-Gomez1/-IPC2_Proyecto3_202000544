from flask import Flask, Response, request,jsonify
from flask_cors import CORS
from Lectura import LecturaDatos,ArchivoSalida,data
from Operaciones import limpiar
import xml.etree.ElementTree as ET
import json
import pdfkit
import webbrowser
app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origin": "*"}})
#CORS (app)


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
    
'''
@app.route('/eventsPDF/', methods=['GET'])
def get_eventsPDF():
    
    data = ArchivoSalida()
    GenrarSalidaPDF(data)
    return Response(response='Se genero PDF')   
'''

@app.route('/events/', methods=['GET'])
def get_events():
    data()
    dataa = ArchivoSalida()
    return Response(response=dataa)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
