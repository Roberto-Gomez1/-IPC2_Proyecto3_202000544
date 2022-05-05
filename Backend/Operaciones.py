import Lectura as LD


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
