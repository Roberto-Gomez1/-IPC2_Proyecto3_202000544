from django.http import HttpRequest
from django.http.response import HttpResponse
import datetime
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render

class Persona(object):
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido= apellido

def saludo(request):

    diccionario = {} 
    return render(request,"Rango.html",diccionario)

def curriculum(request):

    diccionario = {} 
    return render(request,"Resumen_Fecha.html",diccionario)



def curriculumNew(request):
    diccionario = {} 
    return render(request,"curriculumNew.html",diccionario)


def VistaPrinciapl(request):

    return render(request,"Main.html")

def textvaribles(request):

    diccionario = {} 
    return render(request,"documentation.html",diccionario)


def despedida(request):

    return HttpResponse("hasta luego")