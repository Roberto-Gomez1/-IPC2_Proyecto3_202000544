class palabras_b():
    def __init__(self,tipo, palabra):
        self.tipo = tipo 
        self.palabra = palabra
    def __repr__(self):
        return f'\n Tipo: {self.tipo} Palabra: {self.palabra}'

class vicio():
    def __init__(self,servicio, alias):
        self.servicio = servicio
        self.alias = alias 
        
    def __repr__(self):
        return f'\n Servicio: {self.servicio} Alias: {self.alias}'

class mensaje():
    def __init__(self,fecha, empresa, servicio, estado):
        self.fecha = fecha 
        self.empresa =empresa
        self.servicio =servicio
        self.estado = estado 
    def __repr__(self):
        return f'\n Fecha: {self.fecha} Empresa: {self.empresa} Servicio: {self.servicio} Estado: {self.estado}'


